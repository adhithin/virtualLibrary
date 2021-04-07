import os
from flask import Flask, Blueprint, render_template, flash, redirect, url_for, session, logging
from flask import request
from lukebp.squared import Squared

squared_bp = Blueprint('lukebp', __name__,
                         template_folder='templates',)


@squared_bp.route('/squared', methods=["GET", "POST"])
def squared():
    if request.form:
        return render_template("squared.html", fibonacci=Squared(int(request.form.get("series"))))
    return render_template("squared.html", fibonacci=Squared(2))