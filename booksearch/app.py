import os
from flask import Flask, Blueprint, render_template, flash, redirect, url_for, session, logging
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from bs4 import BeautifulSoup
import smtplib
import time
from booksearch.selection import Books
from booksearch.quiz import NeuralNetwork
import numpy as np
from booksearch.bubblesort import BubbleSort


booksearch_bp = Blueprint('booksearch', __name__,
                      template_folder='templates',
                      static_folder='static', static_url_path='assets')


@booksearch_bp.route('/', methods=['GET', 'POST'])
def search():
    genres = 'nothing'
    if request.method == 'POST':
        favgenres = 0
        genres = request.form.getlist('genre')
        print(genres)
        if 'Romance' and 'SciFi' and 'Nonfiction' and 'Comedy' in genres:
            return render_template("allgenres.html")
        if 'Comedy' in genres:
            return render_template("comedy.html")
        if 'Nonfiction' in genres:
            return render_template("nonfiction.html")
        if 'Romance' in genres:
            return render_template("romance.html")
        if 'SciFi' in genres:
            return render_template("scifi.html")
        return render_template("select-book.html", bookrecs=Books(int(request.form.get("series"))), bubbles=BubbleSort(genres))
    if request.method == 'POST':
        return render_template("select-book.html", bookrecs=Books(int(request.form.get("series"))), bubbles=BubbleSort(genres))
    return render_template("select-book.html", bookrecs=Books(1))

@booksearch_bp.route('/allgenres', methods=['GET', 'POST'])
def allgenres():
    return render_template("allgenres.html")

@booksearch_bp.route('/bookquiz', methods=['GET', 'POST'])
def quiz():
    X = np.array([[0,0,1],#these are our inputs. first number: if they eat bananas. second: strawberries; third: blueberries
                  [0,1,0],
                  [1,0,0],
                  [1,1,1]])
    y = np.array([[0],[0],[0],[0]])
    return render_template("bookquiz.html", bookquiz=NeuralNetwork(X, y))

@booksearch_bp.route('/bubblesort', methods=['GET', 'POST'])
def alphabetize():
    sort = 'nothing'
    if request.method == 'POST':
        sort = request.form.getlist('sort')
    return render_template("bubblesort.html", bubbles=BubbleSort(sort))