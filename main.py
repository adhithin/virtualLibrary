import os
from flask import Flask, render_template, flash, redirect, url_for, session, logging
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
#from bs4 import BeautifulSoup
import smtplib
import time
from emails.app import emails_bp
from findabook.app import bookfinder_bp
from booksearch.app import booksearch_bp
from booksmart.app import booksmart_bp
from blueprint.luke.routes import luke


app = Flask(__name__)
app.register_blueprint(emails_bp, url_prefix='/emails')
app.register_blueprint(bookfinder_bp, url_prefix='/findabook')
app.register_blueprint(booksearch_bp, url_prefix='/booksearch')
app.register_blueprint(booksmart_bp, url_prefix='/booksmart')
app.register_blueprint(luke, url_prefix='/Mini Lab')

basedir = os.path.abspath(os.path.dirname(__file__))

# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#OMG SO IMPORTANT TO INCLUDE THIS ABOVE! Warnings up the wazoo if not here on a development server.

db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    email = 'nothing'
    if request.method == 'POST':
        email = request.form['email']
        def send_email():
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login('adhithi.nmurthy07@gmail.com', 'yavesbrwlogwvuaa')

            subject = 'Hello from virtualLibrary'

            body = 'Check out the website to learn about Bananas: https://en.wikipedia.org/wiki/Banana'

            msg = f"Subject: {subject}\n\n{body}"

            server.sendmail(
                'adhithi.nmurthy07@gmail.com',
                email,
                msg

            )

            server.quit()

        send_email()
        print("email: " + email)

    return render_template("home.html")



if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='8024', host='127.0.0.1')
