from flask import Flask, render_template, redirect, url_for, request, flash,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///reportacrime.db"
app.secret_key = 'your_secret_key'  # Needed for flashing messages
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    phonenumber = db.Column(db.Integer)
    password = db.Column(db.String(200))

    def __repr__(self):
        return f"{self.username} - {self.password}"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Crime(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), db.ForeignKey('users.username'), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    toc = db.Column(db.String(50), nullable=False)  # Type of crime
    desc = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=func.now())

    def __repr__(self):
        return f"Crime({self.sno}, {self.username}, {self.location}, {self.toc})"

@app.route('/')
def home():
    return render_template('front_page.html')
@app.route('/front_page.html')
def home2():
    return render_template('front_page.html')
@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/faq.html')
def faq():
    return render_template('faq.html')

@app.route("/newsroom.html")
def newsroom():
    return render_template("newsroom.html")

@app.route("/login.html", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Users.query.filter_by(username=username).first()

        if user is None:
            flash("Invalid Username! Make sure you are registered!!", "error")
            return redirect('/login.html')
        
        if user.check_password(password):
            session['username']=user.username
            flash("Login Successful!", "success")
            return render_template("rc.html")
        else:
            flash("Incorrect Password! Please try again.", "error")
            return redirect("/login.html")
    
    return render_template("login.html")

@app.route("/signup.html", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form["username"]
        phonenumber = request.form["phoneno"]
        password = request.form["password"]
        
        user = Users(username=username, phonenumber=phonenumber)
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        flash("Signup successful! You can now login.", "success")
        return redirect('/login.html')
    
    return render_template("signup.html")

@app.route("/test.html")
def privacy():
    return render_template("test.html")

@app.route("/documentation.html")
def documentation():
    return render_template("documentation.html")

@app.route('/rc.html', methods=['GET', 'POST'])
def rc():
    if request.method == 'POST':
        username = request.form['username']
        location = request.form['location']
        toc = request.form['crime_type']
        desc = request.form['description']
        crimes = Crime(username=username, location=location, toc=toc, desc=desc)
        db.session.add(crimes)
        db.session.commit()
        return redirect('crimerates.html')
    return render_template("rc.html")
@app.route("/logout")
def logout():
    session.pop('username', None)
    flash("Logged out successfully!", "success")
    return redirect(url_for('login'))
@app.route('/crimerates.html')
def reportcrime():
    crime_reports = Crime.query.all()
    return render_template("crimerates.html", crimes=crime_reports)
if __name__ == "__main__":
    app.run(debug=True)