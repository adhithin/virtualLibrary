import os
from flask import Flask, Blueprint, render_template, flash, redirect, url_for, session, logging
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
#from bs4 import BeautifulSoup
import smtplib
import time
from booksearch.selection import Books


booksearch_bp = Blueprint('randombook', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@randombook_bp.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        return render_template("book.html", authorrecs=Authors(int(request.form.get("series"))))
    return render_template("book.html", bookrecs=Authors(1))

@randombook_bp.route('/allgenres', methods=['GET', 'POST'])
def allgenres():
    return render_template("allgenres.html")


