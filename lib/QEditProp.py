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
	def defaults(): return {
		'pfx'		:	'mqw'				,
		'm'			:	[0,0,0,0]			,
		'hPol'	:	'E'						,
		'vPol'	:	'P'						,
		'lbl'		:	None					,
		'ed'		:	True,
		}
	def Cfg():
		c={
			'pfx_name'			: k.get('pfx_name'),
			'pfx'						: k.get('pfx'),
			'name'					:	k.get('name'),
			'qt'						: gnr.PfxMap(k.get('pfx')),
			'spol'					:	[k.get('hPol'),k.get('vPol')],
			'sizepolicy'		:	gnr.sizePol(k.get('hPol'), k.get('vPol')),
			'margin'				:	k.get('m'),
			'ed'						:	k.get('ed'),
		}
		def Optional():return {
			'maxw'					:	k.get('w'),
			'maxh'					: k.get('h'),
			'maxsize'				:	gnr.makeSize(k.get('w'),k.get('h')),
			}
		if k.get('w'):
			c|=Optional()
		return c

	def Elements():
		parent=w['Cfg']['name']
		e		= {}
		e|= QtWgt.make(f'lbl_Edit_{parent}',hPol='F',vPol='F')
		e|= QtWgt.make(f'txt_Edit_{parent}')
		e|= QtWgt.make(f'txt_Edit_{parent}dup')
		e|= QtWgt.make(f'tBtn_Edit_{parent}Set',hPol='F',vPol='F',w=50,h=32)
		e|= elements.make_iBtn(f'Edit_{parent}', bi=True)
		return e
	def ShortMtds():
		parent=w['Cfg']['name']
		lbl=w['Elements'][f'lbl_Edit_{parent}']['Mtd']
		txt=w['Elements'][f'txt_Edit_{parent}']['Mtd']
		dup=w['Elements'][f'txt_Edit_{parent}dup']['Mtd']
		set=w['Elements'][f'tBtn_Edit_{parent}Set']['Mtd']
		edt=w['Elements'][f'iBtn_Edit_{parent}']['Mtd']
		return lbl,txt,dup,set,edt
	def Fnx():
		lbl,txt,dup,set,edt=ShortMtds()
		def txtText():
			def txtText(text):
				txt['setText'](text)
				dup['setText'](text)
			return txtText
		def setText():
			def setText():
				nText= txt['text']()
				dup['setText'](nText)
				edt['setChecked'](False)
				set['setHidden'](True)
				fnSet(nText)
			return setText
		def edit():
			def edit(state):
				edt['setChecked'](state)
				txt['setReadOnly'](not state)
				set['setHidden'](not state)
				if not state:
					txt['setText'](dup['text']())
			return edit
		def editable():
			def editable(state):
				edt['setHidden'](state)
			return editable
		f = {}
		f['Edit'] 		=	edit()
		f['txtText'] 	=	txtText()
		f['setText']	=	setText()
		f['Editable'] =	editable()
		return f
	def Con():
		lbl,txt,dup,set,edt=ShortMtds()
		c = {}
		c['iBtn_Edit']= edt['clicked'].connect
		c['tBtn_Set']=	set['clicked'].connect
		c['txt_Edit']	= {}
		c['txt_Edit']['returnPressed']= txt['returnPressed'].connect

		c['iBtn_Edit'](w['Fnx']['Edit'])
		c['tBtn_Set'](w['Fnx']['txtText'])
		c['txt_Edit']['returnPressed'](w['Fnx']['txtText'])
		return c
	def Init(w):
		for element in w['Elements']:
			w['Fnx']['Add'](w['Elements'][element])
		lbl,txt,dup,set,edt=ShortMtds()
		lbl['setText'](w['Cfg']['name'])
		set['setHidden'](True)
		set['setText']('Set')
		txt['setReadOnly'](True)
		dup['setHidden'](True)
		w['Fnx']['Editable'](not w['Cfg']['ed'])
		return w
		
	k,Arg					=		gnr.ArgKwargs(defaults,**k)
	w							=		QWgt.make(k.get('name'),t='h',vPol='F',hPol='E')
	w['Name']			=		k.get('pfx_name')
	w							|=	{'Elements' : Elements()}
	w							|=	{'Cfg' 			: Cfg()}
	w['Fnx'] 			|=	Fnx()
	w['Con']			|=	Con()
	return Init(w)


def make(name,pfx='wgt',**k):
	Names=gnr.makeNames(name=name,pfx=pfx)
	kwargs={
	'pfx_name'	:	Names['pfx_name'],
	'pfx'				:	Names['pfx'],
	'name'			:	Names['name'],
		'qt'        : gnr.PfxMap(pfx),}
	qtwgt 		=	QEditProp(**kwargs,**k)
	return qtwgt