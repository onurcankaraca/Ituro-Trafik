#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import pytesseract
import cv2
import numpy as np
#import RPi.GPIO as GPIO
import time

"""
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

GPIO.setup(25,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

p=GPIO.PWM(16,100)
q=GPIO.PWM(25,100)
hafıza=""

def cift_serit():
    
    if ((cx_sol >sol_rfr) and (sag_rfr>cx_sag)) or ((sol_rfr>cx_sol) and (cx_sag>sag_rfr)):
        print("düz gidecek")
        
        
        p.start(10) #Motor will run at slow speed
        q.start(10)
        GPIO.output(21,True)
        GPIO.output(20,False)
        GPIO.output(16,True)
        
        GPIO.output(23,True)
        GPIO.output(24,False)
        GPIO.output(25,True)
        

    elif (cx_sol< sol_rfr) and (cx_sag < sag_rfr):

        
        x=((sol_rfr-cx_sol)+(sag_rfr-cx_sag))/2
        print('sag motora sol motordan %d fazla pwm veriliyor.' %x)
        print('aradaki fark= %d ' %x)
                
        p.start(20) #Motor will run at slow speed
        q.start(20+x) 
        GPIO.output(21,True)
        GPIO.output(20,False)
        GPIO.output(16,True)
        
        GPIO.output(23,True)
        GPIO.output(24,False)
        GPIO.output(25,True)
        
        
        
    elif (cx_sol > sol_rfr) and ( cx_sag > sag_rfr):
        y=((cx_sol-sol_rfr)+(cx_sag-sag_rfr))/2
        print("sol motora y daha fazla pwm") 
        print('aradaki fark= %d ' %y)
                
        p.start(10+y) #Motor will run at slow speed
        q.start(10)
        GPIO.output(21,True)
        GPIO.output(20,False)
        GPIO.output(16,True)
        
        GPIO.output(23,True)
        GPIO.output(24,False)
        GPIO.output(25,True)
        
def sol_serit():
    print("yalnıza sol serit takibi")
    p.start(50) #Motor will run at slow speed
    q.start(10)
    GPIO.output(21,True)
    GPIO.output(20,False)
    GPIO.output(16,True)
    
    GPIO.output(23,True)
    GPIO.output(24,False)
    GPIO.output(25,True)
        
        
def sag_serit():
    print("yalnızca sag serit takibi")
    
    p.start(10) #Motor will run at slow speed
    q.start(50)
    GPIO.output(21,True)
    GPIO.output(20,False)
    GPIO.output(16,True)
    
    GPIO.output(23,True)
    GPIO.output(24,False)
    GPIO.output(25,True)   
    
def dur():
    print("Araç duruyor")
    #durma fonksiyonu
    
    p.start(0) #Motor will run at slow speed
    q.start(0)
    GPIO.output(21,True)
    GPIO.output(20,False)
    GPIO.output(16,True)
    
    GPIO.output(23,True)
    GPIO.output(24,False)
    GPIO.output(25,True)  
"""  

frame=cv2.imread("red.png")
    

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

resize=cv2.resize(frame,(512,512))
#-------------------------------------------------------------------
#şerit

lower_black = np.array([0, 0, 0], np.uint8)
upper_black = np.array([180, 255, 80], np.uint8) 

mask_serit = cv2.inRange(hsv, lower_black, upper_black)
mask_serit=cv2.resize(mask_serit,(512,512))
mask_sol_serit=mask_serit.copy()
mask_sag_serit=mask_serit.copy()

mask_sol_serit[0:312,0:512]=0   #(y,x)
mask_sol_serit[0:512,100:512]=0

mask_sag_serit[0:312,0:512]=0   #(y,x)
mask_sag_serit[0:512,0:412]=0


M_serit_sol = cv2.moments(mask_sol_serit)
M_serit_sag = cv2.moments(mask_sag_serit)

sol_rfr=50
sag_rfr=462

#şerit
#-------------------------------------------------------------------
#-------------------------------------------------------------------
#tabela

lower_red = np.array([0,50,50], np.uint(8)) 
upper_red = np.array([10,255,255], np.uint(8)) 
mask1 = cv2.inRange(hsv, lower_red, upper_red)


lower_red = np.array([170,50,50]) 
upper_red = np.array([180,255,255])
mask2 = cv2.inRange(hsv, lower_red, upper_red)

mask_tabela_kırmızı = mask1 + mask2

x,y,w,h = cv2.boundingRect(mask_tabela_kırmızı)
orta_nokta=frame[y:y+h, x:x+w] 
roi_ok = frame[y:y+h, x:x+w]





orta_nokta_color = orta_nokta[int(w/2),int(h/2)]


lower_black = np.array([0, 0, 0], np.uint8)
upper_black = np.array([180, 255, 80], np.uint8) 

mask_ok= cv2.inRange(roi_ok, lower_black, upper_black)
bl = (0,0,0)
wh = (255,255,255)



sag_beyaz = 0
sol_beyaz = 0

for carpan in range(1,int(w*0.375)): 
    if mask_ok[int(h*0.375),int(w/2 + carpan)] == 255:
        #cv2.circle(mask_ok, (int(w/2 + carpan), int(h*0.375)), 1, wh, 1)
        sag_beyaz = sag_beyaz+1

for carpan in range(1,int(w*0.375)): 
    if mask_ok[int(h*0.375),int(w/2 - carpan)] == 255:
        #cv2.circle(mask_ok, (int(w/2 - carpan), int(h*0.375)), 1, wh, 1)
        sol_beyaz = sol_beyaz+1


print(sag_beyaz)
print(sol_beyaz)

Hassasiyet = 5

#tabela
#-------------------------------------------------------------------
#-------------------------------------------------------------------
#park yeri

park=pytesseract.image_to_string(frame)
park_bul=park.find("")

A1='Al'
A2="A2"
B1="B1"
B2='B2'
A11=park.find(A1)
A22=park.find(A2)
B11=park.find(B1)
B22=park.find(B2)

#park yeri
#-------------------------------------------------------------------


print(park)
if (200 <= orta_nokta_color[2] <= 255) and (orta_nokta_color[0]<30) :
    print("Bu bir kirmizi isiktir.")
    #dur()
#elif park_bul>=0: 
elif A11>=0:
    print("A1 bulduuuuum")
elif A22>=0:
    print("A2 bulduuuuum")
elif B11>=0:
    print("B1 bulduuuuum")
elif B22>=0:
    print("B2 bulduuuuum")

else: # 0<=orta_nokta_color[2]<=100
    if sag_beyaz - sol_beyaz > Hassasiyet:
        print("-----------saga don tabelası")
    elif sol_beyaz - sag_beyaz > Hassasiyet:
        print("-----------sola don tabelası")
    else:
        print("-----------duz git tabelası")

        #sag_serit()

cv2.imshow("img",frame)
cv2.imshow("mask_ok", mask_ok)
#cv2.imshow("mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()