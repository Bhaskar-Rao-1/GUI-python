from tkinter import *

count=0

def click():
    global count
    count+=1
    print(count)
    print("you clicked button")

window=Tk()
photo=PhotoImage(file='feather.png')

button=Button(window,text='Click me!',command=click,font=('Comic sans',30),fg='green',bg='black',activeforeground='green',activebackground='black',state=ACTIVE,image=photo,compound='top')
button.pack()
window.mainloop()