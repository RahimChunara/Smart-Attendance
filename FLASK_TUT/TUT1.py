# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 13:21:22 2019

@author: ahirr
"""
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app  = Flask(__name__) 
app = Flask(__name__)

app.config['SECRET_KEY'] = '123456789'

posts = [
        {
                'author' : 'Abhishek',
                'title' : 'Blog 1',
                'contents' : 'First post',
                'date_posted' : 'September 4, 2018'
                },
                 {
                'author' : 'Aditya',
                'title' : 'Blog 2',
                'contents' : 'second post',
                'date_posted' : 'September 5, 2018'
                }
        ]


@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', posts= posts)

@app.route('/about')
def about_page():
    return render_template('about.html', title= 'Aboutpage')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
if __name__ == '__main__' :
    app.run(debug='true')