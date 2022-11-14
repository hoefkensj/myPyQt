#!/usr/bin/env python


import sys
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





def Gui(*a,**k):
	def Arg(a,args={}):
		d= {
				'm'   : [0, 0, 0, 0],
				't'   : None,
				'hPol': 'E',
				'vPol': 'E',
				}
		args = args or gnr.ArgKwargs(defaults=d, **k)
		return args(a)

	def Cfg():
		c={}
		c['AppName']			= Arg('name')
		c['QtName']				=	Arg('pfx_name')
		c['QtVersion']		= Arg('Qt')
		c['hpol']					=	Arg('hPol')
		c['vpol']					=	Arg('vPol')
		c['sizepolicy']		=	gnr.sizePol(h=c['hpol']	, v=c['vpol']	)
		c['layouttype']		=	Arg('t')
		c['layout_name']	=	gnr.Layouts(Arg('t')),
		c['margin']				=	Arg('m')
		return c

	def App():
		from sys import argv
		a = {}
		a['QtApp'] = QApplication(argv)
		a['Clip'] = a['QtApp'].clipboard()
		return a

	def Fnx():
		def Init():
			# for element in GUI['Elements']:
			# 	wgt=GUI['Elements'].get(element)
			# 	f['Add'](wgt)
			f['Show']()
		def Run():
			f['Init']()
			from sys import exit
			exit(GUI['App']['QtApp'].exec())
		f={}
		f['Add']	=	GUI['Main']['Fnx']['Add']
		f['Show']	=	GUI['Main']['Mtd']['show']
		f['Init']	=	Init
		f['Run']	=	Run
		return f

	GUI = {}
	GUI['App'] = App()
	GUI['Main']= QWgt.make('Main', t='v')
	GUI['Elements']= GUI['Main']['Fnx']['Add']
	GUI['Fnx']=Fnx()
	GUI['Run']=GUI['Fnx']['Run']
	return GUI

def make(*a,**k):
	pfx=f'Qt{QtVersion}'
	Names=gnr.makeNames(name=[a][0], pfx=pfx)
	kwargs={
	'pfx_name'  :	Names['pfx_name'],
	'pfx'       :	Names['pfx'],
	'name'      :	Names['name'],}
	return Gui(**kwargs, **k)

# pTree(d=GUI)


# pTree()
# browse(myPyQt=GUI())