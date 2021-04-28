import os
from flask import Flask, Blueprint, render_template, flash, redirect, url_for, session, logging
import requests
from flask import request, render_template_string
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
#from bs4 import BeautifulSoup
import smtplib
import time
from randompoem.author import Authors
from randompoem.templates.kbubblesort import bubbleSort

randompoem_bp = Blueprint('randompoem', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')

@randompoem_bp.route('/sort', methods=['GET', 'POST'])
def sortform():
    if request.method == 'GET':
        return render_template("sort.html")
    elif request.method == 'POST':
        data = request.form.get('inputdata').split()
        dtype = request.form.get('typeofdata')
        if dtype == "int":
            newdata=[]
            for element in data:
                newdata.append(int(element))
            data = newdata
        bubbleSort(data)
        newdata=[]
        for element in data:
            newdata.append(str(element))
        data = newdata

        return render_template_string('Form was submitted! Sorted Data: ' + " ".join(data))


@randompoem_bp.route('/')
def random():
    poemdata = get_poem_data()
    return render_template("poem.html", poemdata=poemdata)

def get_poem_data():
    response = requests.get("https://www.poemist.com/api/v1/randompoems")
    remotedata = response.json()
    return remotedata

