#!/usr/bin/env python
import sys
from  PyQt5.QtWidgets import QWidget,QApplication
from wgt import  Wgt
from tree import Tree
from QtWgt import make
from iBtn import iBtn
from assets import ico

# from QtpyDictator.pyDictatorQt import browse

def App():
	from sys import argv
	
	a = {}
	a['QtApp'] = QApplication(argv)
	a['Clip'] = a['QtApp'].clipboard()
	return a

def pTree(*a, **k):
	d = k.get('d')
	indent = k.get('indent') or 0
	keys=len(d.keys())
	for key in d:
		dkey=f'\x1b[32m{d[key]}()\x1b[0m' if callable(d[key]) else str(d[key])
		keys-=1
		if isinstance(d[key], dict):
			sys.stdout.write('  ┃  ' * (indent))
			sys.stdout.write('  ┗━━ ' if keys == 0 else '  ┣━━ ')
			sys.stdout.write(f'\x1b[1;34m{str(key)}:\x1b[0m\t')
			if len(d[key]) > 10:
				sys.stdout.write(f'(+ {len(d[key])} items)' + '\n')
			else:
				sys.stdout.write('\n')
				pTree(d=d[key], indent=indent + 1)
		else:
			sys.stdout.write('  ┃  ' * (indent))
			sys.stdout.write('  ┗━━ ' if keys == 0 else '  ┣━━ ')
			sys.stdout.write(f'{str(key)}\t:\t{dkey}\n')

def Elements():
	def create(e={}):
		e|= make(n='trw_Tree')
		e|=	make(n='lbl_Test')
		e|=	make(n='txt_Key')
		e|= iBtn(n='Search',ico=ico.ico)
		return e
	e = create()
	return e

def place(**k):
	GUI=k.get('ui')
	e=k.get('e') or 'All'
	if e == 'All':
		for element in GUI['Elements']:
			GUI['Main']['Fnx']['Add'](GUI['Elements'][element])
	return GUI

def Gui():
	GUI = {}
	GUI['App'] = App()
	GUI['Main'] = Wgt(n='Qt5', t='V')
	GUI['Elements']=Elements()
	GUI=place(ui=GUI,e='All')
	GUI['Main']['Mtd']['show']()

	return GUI



GUI=Gui()
pTree(d=GUI)
sys.exit(GUI['App']['QtApp'].exec())

# pTree()
# browse(myPyQt=GUI())