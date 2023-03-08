from flask import Flask
# from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('base.html')


@app.route("/login")
def login():
    return render_template('login.html')





# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()
