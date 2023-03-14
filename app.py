from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
import json
import requests

app = Flask(__name__)

result = ""
result_log = 0
result_reg = 0

@app.route("/")
def base():
    return render_template('base.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/log", methods=['POST'])
def log():
    log = request.form.get('_login')
    passwd = request.form.get('_password')
    global result_log
    global result_reg
    
    if (['action'] == "v_log"):
        result_log = requests.post('https://spbcoit.ru/proxy/11/postgrest/rpc/log', log, passwd)
        if result_log == 0:
            return redirect(url_for('login'))
        else:
            return redirect(url_for('index'))
    else:
        result_reg = requests.post('https://spbcoit.ru/proxy/11/postgrest/rpc/reg', log, passwd)
        if result_reg == 0:
            return redirect(url_for('login'))
        else:
            return redirect(url_for('index'))
    
    
    #if result_log == 0 or result_reg == 0:
    #    return redirect(url_for('login'))
    #else:
    #    return redirect(url_for('index'))


@app.route("/send_address", methods=['POST'])
def ip_func():
    address = request.form.get('_address')
    haddress = address
    a, b = address.split("/")
    first, second, third, fourth = a.split(".")
    first = str(bin(int(first)))[2:]
    second = str(bin(int(second)))[2:]
    third = str(bin(int(third)))[2:]
    fourth = str(bin(int(fourth)))[2:]
    while len(first) != 8:
        first = "0" + first
    while len(second) != 8:
        second = "0" + second
    while len(third) != 8:
        third = "0" + third
    while len(fourth) != 8:
        fourth = "0" + fourth
    bin_ip = first + second + third + fourth
    
    bin_ip = bin_ip[:int(b)]
    for i in range (32-int(b)):
        bin_ip += "0"
    
    address = str(int(bin_ip[0:8], 2)) + "." + str(int(bin_ip[8:16], 2)) + "." + str(int(bin_ip[16:24], 2)) + "." + str(int(bin_ip[24:32], 2)) + "/" + b
    s = '{"_ip": "' + address + '"}'
    print(s)
    global result
    result = requests.post('https://spbcoit.ru/proxy/11/postgrest/rpc/send_address', s)
    result2 = requests.post('https://spbcoit.ru/proxy/11/postgrest/rpc/add_history', haddress)
    return redirect(url_for('country'))


@app.route('/get_country')
def country():
    return render_template('index.html', _country=result.text)

app.run(host='0.0.0.0', port=30011)