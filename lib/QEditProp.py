#!/usr/bin/env python
# Auth
from . import QtWgt,gnr
from . import elements
import sys
from . import QWgt
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

def QEditProp(**k):
	def Arg(a,args={}):
		d	=	{
		'pfx'   :	'mqw'				,
		'm'     :	[0,0,0,0]			,
		'hPol'  :	'P'						,
		'vPol'  :	'P'						,
		'w'     :	20						,
		'h'     :	20						,
		'bi'    :	False					,
		'icowh' :	[32,32]				,
		'lbl'   :	None					,
		}
		args = args or gnr.ArgKwargs(defaults=d,**k)

		return args(a)


	def Cfg():
		def sizing():
			c={}
			c['hpol']					=	Arg('hPol')
			c['vpol']					=	Arg('vPol')
			c['sizepolicy']		=	gnr.sizePol(h=c['hpol'], v=c['vpol'])
			c['maxw']					=	Arg('w')
			c['maxh']					= Arg('h')
			c['maxsize']			=	gnr.makeSize(c['maxw'],c['maxh'])
			c['margin']				=	Arg('m')
			return c
		c		=		{}
		c		|=	gnr.makeNames(name=n[0], pfx=Arg('pfx'))
		c		|=	sizing()
		c['qt'] = gnr.PfxMap(Arg('pfx'))
		c['checkable']		= Arg('bi')
		c['btnstyle']			=	gnr.tBtnStyles('I')
		return c


	# def elements():
	# 	e= {}
	# 	e['lbl_EditProp']		= QtWgt.make(n='lbl_EditProp')
	# 	e		|= QtWgt.make(n='txt_EditProp')#(n,ro=True)
	# 	e		|= QtWgt.make(n='txt_dupEditProp')#(n,ro=True)
	# 	e		|= QtWgt.make('tBtn_Set')
	# 	e		|= iBtn('Edit', bi=True)
	# 	return e

	def Elements():
		add=w['Fnx']['Add']
		e		= {}
		# e['lbl_EditProp']=QtWgt.make('lbl_EditProp')
		# e['txt_EditProp']	= QtWgt.make('txt_EditProp')
		# e['txt_dupEditProp']	= QtWgt.make('txt_dupEditProp')
		e|= QtWgt.make('tBtn_Set')
		e|= elements.make_iBtn('Edit', bi=True)
		for element in e:
			add(e[element])
		return e

	def build():
		elements=	w['Elements']
		for element in elements :
			w['Fnx']['Add'](elements[element])


	def init(wgt):
		# w['Elements']['lbl_EditProp']['Mtd']['setText'](Arg('lbl'))
		w['Elements']['tBtn_Set']['Mtd']['setHidden'](True)
		# w['Elements']['txt_EditProp']['Mtd']['setReadOnly'](True)
		# w['Elements']['txt_dupEditProp']['Mtd']['setHidden'](True)
		# w['Fnx']['Editable'](not k.get('ed'))
		return wgt
	def fnx(wgt):
		def txtText(wgt):
			def txtText(text):
				wgt.txt.setText(text)
				wgt.txtdup.setText(text)
			return txtText
		def setText(wgt):
			def setText():
				nText=  wgt.txt.text()
				wgt.txtdup.setText(nText)
				wgt.btnEdit.setChecked(False)
				wgt.btnSet.setHidden(True)
				fnSet(nText)
			return setText
		def edit(wgt):
			def edit(state):
				wgt.btnEdit.setChecked(state)
				wgt.txt.setReadOnly(not state)
				wgt.btnSet.setHidden(not state)
				if not state:
					wgt.txt.setText(wgt.txtdup.text())
			return edit
		def editable(wgt):
			def editable(state):
				w['Elements']['iBtn_Edit']['Mtd']['setHidden'](state)
			return editable
		f = {}
		f['Edit'] 		=	edit(wgt)
		f['txtText'] 	=	txtText(wgt)
		f['setText']	=	setText(wgt)
		f['Editable'] =	editable(wgt)
		return f
	def conn(wgt):
		c = {}
		c['iBtn_Edit']= w['Elements']['iBtn_Edit']['Mtd']['clicked'].connect
		# c['tBtn_Set']= w['Elements']['tBtn_Set']['Mtd']['clicked'].connect
		# c['txt_EditProp']	= {}
		# c['txt_EditProp']['returnPressed']= w['Elements']['txt_EditProp']['Mtd']['returnPressed'].connect
		# wgt.btnEdit.clicked.connect(w['fnx']['Edit'])
		# wgt.btnSet.clicked.connect(w['fnx']['txtText'])
		# wgt.txt.returnPressed.connect(w['fnx']['txtText'])
		return c
	w ={}


	w=	QWgt.make(Arg('name'),t='h')
	w['Elements'] = Elements()


	w['Fnx'] 			|= fnx(w['Wgt'])
	w['Conn']			=	conn(w['Wgt'])
	w['Wgt']			=	init(w['Wgt'])

	return w


def make(name,pfx='wgt',**k):
	Names=gnr.makeNames(name=name,pfx=pfx)
	kwargs={
	'pfx_name'  :	Names['pfx_name'],
	'pfx'       :	Names['pfx'],
	'name'      :	Names['name'],
		'qt'        : gnr.PfxMap(pfx),}
	qtwgt 		=	QEditProp(**kwargs,**k)
	return qtwgt