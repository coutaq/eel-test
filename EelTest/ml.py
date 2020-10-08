import numpy as np 
import matplotlib.pyplot as plt 
import os 
import cv2
import random
import eel
from pathlib import Path

DATADIR = Path("data/uppercase")
CATEGORIES = ['00', '01'] 
print(DATADIR)
eel.init('web', allowed_extensions=['.js', '.html'])
print("web")
DATADIR1 = Path("data/uppercase/00/1.jpg")
print(DATADIR1)
eel.loadImage(DATADIR1)

for category in CATEGORIES:
    path = os.path.join(DATADIR, category)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img));
        print(img)

print("main")
eel.start("main.html")






        

