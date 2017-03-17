
from flask import Flask,render_template
import xkcd
import os
from app import app


def getComicNum(number):
    Comic = xkcd.getComic(number, False)
    location = os.path.dirname(os.path.abspath(__file__)) + "/static/images/"
    name = str(number) + ".png"
    Comic.download(output=location,outputFile=name,silent=False)
    return  Comic



