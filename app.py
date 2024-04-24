# this is python configuration file

from flask import Flask , render_template #this is a flaskpachage

app=Flask(__name__)
@app.route('/')#default api view function
def home():
    return render_template("home.html")
@app.route('/s2s/api/signup')
def user_sigin():
    return"this is user signin"
@app.route('/s2s/api/login')
def user_login():
    return"this is user login"

@app.route('/s2s/api/blog')
def user_blog():
    return"this is user blog"




if __name__=="__main__":
    app.run(debug=True)
