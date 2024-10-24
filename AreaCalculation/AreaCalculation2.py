import imageio
import scipy.misc
import imageio
from PIL import Image
import numpy as np
import random
img = Image.open('test1.png')
img = np.array(img)
count_punjab=0
count_india=0
count=0
height, width, _ = img.shape
while(count<=1000000):
    y=random.randint(0,width-1)
    x=random.randint(0,height-1)
    z=0
    if(img[x][y][z]==60):
        count_india+=1
        count+=1
    elif(img[x][y][z]==80):
        count_punjab+=1
        count+=1
area_punjab=(count_punjab/count_india)*3287263
print(area_punjab)