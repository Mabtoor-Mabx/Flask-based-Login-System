# Required Libraries
from flask import Flask, session, request, redirect, Response, url_for, render_template

# create an app
app = Flask(__name__)

# create secret key
app.secret_key = "Mabtoor111"

# create dummy username/password 

USERNAME= "Mabtoor"
PASSWORD = "1010"

# Welcome Screen Page
@app.route("/")
def home():
    # IF logged in , Show Username
    if "username" in session:
        return render_template("home.html", user= session['username'])
    else:
        return redirect(url_for('login'))
    
# Login Screen page (Username And Password)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="POST":
        uname = request.form.get('username')
        pwd = request.form.get("password")

        if uname==USERNAME and pwd == PASSWORD:
            session['username']= uname
            return redirect(url_for('home'))
        else:
            error = "Invalid Username or Password"
            return render_template('login.html', error=error)
    return render_template('login.html')

# Link for logout the session
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Main Function

if __name__=='__main__':
    app.run(debug=True)



    