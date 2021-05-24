# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 19:34:20 2021

@author: felip
"""

from bs4 import BeautifulSoup
with open("index.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    root = soup.html
    root_childs = [e.name for e in root.children if e.name is not None]
    print(root_childs)
    