# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 19:05:36 2021
simple.py
@author: felip
"""

from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    contents = f.read()
    
    soup = BeautifulSoup(contents, 'lxml')
    
    print(soup.h2)
    print(soup.head)
    print(soup.li)
    