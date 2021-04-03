from flask import Blueprint, render_template, request
from findabook.algorithm import Pascal

bookfinder_bp = Blueprint('findabook', __name__,
                         template_folder='templates',
                         static_folder='static', static_url_path='assets')


@bookfinder_bp.route('/')
def aditihome():
    return render_template("step1.html")

@bookfinder_bp.route('/algo', methods=["GET", "POST"])
def pascalalgo():
    if request.form:
        return render_template("algorithm.html", pascal=Pascal(int(request.form.get("series"))))
    return render_template("algorithm.html", pascal=Pascal(2))
