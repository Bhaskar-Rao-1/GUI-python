from tkinter import *

window=Tk()
photo=PhotoImage(file='feather.png')

label=Label(window,
text="Hello world!",
font=('Arial',40,'bold'),
fg='green',
bg='black',
relief=RAISED,
bd=10,
padx=20,
pady=20,
image=photo,
compound='top')#bottom
#label.place(x=0,y=0)
label.pack()

window.mainloop()