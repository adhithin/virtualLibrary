from flask import Blueprint, render_template, request, render_template_string
from lukebp.bubblesort import bubblesort, bubble
from lukebp.squared import Squared

squared_bp = Blueprint('lukebp', __name__,
                         template_folder='templates',
                          static_folder='static', static_url_path='assets')


@squared_bp.route('/squared', methods=["GET", "POST"])
def squared():
    if request.form:
        return render_template("squared.html", fibonacci=Squared(int(request.form.get("series"))))
    return render_template("squared.html", fibonacci=Squared(2))

@squared_bp.route('/bubblesort', methods=['GET', 'POST'])
def sortform(dtype=None):
    if request.method == 'GET':
        return render_template("bubblesort.html")
    elif request.method == 'POST':
        data = request.form.get('inputintegers').split()
        if dtype == "int":
            newdata=[]
            for element in data:
                newdata.append(int(element))
            data = newdata
        bubble(data)
        newdata=[]
        for element in data:
            newdata.append(str(element))
        data = newdata

        return render_template_string('Output of Sorted Data: ' + " ".join(data))
