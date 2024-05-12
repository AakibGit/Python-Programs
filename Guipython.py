from tkinter import *

def func():
    value = entry.get()
    print(value)

window = Tk()
label = Label(window,text="GUI IN PYTHON",font=('Arial',20,'bold'))
entry = Entry(window)
btn = Button(window,text="Click",command=func)
# text = Text(window,padx=5,pady=10)
# can = Canvas(window,height=50,width=50)

entry.pack()
label.pack()
btn.pack()
# text.pack()
# can.pack()

window.title("Python Gui")
window.geometry("300x300")
window.mainloop()