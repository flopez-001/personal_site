# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:18:36 2021

@author: felip
"""

from bs4 import BeautifulSoup
#import requests as req
with open("index.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')

print(soup.find("ul", id="mylist"))