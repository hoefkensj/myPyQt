#!/usr/bin/env python


import sys

import lib.Create
import lib.QModules.QMain
from .PyQtX import QWidget,QApplication,QtVersion
from . import QWgt
from . import gnr

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





def QGui(*a,**k):

	def App():
		from sys import argv
		a = {}
		a['QtApp'] = QApplication(argv)
		a['Clip'] = a['QtApp'].clipboard()
		return a
	def Fnx():
		def Add():
			return GUI['Main']['Add']
		def Generate():
			for element in GUI['Elements']:
				wgt=GUI['Elements'].get(element)
				GUI['Main']['Add'](wgt['Wgt'])
		def Show():
			return GUI['Main']['Mtd']['show']
		def Run():
			from sys import exit
			Generate()
			GUI['Show']()
			exit(GUI['App']['QtApp'].exec())
		f={}
		f['Add']	=	Add()
		f['Generate']= Generate
		f['Show']	=	Show()
		f['Run']	=	Run
		return f
	def Init(w):
		return GUI

	GUI = {}
	GUI['App'] 				= 	App()
	GUI['Main'] 			=	 lib.QModules.QMain.make(k['pfx_name'])
	GUI['Fnx']				= 	Fnx()
	GUI['Elements']		=		{}
	GUI['Show']				=		GUI['Fnx']['Show']
	GUI['Run']				=		GUI['Fnx']['Run']
	return Init(GUI)

def make(name,**k):
	k={
		'margin'    :	[0,0,0,0]					,
		'pol'       :	'EE'							,
		't'         :	'v'								,
		}|k|{
		'pfx'       :	'wgt'							,
		'name'      :	name							,
		'pfx_name'  :	f'wgt_{name}'			,
		}
	return QGui(**k)

# pTree(d=GUI)

# pTree()
# browse(myPyQt=GUI())