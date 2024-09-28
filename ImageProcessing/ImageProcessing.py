from PIL import Image
#Flipping Image1.png
img=Image.open('Image1.png')
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)
transposed_img.save('corrected.png')
print("Done Flipping")

#Image enhancement for Image2.png
import cv2
img=cv2.imread('Image2.png')
clahe=cv2.createCLAHE()
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
enh_img=clahe.apply(gray_img)
cv2.imwrite('enhanced.png',enh_img)
print("Done enhancing")