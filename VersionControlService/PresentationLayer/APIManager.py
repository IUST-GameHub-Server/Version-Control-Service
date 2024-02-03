from ..LogicLayer.VersionControlLogic import VersionControlLogic
from flask import Flask

app = Flask(__name__)
config=""

@app.route('/show_current_version')
def show_current_version(email):
    return "Not Implemented"

@app.route('/show_new_version')
def show_new_version(newVersion):
    return "Not Implemented"


@app.route('/show_update_offer')
def show_update_offer():
    return "Not Implemented"

@app.route('/show_features_of_new_version')
def show_features_of_new_version():
    return "Not Implemented"
