from flask import Blueprint, render_template, request

bookfinder_bp = Blueprint('findabook', __name__,
                         template_folder='templates',
                         static_folder='static', static_url_path='assets')


@bookfinder_bp.route('/')
def aditihome():
    return render_template("step1.html")