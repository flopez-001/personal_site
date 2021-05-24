# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:39:50 2021

@author: felip
"""

import requests
url = 'https://www.nvcc.edu'

response = requests.get(url)
print(type(response.text))
print(response.text[:1000])