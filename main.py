import tkinter
from tkinter import *
from turtle import clear

root=Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(background="black")

equation=""

label_result=Label(root,width=25, height=2, text="0",anchor="e",font=("Arial", 40),bg="black",fg="white")
label_result.pack()

Button(root,text="C",width=11,height=3,font=("Arial", 20),bg="gray",fg="white",command=lambda: clear ()).pack(x=10,y=100)
Button(root,text="DEL",width=11,height=3,font=("Arial", 20),bg="gray",fg="white",command=lambda: delete()).pack(x=140,y=100)
Button(root,text="%",width=11,height=3,font=("Arial", 20),bg="gray",fg="white",command=lambda:press("%")).pack(x=270,y=100)
Button(root,text="/",width=11,height=3,font=("Arial", 20),bg="gray",fg="white",command=lambda:press("/")).pack(x=400,y=100)

Button(root,text="7",width=11,height=3,font=("Arial", 20),bg="gray",fg="white",command=lambda:press("7")).pack(x=10,y=180)
Button(root,text="8",width=11,height=3,font=("Arial", 20),bg="gray",fg="white",command=lambda:press("8")).pack(x=140,y=180)
Button(root,text="9",width=11,height=3,font=("Arial", 20),bg="gray",fg="white",command=lambda:press("9")).pack(x=270,y=180)
Button(root,text="*",width=11,height=3,font=("Arial", 20),bg="gray",fg="white",command=lambda:press("*")).pack(x=400,y=180)

Button(root,text="4",width=11,height=3,font=("Arial", 20),bg="gray",fg="white",command=lambda:press("4")).pack(x=10,y=260)
Button(root,text="5",width=11,height=3,font=("Arial", 20),bg="gray",fg="white",command=lambda:press("5")).pack(x=140,y=260)
Button(root,text="6",width=11,height=3,font=("Arial", 20),bg="gray",fg="white",command=lambda:press("6")).pack(x=270,y=260)
Button(root,text="-",width=11,height=3,font=("Arial", 20),bg="gray",fg="white",command=lambda:press("-")).pack(x=400,y=260)



root.mainloop()