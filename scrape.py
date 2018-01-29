from workers import workIt
from bs4 import BeautifulSoup
import requests
import urllib.parse as urlparse
import random
import re


def WeebMachine(baseLink):
    list = {}

    main = requests.get(baseLink)
    mainSoup = BeautifulSoup(main.content, "html.parser")

    first = mainSoup.find_all("div", { "class" : "episode" })
    links = []

    for link in first:
        links.append("http://moetube.net" + link.find("a")['href'])


    if (len(links) > 0):
        for i, link in enumerate(links):
            list[i + 1] = link
        
       # mp4 = workIt(list)
    else:
        list = ["Error, link not working"]

    return workIt(list)
'''
def linkParse(list):
    parsedlist = {}
    for key, val in list.items():
        req = requests.get(val)
        soup = BeautifulSoup(req.content, "html.parser")
        try:
            parsedlink = soup.find("source")['src']
        except e:
            return ("Link not available")

        parsedlist[key] = parsedlink

    return parsedlist
'''

print(WeebMachine('http://www.moetube.net/anime/2745990/koutetsujou-no-kabaneri/1'))