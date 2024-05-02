from flask import Flask,render_template,flash,redirect,url_for
from flask_1.models import User,Post
from flask_1 import app
from flask_1.forms import RegistrationForm,LoginForm
posts=[
    {
        'author':"cory", 'title':'blog_post_1',"content":"The first post","date":"january 2020"
    },
    {
        "author":"harry","title":"Issues in indian farming","content":'''One of the major challenges faced by Indian agriculture is the problem of soil degradation and nutrient depletion. Soil degradation occurs due to several factors such as erosion, loss of organic matter, and chemical pollution, amongst others. As a result, Indian soil is losing its fertility at an alarming rate, leading to decreased crop yields and reduced productivity.

Farmers often resort to using chemical fertilizers to compensate for the loss of soil fertility, which only exacerbates the problem. The overuse of chemical fertilizers damages the soil microbiome and reduces its ability to retain moisture and essential nutrients.

Furthermore, soil degradation also contributes to environmental issues like air and water pollution. When soil loses its fertility, it affects the quality of crops, which in turn affects human health and well-being.

To address this issue, farmers need to adopt sustainable practices like crop rotation, intercropping, and agroforestry. These practices help to restore soil fertility and reduce soil erosion. For example, crop rotation involves planting different crops on the same land in successive seasons. This helps to replenish soil nutrients and reduce pest and disease buildup.''',"date":"nov 2023"
    }
]
@app.route("/")
def home():
    return render_template('home.html',posts=posts,title="home sweet home") #we will have access to this variable in the template

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register",methods=['POST','GET']) #list of allowed methods in our route
def register():
    form=RegistrationForm()
    #creating instance of the registration form
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}','success') #easy to send ot alert , category
        return redirect(url_for('home'));
    return render_template("register_1.html",title='Register',form=form)
# just like how we set posts , we have access to this instance form in the register template for showing the data

@app.route("/login",methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=="admin@gmail.com" and form.password.data=="hello":
            flash("You have successfully logged in","success")
            return redirect(url_for('home'))
        else:
            flash("Login unsuccessful please check your password")
    return render_template("login.html",title='Login',form=form)