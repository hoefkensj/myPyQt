#!/usr/bin/env python


import sys

import lib.Create
import lib.QModules.QMain
import lib.QtApplication
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
	def Fnx():
		def Generate():
			def generate():
				for element in 	GUI['Main']['Elements']:
					GUI['Fnx']['Add'](GUI['Main']['Elements'][element]['Wgt'])
			return generate
		def Run():
			def run():
				GUI['Fnx']['Generate']()
				GUI['Show']()
				sys.exit(GUI['App']['QtApp'].exec())
			return run
		f={}
		f['Add']			=	GUI['Main']['Add']
		f['Show']			=	GUI['Main']['Mtd']['show']
		f['Generate'] = Generate()
		f['Run']			=	Run()
		return f
	def Init(GUI):
		return GUI

	GUI = lib.Create.QCreate(dict, **k)
	GUI['App'] 				= 	lib.QtApplication.QtApplication()
	GUI['Main'] 			=	 	lib.QModules.QMain.make(GUI['name'],**k)
	GUI['Fnx']				= 	Fnx()
	GUI['Elements']		=	GUI['Main']['Elements']

	GUI['Show']				=		GUI['Fnx']['Show']
	GUI['Run']				=		GUI['Fnx']['Run']
	return Init(GUI)

def make(name,**k):
	k={

		}|k|{
		'pfx'       :	'gui'							,
		'name'      :	name							,

		}
	return QGui(**k)

# pTree(d=GUI)

# pTree()
# browse(myPyQt=GUI())