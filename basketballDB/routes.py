from flask import render_template, url_for, flash, redirect
from basketballDB.models import User, Post 
from basketballDB import app
from basketballDB.forms import RegistrationForm, LoginForm
from classes.teamBoard import TeamBoard
from basketballDB.listTeams import all_teams

players = [  #this is test data for roster
    {
        'name' : 'RJ Davis',
        'year': 'Senior',
        'height': '6\'0"',
        'weight': 180 
    },
    {
        'name' : 'Armando Bacot',
        'year': 'Graduate',
        'height': '6\'11"',
        'weight': 240 
    }
]

favorite_teams = [TeamBoard("UNC"), TeamBoard("Wake Forest")] # test favorite teams

@app.route("/") 
@app.route("/home") # home page can be accessed two ways
def home(): # ROOT page
    return render_template('home.html',all_teams=all_teams) # We can return HTML directly or by file.

@app.route("/roster")
def roster(): 
    return render_template('roster.html', players=players, title = 'Roster 23-24') # we can pass in test data(players) and call it using variable 'players'

@app.context_processor # context processor allows us to add variable to context of all templates
def passFavoriteTeams():
    return dict(favorite_teams = favorite_teams) 

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            flash(f'We have successfully logged you in!','success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful. Please check username and/or password.','danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/rankings/<int:team_id>")
def rankings(team_id):
    return render_template('team_board.html', title='Rankings',team_id=team_id)
