from tkinter import * 
import calendar

def discal():
    year = int(e.get())
    month = int(e1.get())
    # print(calendar.calendar(int(year)))
    l3 = Label(win,text=calendar.month(year,month),font=['Helvetica bold', 18])
    l3.pack(padx=15,pady=15)

win = Tk()

l = Label(win,text="Python Calendar",font=['Helvetica bold', 30])
l.pack()

l1 = Label(win,text="Enter The year ",font=['Helvetica bold', 20])
l1.pack(padx=10,pady=10)

e = Entry(win,width=50,font=['Helvetica bold', 15])
e.pack(padx=20,pady=10)

l2 = Label(win,text="Enter the Month",font=['Helvetica bold', 20])
l2.pack(padx=15,pady=10)

e1 = Entry(win,width=50,font=['Helvetica bold', 15])
e1.pack(padx=20,pady=10)

btn = Button(win,text="Submit",font=['Helvetica bold', 10],command=discal)
btn.pack(padx=15,pady=10)


win.title("Calendar in Python")
win.geometry("450x580")
win.mainloop()


