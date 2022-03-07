#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from PIL import Image
import PIL
import cv2

onur=cv2.imread("adsız.png")

x= onur[10, 10]

if 230 <= x[2] <= 255 :
    print("onur")
else:
    print("hata")
print(x)


#cap=cv2.VideoCapture(0)

# while True:
    
#     ret,frame=cap.read()
#     x= (frame[10, 10])
#     #print (b)
#     #print (g)
#     #print (r)
#     if x[1]==255:
#         print("onur")
#     else:
#         print("hata")
#     print(x)
cv2.imshow("aaaaaaaaaaa",x)
    
    
cv2.waitKey(0)
cv2.destroyAllWindows()