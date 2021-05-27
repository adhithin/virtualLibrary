import os
from flask import Flask, Blueprint, render_template, flash, redirect, url_for, session, logging
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from bs4 import BeautifulSoup
import smtplib
import time


emails_bp = Blueprint('join', __name__,
                         template_folder='templates',
                         static_folder='static', static_url_path='assets')
app = Flask(__name__)

db = SQLAlchemy(app) ## renaming so we can abbreviate to db.

class Ebook(db.Model):
    __tablename__ = 'Ebook'
    id = db.Column(db.Integer, primary_key=True)
    # not planning to delete scores, but still a good practice
    p_title = db.Column(db.String(10), unique=False, nullable=False)
    p_price = db.Column(db.Integer, unique=False, nullable=False) # want score as int so we can sort by it easily.

    ## the initializer
    def __init__(self, p_title, p_price):
        self.p_title = p_title
        self.p_price = p_price


    def __repr__(self):
        return f"{self.p_title},{self.p_price}"

#must go after 'models'
db.create_all();

@emails_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email_list = []
        email = request.form['email']
        def send_email():
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login('adhithi.nmurthy07@gmail.com', 'yavesbrwlogwvuaa')

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



@emails_bp.route('/sell', methods=['GET', 'POST'])
def ebook():
    ## activating our procedure ebook(). our calls go through here.

    if request.method == 'POST': ## if the form in HTML is entered (the submit button is pressed) then this code segment will run
        title = request.form['name'] ## this is the book title
        price = int(request.form['rating']) ## this is the price of that book
        #the code below confirmed I had the proper data. Now to add it to the db.
        print(title)
        print(price)
        ebook_catalog = [] ## here's the list for the eBook catalog

        ## conditional: if the title field is left blank, then the website will take the user to a different page.
        if title == " ":  ## sequencing & selection
            print("no friend we need a valid book title")
            return render_template("novalidtitle.html") ## this page tells the user to enter a valid title. it has a button to go back.
        ## conditional: if the price entered is greater than 30, then the website will take the user to a different page.
        if (price > 30):  ## sequencing & selection
            print("no friend that's too much money")
            return render_template("veryhighprice.html")## this page tells the user to enter a valid price. it has a button to go back.

        ## if the title isn't left blank and the price is in the price range, this segment will be implemented
        else: ## sequencing & selection
            new_book = Ebook(title, price)
            db.session.add(new_book) ## adding the book to the database
            db.session.commit() ## adding the book and commiting the new book list

    #query the db for the ratings; sequencing & selection
    books = Ebook.query.order_by(desc('p_price')).all() ## ordering the books by price
    ebook_catalog = [] ## here's the list for the eBook catalog

    for book in books: ## iteration with for loops
        new_book = {'title':book.p_title, 'price':book.p_price}
        ebook_catalog.append(new_book) ## adding the new book into our eBook list.


    return render_template('ebooks.html', ebook_catalog = ebook_catalog)