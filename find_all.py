# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:26:55 2021

@author: felip
"""


from bs4 import BeautifulSoup
#import requests as req
with open("index.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    
    for tag in soup.find_all("li"):
        print("{0}: {1}".format(tag.name, tag.text))
        