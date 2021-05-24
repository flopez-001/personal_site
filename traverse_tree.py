# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 19:25:20 2021

@author: felip
"""

from bs4 import BeautifulSoup
with open("index.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, "lxml")
    
    for child in soup.recursiveChildGenerator():
        if child.name:
            print(child.name)
            