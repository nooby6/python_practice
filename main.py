import tkinter
from tkinter import *
from turtle import clear

root=Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.resizable(True,True)
root.configure(background="black")

equation=""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation=""
    label_result.config(text=equation)

def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="Error"
            equation=""
    label_result.config(text=result)


label_result=Label(root,width=25, height=2, text="0",anchor="e",font=("Arial", 40),bg="black",fg="white")
label_result.pack()

Button(root,text="C",width=10,height=3, bd=2,bg="black",fg="white",command=lambda:clear()).place(x=10,y=100)
Button(root,text="(",width=10,height=3, bd=1,bg="black",fg="white",command=lambda:show("(")).place(x=130,y=100)
Button(root,text=")",width=10,height=3, bd=1,bg="black",fg="white",command=lambda:show(")")).place(x=250,y=100)
Button(root,text="/",width=10,height=3, bd=1,bg="black",fg="white",command=lambda:show("/")).place(x=370,y=100)

Button(root,text="7",width=10,height=3, bd=1,bg="black",fg="white",command=lambda:show("7")).place(x=10,y=180)
Button(root,text="8",width=10,height=3, bd=1,bg="black",fg="white",command=lambda:show("8")).place(x=130,y=180)
Button(root,text="9",width=10,height=3, bd=1,bg="black",fg="white",command=lambda:show("9")).place(x=250,y=180)
Button(root,text="*",width=10,height=3, bd=1,bg="black",fg="white",command=lambda:show("*")).place(x=370,y=180)

Button(root,text="4",width=10,height=3, bd=1,bg="black",fg="white",command=lambda:show("4")).place(x=10,y=260)
Button(root,text="5",width=10,height=3, bd=1,bg="black",fg="white",command=lambda:show("5")).place(x=130,y=260)
Button(root,text="6",width=10,height=3, bd=1,bg="black",fg="white",command=lambda:show("6")).place(x=250,y=260)
Button(root,text="-",width=10,height=3, bd=1,bg="black",fg="white",command=lambda:show("-")).place(x=370,y=260)

Button(root,text="1",width=10,height=3, bd=1,bg="black",fg="white",command=lambda:show("1")).place(x=10,y=340)
Button(root,text="2",width=10,height=3, bd=1,bg="black",fg="white",command=lambda:show("2")).place(x=130,y=340)
Button(root,text="3",width=10,height=3, bd=1,bg="black",fg="white",command=lambda:show("3")).place(x=250,y=340)
Button(root,text="+",width=10,height=3, bd=1,bg="black",fg="white",command=lambda:show("+")).place(x=370,y=340)

Button(root,text="0",width=10,height=3, bd=1,bg="black",fg="white",command=lambda:show("0")).place(x=10,y=420)
Button(root,text=".",width=10,height=3, bd=1,bg="black",fg="white",command=lambda:show(".")).place(x=130,y=420)
Button(root,text="^",width=10,height=3, bd=1,bg="black",fg="white",command=lambda:show("^")).place(x=370,y=420)
Button(root,text="=",width=15,height=5, bd=1,bg="orange",fg="white",command=lambda:calculate()).place(x=250,y=420)



root.mainloop()