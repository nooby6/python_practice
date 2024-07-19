import tkinter
from tkinter import *

root=Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(background="black")


label_result=Label(root,width=25, height=2, text="0",anchor="e",font=("Arial", 40),bg="black",fg="white")
label_result.pack()

Button(root,text="C", width=5, font=("Arial", 20),bg="black",fg="white",borderwidth=0).pack(side=LEFT,expand=True,fill="both")

root.mainloop()