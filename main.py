import tkinter
from tkinter import *
from turtle import clear

root=Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(background="black")

equation=""

def press(num):
    global equation
    equation=equation+str(num)
    label_result.config(text=equation)

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation=""
    label_result.config(text=equation)

label_result=Label(root,width=25, height=2, text="0",anchor="e",font=("Arial", 40),bg="black",fg="white")
label_result.pack()

Button(root,text="C",width=10,height=3, bg="black",fg="white",command=lambda:clear()).pack(x=10,y=100)
Button(root,text="(",width=10,height=3, bg="black",fg="white",command=lambda:press("(")).pack(x=120,y=100)
Button(root,text=")",width=10,height=3, bg="black",fg="white",command=lambda:press(")")).pack(x=230,y=100)
Button(root,text="/",width=10,height=3, bg="black",fg="white",command=lambda:press("/")).pack(x=340,y=100)

Button(root,text="7",width=10,height=3, bg="black",fg="white",command=lambda:press(7)).pack(x=10,y=160)
Button(root,text="8",width=10,height=3, bg="black",fg="white",command=lambda:press(8)).pack(x=120,y=160)
Button(root,text="9",width=10,height=3, bg="black",fg="white",command=lambda:press(9)).pack(x=230,y=160)
Button(root,text="*",width=10,height=3, bg="black",fg="white",command=lambda:press("*")).pack(x=340,y=160)

Button(root,text="4",width=10,height=3, bg="black",fg="white",command=lambda:press(4)).pack(x=10,y=220)
Button(root,text="5",width=10,height=3, bg="black",fg="white",command=lambda:press(5)).pack(x=120,y=220)
Button(root,text="6",width=10,height=3, bg="black",fg="white",command=lambda:press(6)).pack(x=230,y=220)
Button(root,text="-",width=10,height=3, bg="black",fg="white",command=lambda:press("-")).pack(x=340,y=220)

Button(root,text="1",width=10,height=3, bg="black",fg="white",command=lambda:press(1)).pack(x=10,y=280)
Button(root,text="2",width=10,height=3, bg="black",fg="white",command=lambda:press(2)).pack(x=120,y=280)
Button(root,text="3",width=10,height=3, bg="black",fg="white",command=lambda:press(3)).pack(x=230,y=280)
Button(root,text="+",width=10,height=3, bg="black",fg="white",command=lambda:press("+")).pack(x=340,y=280)

Button(root,text="0",width=10,height=3, bg="black",fg="white",command=lambda:press(0)).pack(x=10,y=340)
Button(root,text=".",width=10,height=3, bg="black",fg="white",command=lambda:press(".")).pack(x=120,y=340)
Button(root,text="=",width=10,height=3, bg="black",fg="white",command=lambda:press("=")).pack(x=230,y=340)


root.mainloop()