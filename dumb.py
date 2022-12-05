#!/usr/bin/env python
from tkinter import *
def printcontents():
	mystring=mytxt.get()
	print(mystring)
tkgui=Tk()
mytxt = Entry(tkgui)
mybutton=Button(tkgui, text="Print",command=printcontents)
mytxt.pack()
mybutton.pack()
tkgui.mainloop()


