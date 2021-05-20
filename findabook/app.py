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
def sort():
    if request.method == 'GET':
        return render_template("bubblesort.html") # fetches the list from the user interface
    elif request.method == 'POST':
        userlist = request.form.get('inputintegers').split() # the variable userlist is assigned to the string of numbers that the user inputs
        newlist=[] # an empty list called newlist is created
        for element in userlist:
            newlist.append(int(element)) # every number from userlist is converted from a string to an integer and added to the end of newlist
        userlist = newlist # userlist is redefined as the list numbers that the user inputs
        BubbleSort(userlist) # userlist is passed through the procedure BubbleSort as a parameter, which sorts userlist
        newlist = [] # userlist is redefined as an empty list
        for element in userlist:
            newlist.append(str(element)) # every sorted number from userlist is converted from an integer to a string and added to the end of newlist
        userlist = newlist # userlist is redefined as the list numbers that the user inputs
        return render_template_string('Experimental Data Sorted from Least to Greatest Value: ' + " ".join(userlist)) # prints "Experimental Data Sorted from Least to Greatest Value:" and prints the sorted list of data afterwards