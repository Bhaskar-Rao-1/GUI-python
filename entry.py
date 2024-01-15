from tkinter import *


def sub():
    user=entry.get()
    print("hello",user)
    #entry.config(state=DISABLED)

def dels():
    entry.delete(0,END)

def Bspace():
    entry.delete(len(entry.get())-1,END)

window=Tk()

entry=Entry(window,
         font=('Arial',20))
##entry.insert(0,"name:")
#entry.show="*"
submit=Button(window,text="submit",command=sub)
submit.pack(side=RIGHT)

delete=Button(window,text='delete!',command=dels)
delete.pack(side=RIGHT)

space=Button(window,text="space",command=Bspace)
space.pack(side=RIGHT)

entry.pack(side=LEFT)

window.mainloop()