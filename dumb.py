#!/usr/bin/env python
from tkinter import *
def printcontents():
	mystring=mytxt.get()
	print(mystring)
tkgui=Tk()
mytxt = Entry(tkgui)
mybutton=Button(tkgui, text="Print",command=printcontents,height = 30, width = 30)
mytxt.pack()
mybutton.pack()
tkgui.mainloop()


