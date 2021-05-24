# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:36:03 2021

@author: felip
"""

from bs4 import BeautifulSoup
import requests as req

resp = req.get("https://www.nvcc.edu")
soup = BeautifulSoup(resp.text, 'lxml')
    
tags = soup.find_all(["h2", "p"])
for tag in tags:
    print(" ".join(tag.text.split()))
        