import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

GPIO.setup(25,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

p=GPIO.PWM(16,100)
q=GPIO.PWM(25,100)

while True:
    p.start(20) #Motor will run at slow speed
    q.start(20)
    GPIO.output(21,True)
    GPIO.output(20,False)
    GPIO.output(16,True)
    
    GPIO.output(23,True)
    GPIO.output(24,False)
    GPIO.output(25,True)
    
    time.sleep(3)
    p.ChangeDutyCycle(100) #Motor will run at High speed
    q.ChangeDutyCycle(100)
    
    GPIO.output(21,True)
    GPIO.output(20,False)
    GPIO.output(16,True)

    GPIO.output(23,True)
    GPIO.output(24,False)
    GPIO.output(25,True)

    time.sleep(3)
    GPIO.output(16,False)
    GPIO.output(25,False)

    p.stop()
    q.stop()