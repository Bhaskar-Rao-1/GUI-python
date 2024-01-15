from tkinter import *


def send():
    user=enter.get()
    print("Hello",user)

window=Tk()

enter=Entry(window,font=('Arial',20),fg='green',bg='black')
enter.pack(side=LEFT)

send=Button(window,text="send",command=send)
send.pack(side=RIGHT)

window.mainloop()