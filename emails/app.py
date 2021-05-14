import os
from flask import Flask, Blueprint, render_template, flash, redirect, url_for, session, logging
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from bs4 import BeautifulSoup
import smtplib
import time


emails_bp = Blueprint('emails', __name__,
                         template_folder='templates',
                         static_folder='static', static_url_path='assets')


@emails_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        def send_email():
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login('apstudent138@gmail.com', 'cin766fAw')

            subject = 'Hello from virtualLibrary'

            body = 'here are some book recomendations for you; check it out by using the secret password to open the page: apstudents'

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