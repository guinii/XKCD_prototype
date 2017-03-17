
from flask import render_template
import xkcd
import os
from app import app
from app import functions
from random import randint

count = randint(50,xkcd.getLatestComicNum()) #random number for first comic



@app.route('/')
@app.route('/index') #index route
def index():
    global count
    Comic = functions.getComicNum(count) #get the commic identified with count
    name = str(Comic.number)+".png"
    return  render_template('index.html',
                            titleComic = Comic.getTitle(),
                            namePhoto = "images/"+ name,
                            linkToComic = Comic.link)

@app.route('/next')
def next():
    global count
    if count + 1 is xkcd.getLatestComicNum()+1:   #no more comics
        raise EnvironmentError("There is no more commics")
    else:
        count += 1
    Comic = functions.getComicNum(count)
    name = str(Comic.number) + ".png" #comic identified by his number
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
    Comic = xkcd.getRandomComic() #random comic
    location = os.path.dirname(os.path.abspath(__file__)) + "/static/images/" #location
    name = str(Comic.number) + ".png"
    Comic.download(output=location, outputFile=name, silent=False) #silent False for debug possible errors
    return  render_template('index.html',
                            titleComic = Comic.getTitle(),
                            namePhoto = "images/"+name,
                            linkToComic = Comic.link)

