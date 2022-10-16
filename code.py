from ast import Break
from calendar import Calendar
import tkinter as tk

while True:
    try:
        print("Select an operation to perform:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        GET=int(input("         "))
        if GET==1 or GET==2 or GET==3 or GET==4:
            break
    except ValueError as v:
        print("       Error:-  Invalid The Input. Please Enter the String data.") 
    else:
        break
    try:
        Num1=float(input("Enter the First value:-     "))
    except ValueError as v:               
        print("       Error:-  Invalid The Input. Please Enter the String data.") 
    else:
        break
    try:
        Num2=float(input("Enter the Second value:-     "))
    except ValueError as v:               
        print("       Error:-  Invalid The Input. Please Enter the String data.") 
    else:
        break
    

while True:
        if GET==1 or GET==2 or GET==3 or GET==4:
            break
        else:
            print("Error:- Enter the correct value")
            break

# while True:
#     try:
#         Num1=float(input("Enter the First value:-     "))
#     except ValueError as v:               
#         print("       Error:-  Invalid The Input. Please Enter the String data.") 
#     else:
#         break
# while True:
#     try:
#         Num2=float(input("Enter the Second value:-     "))
#     except ValueError as v:               
#         print("       Error:-  Invalid The Input. Please Enter the String data.") 
#     else:
#         break
    
              

def Addition():
    C=Num1+Num2
    return C

def Subtraction():
    C=Num1-Num2
    return C

def Multiplication():
    C=Num1*Num2
    return C

def Division():
    C=Num1/Num2
    return C

price=[]
if GET==1:
    print(      Addition())
    price.append(Addition())
elif GET==2:
    print(      Subtraction())
    price.append(Subtraction())
elif GET==3:
    print(      Multiplication())
    price.append(Multiplication())
elif GET==4:
    print(      Division())
    price.append(Division())
else:
    print("Error")

while True:
    try:
        GST=int(input("Select the GST slab 1- 5%, 2- 12%, 3- 18%, 4- 28%         "))
    except ValueError as v:
        print("       Error:-  Invalid The Input. Please Enter the String data.") 
    else:
        break

while True:
        if GST==1:
            cal=price[0]*5/100
            CGST = cal/2
            total=price[0]+cal
            print("CGST:-",CGST,"SGST:-",CGST)
            print("Total GST is ",cal)
            print("Total price is: ",total)
            Break
        if GST==2:
            cal=price[0]*12/100
            CGST = cal/2
            total=price[0]+cal
            print("CGST:-",CGST,"SGST:-",CGST)
            print("Total GST is ",cal)
            print("Total price is: ",total)
            Break
        if GST==3:
            cal=price[0]*18/100
            CGST = cal/2
            total=price[0]+cal
            print("CGST:-",CGST,"SGST:-",CGST)
            print("Total GST is ",cal)
            print("Total price is: ",total)
            Break
        if GST==4:
            cal=price[0]*28/100
            CGST = cal/2
            total=price[0]+cal
            print("CGST:-",CGST,"SGST:-",CGST)
            print("Total GST is ",cal)
            print("Total price is: ",total)
            break
        else:
            print("Error:- Enter the correct value")
            break
