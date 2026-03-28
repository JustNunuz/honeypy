# Libraries
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, request, redirect, url_for
from web_honeypot import *

# Logging format with timestamp
logging_format = logging.Formatter("%(asctime)s %(message)s")

# HTTP logger
funnel_logger = logging.getLogger("HTTP Logger")
funnel_logger.setLevel(logging.INFO)
funnel_handler = RotatingFileHandler("http_audits.log", maxBytes=2000, backupCount=5)
funnel_handler.setFormatter(logging_format)
funnel_logger.addHandler(funnel_handler)

def web_honeypot(input_username="admin", input_password="password"):
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("wp-admin.html")

    @app.route("/wp-admin-login", methods=['POST'])
    def login():
        username = request.form['username']
        password = request.form['password']

        ip_address = request.remote_addr

        funnel_logger.info(f'Client with IP address: {ip_address}, entered \n Username: {username}, Password: {password}')

        if username == input_username and password == input_password:
            return redirect(url_for('redirect_page'))
        else:
            return "Invalid Username and Password"
        
    @app.route("/redirect")
    def redirect_page():
        return render_template('redirect.html')
    return app

def run_web_honeypot(port=5000, input_username="admin", input_password="password"):
    app = web_honeypot(input_username, input_password)
    app.run(debug=True, port=port, host="0.0.0.0")

if __name__ == "__main__":
    run_web_honeypot(port=5000, input_username="admin", input_password="password")
