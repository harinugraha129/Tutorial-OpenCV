import numpy as np
import cv2 as cv

img = cv.imread('data/messi5.jpg')

px = img[100,100]
print( px )

# accessing only blue pixel
blue = img[100,100,0]
print( blue )

img[100,100] = [255,255,255]
print( img[100,100] )

# accessing RED value
red = img.item(10,10,2)
print(red)

# modifying RED value
img.itemset((10,10,2),100)
print(img.item(10,10,2))

# Accessing Image Properties
print("propertis :", img.shape)
print("size :", img.size)
print("datatype :", img.dtype)

# Image ROI
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

cv.imshow('result',img)
cv.waitKey(0)
cv.destroyAllWindows()