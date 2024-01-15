from tkinter import *

def submit():
    #print(listbox.get(listbox.curselection()))for single selection
    food=[]
    for i in listbox.curselection():
        food.insert(i,listbox.get(i))
    for i in food:
        print(i)

def add():
    listbox.insert(listbox.size(),entey.get())
    listbox.config(height=listbox.size())

def dels():
    #listbox.delete(listbox.curselection())for single
    for i in listbox.curselection():
        listbox.delete(i)
    listbox.config(height=listbox.size())

window=Tk()

listbox=Listbox(window,
               font=("Constantia",35),
               bg='#f7ffde',
               width=12,
               selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,'pizza')
listbox.insert(2,'pizza')
listbox.insert(3,'pizza')
listbox.insert(4,'pizza')
listbox.insert(5,'pizza')

entey=Entry(window)
entey.pack(side=LEFT)

listbox.config(height=listbox.size())

submit=Button(window,text="submit",command=submit)
submit.pack(side=LEFT)

add=Button(window,text="add",command=add)
add.pack(side=LEFT)

delete=Button(window,text="del",command=dels)
delete.pack(side=LEFT)

window.mainloop()