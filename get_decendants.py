# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 19:38:26 2021

@author: felip
"""


from bs4 import BeautifulSoup
with open("index.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    root = soup.body
    root_childs = [e.name for e in root.desendants if e.name is not None]
    print(root_childs)