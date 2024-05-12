from tkinter import *
import string
import random


s = list(string.ascii_lowercase)
s1 = list(string.ascii_uppercase)
s2 = list(string.digits)
s3 = list(string.punctuation)

pass_word = []

pass_word.extend(s)
pass_word.extend(s1)
pass_word.extend(s2)
pass_word.extend(s3)

random.shuffle(pass_word)

def func():
   val = entry.get()
   variable.set("The gennerated password is \n"+"".join(pass_word[0:int(val)]))
   
     
win = Tk()

variable = StringVar()

label1 = Label(text="PassWord Generator in Python",font=['Helvetica bold', 20])
label1.pack(padx=10,pady=10)


label = Label(text="Enter the length of the password you want",font=('Arial', 12))
label.pack(padx=20,pady=15)

entry = Entry(width=60,font=('Arial', 16))
entry.pack(padx=15,pady=15)

btn = Button(text="Submit",command=func)
btn.pack(padx=10,pady=10)

labe2 = Label(textvariable=variable,font=('Arial', 15))
labe2.pack(padx=10,pady=10)

win.title("Password Generator")
win.geometry("400x400")
win.mainloop()