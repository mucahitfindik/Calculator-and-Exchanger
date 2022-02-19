# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
