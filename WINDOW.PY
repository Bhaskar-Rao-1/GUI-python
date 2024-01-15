from tkinter import *

#widgets--GUI elements: buyyons,textbox,lables,images
#window--serves as a container to hold or contain these widgets

window=Tk()
window.geometry("420x420")
window.title("PYTHON GUI")

icon=PhotoImage(file='feather.png')
window.iconphoto(True,icon)
window.config(background="#5cfcff")

window.mainloop()