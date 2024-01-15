from tkinter import *

food=['pizza','hamburger','hotdog']

def order():
    if(x.get()==0):
        print("you order pizza")
    elif(x.get()==1):
        print("you ordered hamburger")
    elif(x.get()==2):
        print("you ordered hotdog")
    else:
        print("haah!")
window=Tk()

x=IntVar()

pizza=PhotoImage(file='feather.png')
hotdog=PhotoImage(file='hotdog.png')
burger=PhotoImage(file='burger.png')
foodImages=[pizza,burger,hotdog]
for i in range(len(food)):
    radio=Radiobutton(window,
                    text=food[i],
                    variable=x,#for deselect all
                    value=i,#select one
                    padx=25,
                    font=("Impact",50),
                    image=foodImages[i],
                    #indicatoron=0,width=375,eliminates circles
                    compound='left',
                    command=order)
    
    radio.pack(anchor=W)

window.mainloop()