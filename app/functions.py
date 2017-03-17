
import xkcd
import os


def getComicNum(number): #return comic and download to specific location (identified by number)
    Comic = xkcd.getComic(number, False)
    location = os.path.dirname(os.path.abspath(__file__)) + "/static/images/"
    name = str(number) + ".png"
    Comic.download(output=location,outputFile=name,silent=False)
    return  Comic



