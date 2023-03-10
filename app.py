from flask import Flask
# from flask import request
from flask import render_template


app = Flask(__name__)

@app.route("/")
def base():
    return render_template('base.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/index")
def index():
    return render_template('index.html')

def ip(address):
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
    bin_ip = first + " " + second + " " + third + " " + fourth
    
    bin_ip = bin_ip[-(32-b)]
    for i in 32-b:
        bin_ip += "0"
    
    first, second, third, fourth = a.split(".")
    address = str(int(first, 2)) + "." + str(int(second, 2)) + "." + str(int(third, 2)) + "." + str(int(fourth, 2)) + "/" + b
    return address 

