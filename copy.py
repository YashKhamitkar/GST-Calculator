from ast import Break
from calendar import Calendar
import tkinter as tk
from num2words import num2words

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
final=[]
def slabwiseGST(slab):
    cal=price[0]*slab/100
    CGST = cal/2
    total=price[0]+cal
    final.append(total)
    print("CGST:-",CGST,"SGST:-",CGST)
    print("Total GST is ",cal)
    print("Total price is: ",total)
    print("In Word:-",num2words(final[0]))
    

price=[]

try:
    Num1=float(input("Enter the First value:-     "))
    Num2=float(input("Enter the Second value:-     "))




    if (Num1!=None and Num2!=None):
        print("Select an operation to perform:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        try:
            GET=int(input("         "))
        except ValueError as v:
            print("       Error:-  Invalid The Input. Please Enter the String data.") 
            
        
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
            print("Entered the wrong operation value")
            Break
        if(GET==1 or GET==4 or GET==3 or GET==4):
            try:
                slab=int(input("Select the GST slab 1- 5%, 2- 12%, 3- 18%, 4- 28%         "))
                if slab==1:
                    slabwiseGST(5)
                elif slab==2:
                    slabwiseGST(12)
                elif slab==3:
                    slabwiseGST(18)
                elif slab==4:
                    slabwiseGST(28)
                else:
                    print("Entered the wrong GST value")
                        
            except ValueError as v:
                print("       Error:-  Invalid The Input. Please Enter the int data.") 
        # else:
        #     print("Entered the wrong operation value")

except ValueError as v:
    print("       Error:-  Invalid The Input. Please Enter the numarical value.") 

print()