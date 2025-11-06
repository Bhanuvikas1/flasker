from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    first_name = 'Bhanu'
    stuff = 'This is <strong> bold </strong> text'

    icc_teams = ["India" , "South Africa" , "Sri Lanka", "Australia", "New zealand", "England" , "Pakistan" , "Bangladesh"]
    return render_template('index.html' , first_name = first_name , stuff = stuff , icc_teams = icc_teams)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html' , user_name = name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html') , 404



