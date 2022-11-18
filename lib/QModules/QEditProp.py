#!/usr/bin/env python
# Auth

from lib import QtWgt, gnr
from lib.QElements import QIconButton
import sys
from lib import QWgt
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
		'pfx'   :	'mqw'				,
		'm'     :	[0,0,0,0]			,
		'pol'   :	'EF'						,
		'lbl'   :	None					,
		'ed'    :	True,
		't'     :	'h',
		}
	def Create():
		w=dict()
		w['Name']			=	k['pfx_name']
		w['name']			=	k['name']
		w['Wgt']			=	QWgt.make(w['name'],gnr.ArgKwargs(defaults,**k))
		w['Mtd']			=	gnr.Mtds(w['Wgt'])
		w['Atr']			= gnr.Atrs(w['Wgt'])
		w							|= gnr.SetMtds(w)
		return w
	def Cfg():
		c=		gnr.ArgKwargs(defaults,**k)
		c|={
			'sizepolicy'    :	gnr.sizePol(c.get('pol')),
			'margin'        :	k.pop('m'),
		}
		def Optional():return {
			'maxw'          :	c.get('w'),
			'maxh'          : c.get('h'),
			'maxsize'       :	gnr.makeSize(c.get('w'),c.get('h')),
			}
		if c.get('w'):
			c|=Optional()
		return c
	def Elements():
		parent=w['Cfg']['name']
		e		= {}
		e|= QtWgt.make(f'lbl_Edit{parent}',hPol='F',vPol='F')
		e|= QtWgt.make(f'txt_Edit{parent}')
		e|= QtWgt.make(f'txt_Edit{parent}dup')
		e|= QtWgt.make(f'tBtn_Edit{parent}Set', hPol='F', vPol='F', w=50, h=32)
		e |= QIconButton.make(f'Edit{parent}', bi=True)
		return e
	def ShortMtds():
		parent=w['Cfg']['name']
		s={}
		s['lbl']=w['Elements'][f'lbl_Edit{parent}']
		s['txt']=w['Elements'][f'txt_Edit{parent}']
		s['dup']=w['Elements'][f'txt_Edit{parent}dup']
		s['set']=w['Elements'][f'tBtn_Edit{parent}Set']
		s['edt']=w['Elements'][f'iBtn_Edit{parent}']
		return s
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
		s=ShortMtds()
		s['lbl']['Set']['Text'](w['Cfg']['name'])
		s['set']['Set']['Hidden'](True)
		s['set']['Set']['Text']('Set')
		s['txt']['Set']['ReadOnly'](True)
		s['dup']['Set']['Hidden'](True)
		w['Fnx']['Editable'](not w['Cfg']['ed'])
		return w
		
	w							=		Create()
	w							|=	{'Elements' : Elements()}
	w							|=	{'Cfg' 			: Cfg()}
	w['Fnx'] 			|=	Fnx()
	w['Con']			|=	Con()
	return Init(w)


def make(name,pfx='wgt',**k):
	Names=gnr.makeNames(name=name,pfx=pfx)
	kwargs={
	'pfx_name'  :	Names['pfx_name'],
	'pfx'       :	Names['pfx'],
	'name'      :	Names['name'],
		'qt'        : gnr.PfxMap(pfx),}
	return QEditProp(**kwargs,**k)