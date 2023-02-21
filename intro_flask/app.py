# Uruchamiamy komendą
# $ flask run

# Jeżeli skrypt nazywa się inaczej niż app.py, np. main.py, to
# $ flask -app main run

# W trybie debug (automatyczne odświeżanie + bogatszy traceback)
# $ flask run --debug
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "<h3>Hello, world!</h3>"


from flask import render_template
@app.route("/template/")
def hello_template():
    return render_template('hello.html')


# string, int, float, path, uuid
@app.route("/name/<string:name>/")
def hello_name(name):
    return render_template(
        'hello_name.html',
        name=name
    )


from flask import request
@app.route("/form/", methods=['GET', 'POST'])
def hello_form():
    if request.method == "GET":
        return render_template('hello_form.html')

    elif request.method == "POST":
        # request.args  # dla metody GET
        # request.form  # dla metody POST
        name = request.form.get('name')

        return render_template(
            'hello_name.html',
            name=name,
        )


# # jeżeli chcemy $ python app.py
# if __name__ == '__main__':
#     app.run(debug=True)
