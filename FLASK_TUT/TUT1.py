# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 13:21:22 2019

@author: ahirr
"""
from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == '__main__' :
    app.run(debug='true')