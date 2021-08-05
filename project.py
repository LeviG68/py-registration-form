import tkinter as Tk
from tkinter import *

root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

#heading

Label(root, text="Python Registration Form", font='ar 15 bold').grid(row=0, column=3)

# Fields names
name= Label(root, text='Name')
phone= Label(root, text='Phone')
gender= Label(root, text='Gender')
emergancy= Label(root, text='Emergancy')
paymentmood= Label(root, text='Payment Mood')


# Packing Fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergancy.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

# Vars for storing data 
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergancyvalue = StringVar
paymentmoodvalue = StringVar
checkvalue = IntVar

# Creating entry fields
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergancyentry = Entry(root, textvariable=emergancyvalue)
paymentmoodentry = Entry(root, textvariable=paymentmoodvalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergancyentry.grid(row=4, column=3)
paymentmoodentry.grid(row=5, column=3)

# Creating check box
Checkbutton = Checkbutton(text="Remember me?", variable=checkvalue)
Checkbutton.grid(row=6, column=3)

#Submit button
Button(text="Submit", command=getvals).grid(row=7, column=3 )

root.mainloop() 