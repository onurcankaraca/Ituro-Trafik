#importing modules
import pytesseract


park=pytesseract.image_to_string('turn_right.png')
print(park)

A1='Al'
A2="A2"
B1="B1"
B2='B2'

onur=park.find("")

A11=park.find(A1)
A22=park.find(A2)
B11=park.find(B1)
B22=park.find(B2)

if onur >=0:
    if A11>=0:
        print("A1 bulduuuuum")
    elif A22>=0:
        print("A2 bulduuuuum")
    elif B11>=0:
        print("B1 bulduuuuum")
    elif B22>=0:
        print("B2 bulduuuuum")
