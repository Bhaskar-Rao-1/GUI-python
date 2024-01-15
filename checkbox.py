from tkinter import *

def display():
    if(x.get()==1):#no need 1 if Boolean taken#if StrVar() then =="YES" need to check
        print("you agreed!")
    else:
        print("You don't agreed!")
window=Tk()
x=IntVar()#BooleanVar()#StrVar()

photo=PhotoImage(file='feather.png')

check=Checkbutton(window,
text='i agree!',
variable=x,
onvalue=1,#true then intvat to BooleanVar()--line 9#YES & No is in strVar
offvalue=0,
command=display,
fg='green',
bg='black',
padx=25,
pady=25,
image=photo,
compound='left',
activebackground='black',
activeforeground='green'
)
check.pack()

window.mainloop()