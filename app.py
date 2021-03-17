import os
from flask import Flask, render_template, flash, redirect, url_for, session, logging
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from bs4 import BeautifulSoup
import smtplib
import time

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#OMG SO IMPORTANT TO INCLUDE THIS ABOVE! Warnings up the wazoo if not here on a development server.

db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def home():
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
        print("email is sent to " + email)

    return render_template("index.html")

@app.route('/select-book', methods=['GET', 'POST'])
def selectbook():
    genres = 'nothing'
    if request.method == 'POST':
        genres = request.form.getlist('genre')
        print(genres)
        if 'Romance' and 'SciFi' and 'Nonfiction' and 'Comedy' in genres:
            return render_template("index.html")
        if 'Bananas' and 'Strawberries' in genres:
            return render_template("index.html")
        if 'Comedy' in genres:
            return render_template("index.html")
        if 'Nonfiction' in genres:
            return render_template("index.html")
        if 'Romance' in genres:
            return render_template("index.html")
        if 'SciFi' in genres:
            return render_template("index.html")
    return render_template("select-book.html")


if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='8242', host='127.0.0.1')

