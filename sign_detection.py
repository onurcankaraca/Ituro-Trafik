import cv2
import numpy as np

img = cv2.imread("duz_git.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 50, 50], np.uint8)
upper_red1 = np.array([10, 255, 255], np.uint8)
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

lower_red2 = np.array([170, 50, 50],np.uint8)
upper_red2 = np.array([180, 255, 255],np.uint8)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

mask = mask1 + mask2

x, y, w, h = cv2.boundingRect(mask)

# cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
#print(x)
#print(y)
#print(w)
#print(h)

lower_black = np.array([0, 0, 0], np.uint8)
upper_black = np.array([180, 255, 80], np.uint8)

roi_ok = img[y:y+h, x:x+w]
mask_ok= cv2.inRange(roi_ok, lower_black, upper_black)

bl = (0,0,0)
wh = (255,255,255)

#cv2.circle(mask_ok, (int(w*0.5),int(h*0.375)), 1, wh, 2)

sag_beyaz = 0
sol_beyaz = 0

for carpan in range(1,int(w*0.375)): #sağdaki beyaz noktaların sayısı
    if mask_ok[int(h*0.375),int(w/2 + carpan)] == 255:
        #cv2.circle(mask_ok, (int(w/2 + carpan), int(h*0.375)), 1, wh, 1)
        sag_beyaz = sag_beyaz+1

for carpan in range(1,int(w*0.375)): #soldaki beyaz noktaların sayısı
    if mask_ok[int(h*0.375),int(w/2 - carpan)] == 255:
        #cv2.circle(mask_ok, (int(w/2 - carpan), int(h*0.375)), 1, wh, 1)
        sol_beyaz = sol_beyaz+1


print(sag_beyaz)
print(sol_beyaz)

Hassasiyet = 5

if sag_beyaz - sol_beyaz > Hassasiyet:
    print("-----------saga don tabelası")
elif sol_beyaz - sag_beyaz > Hassasiyet:
    print("-----------sola don tabelası")
else:
    print("-----------duz git tabelası")

cv2.imshow("img",img)
cv2.imshow("mask_ok", mask_ok)
cv2.imshow("mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()

