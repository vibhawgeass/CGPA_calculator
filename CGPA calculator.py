import Tkinter
from Tkinter import *



top=Tkinter.Tk(className="CGPA calculator")
frame = Tkinter.Frame(top)
frame.pack()

w = Tkinter.Label(top, text="Welcome to the CGPA calculator")
w.pack()

l = Label(top, text="Enter the number of subjects")
l.pack()
e = Entry(top, bd =5)
e.pack()

N=[]
L=[]
E=[]

a=[]

def function():
      n = int(e.get())
      for i in range(n):
        L.append(Label(top,text="Enter the marks"))
        E.append(Entry(top,bd=5))
      for i in range(n):
          L[i].pack()
          E[i].pack()


def function1():
    n = int(e.get())
    for i in range(n):
        N.append(int(E[i].get()))
    for i in range(n):
        if (N[i] >= 90 and N[i] <= 100):
            a.append(10)
        if (N[i] >= 80 and N[i] < 90):
            a.append(9)
        if (N[i] >= 70 and N[i] < 80):
            a.append(8)
        if (N[i] >= 60 and N[i] < 70):
            a.append(7)
        if (N[i] >= 50 and N[i] < 60):
            a.append(6)
        if (N[i] >= 40 and N[i] < 50):
            a.append(5)
        if (N[i] >= 30 and N[i] < 40):
            a.append(4)
        if (N[i] >= 20 and N[i] < 30):
            a.append(3)
        if (N[i] >= 10 and N[i] < 20):
            a.append(2)
        if (N[i] >= 0 and N[i] < 10):
            a.append(1)
    sum = 0
    for i in range(n):
        sum = sum + a[i]

    c = sum / float(n)
    button2=Tkinter.Button(text=c)
    button2.pack()

button=Tkinter.Button(text="Enter marks for each subject",command=function)
button1=Tkinter.Button(text="Find CGPA",command=function1)
button.pack()
button1.pack()


top.mainloop()