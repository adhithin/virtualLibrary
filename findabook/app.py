from flask import Blueprint, render_template, request, render_template_string
from findabook.algorithm import Pascal
from findabook.bubblesort import BubbleSort

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

@bookfinder_bp.route('/bubblesort', methods=['GET', 'POST'])
def sortform():
    if request.method == 'GET':
        return render_template("bubblesort.html")
    elif request.method == 'POST':
        userlist = request.form.get('inputintegers').split()
        newlist=[]
        for element in userlist:
            newlist.append(int(element))
        userlist = newlist
        BubbleSort(userlist)
        newlist = []
        for element in userlist:
            newlist.append(str(element))
        userlist = newlist
        return render_template_string('Experimental Data Sorted from Least to Greatest Value: ' + " ".join(userlist))