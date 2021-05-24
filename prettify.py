# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:07:44 2021

@author: felip
"""

from bs4 import BeautifulSoup
import requests as req

resp = req.get("https://www.nvcc.edu")
soup = BeautifulSoup(resp.text, 'lxml')

print(soup.prettify())
print(type(soup.prettify()))