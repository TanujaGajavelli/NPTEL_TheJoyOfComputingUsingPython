from PIL import Image
import numpy as np
import random
im=Image.open("test1.png")
rgb_im=im.convert("RGB")
count_in=0
count_pun=0
count=0
while(count<=100000):
    x=random.randint(0,449)
    y=random.randint(0,533)
    z=0
    r,g,b=rgb_im.getpixel((x,y))
    if(r==60):
        count_in+=1
        count+=1
    elif(r==80):
        count_pun+=1
        count+=1
area_pun=(count_pun/count_in)*3287263
print(area_pun)