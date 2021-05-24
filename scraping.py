# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 19:47:24 2021

@author: felip
"""

from bs4 import BeautifulSoup
import requests as req

resp = req.get("https://www.nvcc.edu")
soup = BeautifulSoup(resp.text, 'lxml')

print(soup.title)
print(soup.title.text)
print(soup.title.parent)
