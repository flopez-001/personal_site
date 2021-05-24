# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:44:11 2021
web_crawl_get_urls
@author: felip
"""

from bs4 import BeautifulSoup
import requests

url = "https://www.nvcc.edu/student-services/index.html"

response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, 'html.parser')

links = soup.findAll("a")
for link in links:
    href = link.get("href")
    if href == None:
        continue