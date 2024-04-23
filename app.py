# this is python configuration file

from flask import Flask #this is a flaskpachage

app=Flask(__name__)
@app.route('/')#default api view function
def home():
    return "this home"
@app.route('/s2s/api/signup')
def user_signup():
    return"this is user signup page"



if __name__=="__main__":
    app.run(debug=True)
