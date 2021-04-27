import os
from flask import Flask, Blueprint, render_template, flash, redirect, url_for, session, logging
import requests
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
#from bs4 import BeautifulSoup
import smtplib
import time
from randompoem.author import Authors


randompoem_bp = Blueprint('randompoem', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@randompoem_bp.route('/')
def random():
    poemdata = get_poem_data()
    return render_template("poem.html", poemdata=poemdata)

def get_poem_data():
    response = requests.get("https://www.poemist.com/api/v1/randompoems")
    remotedata = response.json()
    return remotedata

