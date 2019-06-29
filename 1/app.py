from flask import Flask, render_template
# Here we are importing the Flask module and creating a Flask web server from the Flask module.

app = Flask(__name__)
# __name__ means this current file. In this case, it will be main.py.
# This current file will represent my web application.


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/')  # It represents the default page
def hello_world():
    return 'Hello World!'


# When the user goes to my website and they go to the default page (nothing after the slash),
# then the function below will get activated.


if __name__ == '__main__': # When you run your Python script, Python assigns the name “__main__” to the script when executed.
    app.run(debug=True)
# This will run the application. Having debug=True allows possible Python errors to appear on the web page.
# This will help us trace the errors.
