
from flask import Flask, Blueprint, render_template
from booksmart.rat import Rats
import os
from flask import Flask, Blueprint, render_template, flash, redirect, url_for, session, logging
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
#from bs4 import BeautifulSoup
import smtplib
import time



booksmart_bp = Blueprint('booksmart', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')

@booksmart_bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return render_template("series.html", function=Rats(int(request.form.get("series"))))
    return render_template("series.html", function=Rats(1))



