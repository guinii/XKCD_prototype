
from flask import Flask,render_template
import xkcd
import os
from app import app
from app import functions
from random import randint

count = randint(50,xkcd.getLatestComicNum())



@app.route('/')
@app.route('/index')
def index():
    global count
    Comic = functions.getComicNum(count)
    name = str(Comic.number)+".png"
    return  render_template('index.html',
                            titleComic = Comic.getTitle(),
                            namePhoto = "images/"+ name,
                            linkToComic = Comic.link)

@app.route('/next')
def next():
    global count
    count += 1
    Comic = functions.getComicNum(count)
    name = str(Comic.number) + ".png"
    return  render_template('index.html',
                            titleComic = Comic.getTitle(),
                            namePhoto = "images/"+name,
                            linkToComic = Comic.link)

@app.route('/before')
def before():
    global count
    if count - 1 is not 0:
        count -= 1
    else:
        raise EnvironmentError('There is no commic with 0 index')
    Comic = functions.getComicNum(count)
    name = str(Comic.number)+".png"
    return  render_template('index.html',
                            titleComic = Comic.getTitle(),
                            namePhoto = "images/"+name,
                            linkToComic = Comic.link)

@app.route('/random')
def random():
    Comic = xkcd.getRandomComic()
    location = os.path.dirname(os.path.abspath(__file__)) + "/static/images/"
    name = str(Comic.number) + ".png"
    Comic.download(output=location, outputFile=name, silent=False)
    return  render_template('index.html',
                            titleComic = Comic.getTitle(),
                            namePhoto = "images/"+name,
                            linkToComic = Comic.link)

