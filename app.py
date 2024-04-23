# this is python configuration file

from flask import Flask #this is a flaskpachage

app=Flask(__name__)
@app.route('/')#default api view function
def home():
    return "this home"
@app.route('/s2s/api/login')
def user_signup():
    return"this is user login page"



if __name__=="__main__":
    app.run(debug=True)
