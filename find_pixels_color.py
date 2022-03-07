#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from PIL import Image
import PIL
import cv2

img=cv2.imread("adsız.png")

x= img[10, 10]

if 230 <= x[2] <= 255 :
    print("it's red")
else:
    print("error")
print(x)

cv2.imshow("x",x)
    
cv2.waitKey(0)
cv2.destroyAllWindows()