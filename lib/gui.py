#!/usr/bin/env python


import sys
from .PyQtX import QWidget,QApplication
from .wgt import  Wgt


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





def Gui():
	def App():
		from sys import argv
		a = {}
		a['QtApp'] = QApplication(argv)
		a['Clip'] = a['QtApp'].clipboard()
		return a

	def Elements():
		return {}

	def Fnx():
		def Add(e):
			GUI['Main']['Fnx']['Add'](e.pop(list(e.keys())[0]))
		def Show():
			GUI['Main']['Mtd']['show']()
		def Init():
			for element in GUI['Elements']:
				GUI['Main']['Fnx']['Add'](GUI['Elements'][element])
			GUI['FNX']['Show']()
		def Run():
			from sys import exit
			GUI['FNX']['Init']()
			exit(GUI['App']['QtApp'].exec())
		f={}
		f['Add']	=	Add
		f['Show']	=	Show
		f['Init']	=	Init
		f['Run']	=	Run
		return f

	GUI = {}
	GUI['App'] = App()
	GUI['Main'] = Wgt(n='wgt_Qt5', t='V')
	GUI['Elements']= {}
	GUI['FNX']=Fnx()
	GUI['Run']=GUI['FNX']['Run']
	return GUI




# pTree(d=GUI)


# pTree()
# browse(myPyQt=GUI())