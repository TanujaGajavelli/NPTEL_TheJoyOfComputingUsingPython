import numpy as np
from PIL import Image

width=5
height=4
array=np.zeros([height,width,3],dtype=np.uint8)  #3 represents bytes for RGB  uint-unsigned int
img=Image.fromarray(array)
img.save('test.png')
array1=np.zeros([100,200,3],dtype=np.uint8)
array1[:,:100]=[255,128,0] #Orange
array1[:,100:]=[0,0,255] #Blue
img=Image.fromarray(array1)
img.save('test.png')

im=Image.open('test.png')
rgb_im=im.convert('RGB')
r,g,b=rgb_im.getpixel((100,1))
print(r,g,b)