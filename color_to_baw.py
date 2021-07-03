# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 18:17:01 2021

@author: khilr
"""

import os
from PIL import Image
path = os.getcwd() + "/pics/"
if not os.path.exists('black_and_white'): 
    os.makedirs('black_and_white')
save_path = os.getcwd() + "/black_and_white/"
count = 1
for filename in os.listdir(path): 
    file_ = str(path) + str(filename)
    img = Image.open(file_) 
    img = img.convert("L")
    save_ = save_path + filename + ".jpg"
    img.save(save_,"JPEG")
    print(str(count) + " converted : " + str(filename))
    count += 1
print("total images converted : " + str(count))