import os
from flask import Flask, Blueprint, render_template, flash, redirect, url_for, session, logging
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
#from bs4 import BeautifulSoup
import smtplib
import time


booksearch_bp = Blueprint('booksearch', __name__,
                      template_folder='templates',
                      static_folder='static', static_url_path='assets')


@booksearch_bp.route('/', methods=['GET', 'POST'])
def search():
    genres = 'nothing'
    if request.method == 'POST':
        genres = request.form.getlist('genre')
        print(genres)
        if 'Romance' and 'SciFi' and 'Nonfiction' and 'Comedy' in genres:
            return render_template("allgenres.html")
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