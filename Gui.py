from tkinter import * 


class window(Tk):
    
    def __init__(self):
        super().__init__()
    
    def btn(self):
        self.btn = Button(text="Button using oops")
        self.btn.pack()
        
        
    
win = window()
win.btn()
win.geometry("500x400")
win.mainloop()
    
    