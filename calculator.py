from tkinter import *
import math

win=Tk()
win.geometry('370x380+400+150')
win.title('Calculator')
win.configure(bg='grey')

entry = Entry(win,width=28,font='calibri 18',bd=5,justify=RIGHT)
entry.place(x=10,y=10,height=90)

equation=""

def show(value):
    global equation
    equation+=value
    entry.insert(END,value)

def clear():
    global equation
    equation=""
    entry.delete(0,END)

def calculate():
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    entry.delete(0,END)
    entry.insert(END, result)

btn=Button(win,text='C',font='calibri 15 bold',width=7,bd=2,bg='black',fg='red',command=clear)
btn.place(x=10,y=110)
btn=Button(win,text='(',font='calibri 15 bold',width=7,bd=2,bg='black',fg='green',command=lambda:show("("))
btn.place(x=100,y=110)
btn=Button(win,text=')',font='calibri 15 bold',width=7,bd=2,bg='black',fg='green',command=lambda:show(")"))
btn.place(x=190,y=110)
btn=Button(win,text='*',font='calibri 15 bold',width=7,bd=2,bg='black',fg='green',command=lambda:show("*"))
btn.place(x=280,y=110)
btn=Button(win,text='7',font='calibri 15 bold',width=7,bd=2,bg='black',fg='green',command=lambda:show("7"))
btn.place(x=10,y=160)
btn=Button(win,text='8',font='calibri 15 bold',width=7,bd=2,bg='black',fg='green',command=lambda:show("8"))
btn.place(x=100,y=160)
btn=Button(win,text='9',font='calibri 15 bold',width=7,bd=2,bg='black',fg='green',command=lambda:show("9"))
btn.place(x=190,y=160)
btn=Button(win,text='4',font='calibri 15 bold',width=7,bd=2,bg='black',fg='green',command=lambda:show("4"))
btn.place(x=10,y=210)
btn=Button(win,text='5',font='calibri 15 bold',width=7,bd=2,bg='black',fg='green',command=lambda:show("5"))
btn.place(x=100,y=210)
btn=Button(win,text='6',font='calibri 15 bold',width=7,bd=2,bg='black',fg='green',command=lambda:show("6"))
btn.place(x=190,y=210)
btn=Button(win,text='1',font='calibri 15 bold',width=7,bd=2,bg='black',fg='green',command=lambda:show("1"))
btn.place(x=10,y=260)
btn=Button(win,text='2',font='calibri 15 bold',width=7,bd=2,bg='black',fg='green',command=lambda:show("2"))
btn.place(x=100,y=260)
btn=Button(win,text='3',font='calibri 15 bold',width=7,bd=2,bg='black',fg='green',command=lambda:show("3"))
btn.place(x=190,y=260)
btn=Button(win,text='/',font='calibri 15 bold',width=7,bd=2,bg='black',fg='green',command=lambda:show("/"))
btn.place(x=280,y=160)
btn=Button(win,text='-',font='calibri 15 bold',width=7,bd=2,bg='black',fg='green',command=lambda:show("-"))
btn.place(x=280,y=210)
btn=Button(win,text='+',font='calibri 15 bold',width=7,bd=2,bg='black',fg='green',command=lambda:show("+"))
btn.place(x=280,y=260)
btn=Button(win,text='0',font='calibri 15 bold',width=7,bd=2,bg='black',fg='green',command=lambda:show("0"))
btn.place(x=10,y=310)
btn=Button(win,text='%',font='calibri 15 bold',width=7,bd=2,bg='black',fg='green',command=lambda:show("%"))
btn.place(x=100,y=310)
btn=Button(win,text='.',font='calibri 15 bold',width=7,bd=2,bg='black',fg='green',command=lambda:show("."))
btn.place(x=190,y=310)
btn=Button(win,text='=',font='calibri 15 bold',width=7,bd=2,bg='black',fg='red',command=lambda:calculate())
btn.place(x=280,y=310)

win.mainloop()