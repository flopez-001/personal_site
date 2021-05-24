# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:30:32 2021

@author: felip
"""


from bs4 import BeautifulSoup
#import requests as req
with open("index.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    
    tags = soup.find_all(["h2", "p"])
    for tag in tags:
        
        print(" ".join(tag.text.split()))
        