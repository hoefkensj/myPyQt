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





def QGui(*a,**k):

	def App():
		from sys import argv
		a = {}
		a['QtApp'] = QApplication(argv)
		a['Clip'] = a['QtApp'].clipboard()
		return a
	def Cfg():
		g={
			'QtVersion'					:		k.pop('qtversion'),
			'ContentsMargins'		:		k['margin'],
		}
		QtConf={
			'ObjectName'        :		k['name'],
			'SizePolicy'        :		gnr.sizePol(k['pol']),
		}

		c={
			'Config'	: k,
			'General' : g,
			'QtConf' : QtConf,
		}
		return c

	def Fnx():
		def Add():
			return GUI['Main']['Add']
		def Generate():
			for element in GUI['Elements']:
				wgt=GUI['Elements'].get(element)
				GUI['Add'](wgt)
		def Show():
			return GUI['Main']['Mtd']['show']
		def Run():
			from sys import exit
			GUI['Generate']()
			GUI['Show']()
			exit(GUI['App']['QtApp'].exec())
		f={}
		f['Add']	=	Add()
		f['Generate']= Generate
		f['Show']	=	Show()
		f['Run']	=	Run
		return f
	def Init(w)     :
		Set=	GUI['Main']['Set']
		Read=	GUI['Main']['Read']
		conf = {}
		conf['ObjectName']				=		GUI['Main']['Name']
		conf['SizePolicy']				=		GUI['Main']['Cfg']['sizepolicy']
		for prop in conf:
			Set[prop](conf[prop])
			GUI['Main']['Cfg'][prop]=Read[prop]()
		Set['ContentsMargins'](*	GUI['Main']['Cfg']['margin'])
		return GUI

	GUI = {}
	GUI['App'] 				= 	App()
	GUI['Main']				=		gnr.QtCreate(QWgt.make,**k)
	GUI								|=	{'Elements': {}}
	GUI								|=	{'Cfg' 			: Cfg()}
	GUI['Fnx']				=	Fnx()
	# GUI['Con']				|=	Con()
	GUI['Add']				=		GUI['Fnx']['Add']
	GUI['Generate']		=		GUI['Fnx']['Generate']
	GUI['Show']				=		GUI['Fnx']['Show']
	GUI['Run']				=		GUI['Fnx']['Run']
	return Init(GUI)

def make(n,**k):
	def defaults(): return{
		'margin'		: [0, 0, 0, 0],
		't'		: 'v',
		'pol': 'EE'}
	kwargs={
	'qt'        : gnr.PfxMap('wgt'),
	'qtversion'	: QtVersion,}
	k|=gnr.ArgKwargs(defaults,**k)
	k|=gnr.makeNames(name=n,pfx='wgt')
	k|=kwargs
	return QGui(**k)

# pTree(d=GUI)

# pTree()
# browse(myPyQt=GUI())