from tkinter import *

def submit():
    value=scale.get()
    print("submit",value)
window =Tk()
hot=PhotoImage(file='hot.png')
hotlabel=Label(image=hot)
hotlabel.pack()



scale=Scale(window,
           from_=100,
           to=0,
           length=600,#length
           #orient=HORIZONTAL,#show horizontally
           font=('Consolas',20),
         tickinterval = 10,
         #showvalue=0, #hide current value
         resolution=5,#show the 5,10,15....
         troughcolor='#69FAFF',
         fg='#FF1C00',
         bg='#111111'
           )#from has '_' & from value from where to point then to is to upto value

scale.set(((scale['from']-scale['to'])/2)+scale['to'])#sets value
scale.pack()

cold=PhotoImage(file='winte.png')
coldlabel=Label(image=cold)
coldlabel.pack()

button=Button(window,text="submit",command=submit)
button.pack()

window.mainloop()