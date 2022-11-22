#!/usr/bin/env python
# Auth

from .. import QtWgt, gnr,QWgt
from ..QElements import QIconButton
import sys
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

	def Cfg():
		c= k

		c|={
			'sizepolicy'		:	gnr.sizePol(c.get('pol')),
			'margin'				:	c.pop('m'),
		}
		def Optional():return {
			'maxw'					:	c.get('w'),
			'maxh'					: c.get('h'),
			'maxsize'				:	gnr.makeSize(c.get('w'),c.get('h')),
			}
		if c.get('w'):
			c|=Optional()
		return c
	def Elements():
		parent=w['name']

		e		= {}
		e|= gnr.Element(QtWgt.make(f'lbl_Edit{parent}',pol='FF'))
		e|= gnr.Element(QtWgt.make(f'txt_Edit{parent}',pol='EF'))
		e|= gnr.Element(QtWgt.make(f'txt_Edit{parent}dup',pol='EF'))
		e|= gnr.Element(QtWgt.make(f'tBtn_Edit{parent}Set',pol='EF', w=50, h=32))
		e|= gnr.Element(QIconButton.make(f'Edit_{parent}', bi=True))
		return e
	def Short():
		parent=w['name']
		s={}
		s['lbl']=w['Elements'][f'lbl_Edit{parent}']
		s['txt']=w['Elements'][f'txt_Edit{parent}']
		s['dup']=w['Elements'][f'txt_Edit{parent}dup']
		s['set']=w['Elements'][f'tBtn_Edit{parent}Set']
		s['edt']=w['Elements'][f'Edit_{parent}']
		return s
	def Fnx():
		s=Short()
		def txtText():
			def txtText(text):
				s['txt']['Set']['Text'](text)
				s['dup']['Set']['Text'](text)
			return txtText
		def setText():
			def setText():
				nText= 	s['txt']['Set']['Text']()
				s['dup']['Set']['Text'](nText)
				s['edt']['Set']['Checked'](False)
				s['set']['Set']['Hidden'](True)
				# fnSet(nText)
			return setText
		def edit():
			def edit(state):
				s['edt']['Set']['Checked'](state)
				s['txt']['Set']['ReadOnly'](not state)
				s['set']['Set']['Hidden'](not state)
				if not state:
					s['txt']['Set']['Text'](s['dup']['Read']['Text']())
			return edit
		def editable():
			def editable(state):
				s['edt']['Set']['Hidden'](state)
			return editable
		f = {}
		f['Edit'] 		=	edit()
		f['txtText'] 	=	txtText()
		f['setText']	=	setText()
		f['Editable'] =	editable()
		return f
	def Con():
		s=Short()
		c = {}
		c['iBtn_Edit']= s['edt']['Mtd']['clicked'].connect
		c['tBtn_Set']=	s['set']['Mtd']['clicked'].connect
		c['txt_Edit']	= {}
		c['txt_Edit']['returnPressed']= s['txt']['Mtd']['returnPressed'].connect

		c['iBtn_Edit'](w['Fnx']['Edit'])
		c['tBtn_Set'](w['Fnx']['txtText'])
		c['txt_Edit']['returnPressed'](w['Fnx']['txtText'])
		return c
	def Init(w):
		for element in w['Elements']:
			w['Fnx']['Add'](w['Elements'][element])
		s=Short()
		s['lbl']['Set']['Text'](w['name'])
		s['set']['Set']['Hidden'](True)
		s['set']['Set']['Text']('Set')
		s['txt']['Set']['ReadOnly'](True)
		s['dup']['Set']['Hidden'](True)
		w['Fnx']['Editable'](not w['Cfg']['ed'])
		Set=w['Set']
		Read=w['Read']
		conf = {}
		conf['ObjectName']				=	w['Name']
		conf['SizePolicy']				=	w['Cfg']['sizepolicy']
		for prop in conf:
			Set[prop](conf[prop])
			w['Cfg'][prop]=Read[prop]()
		Set['ContentsMargins'](*w['Cfg']['margin'])
		return w

		
	w 						=		gnr.QtCreate(QWgt.make,**k)
	w							|=	{'Elements' : Elements()}
	w							|=	{'Cfg' 			: Cfg()}
	w['Fnx'] 			|=	Fnx()
	w['Con']			|=	Con()
	return Init(w)


def make(name,**k):
	def defaults():return {
		'pfx'		:	'mqw'				,
		'm'			:	[0,0,0,0]			,
		'pol'		:	'EF'						,
		'lbl'		:	None					,
		'ed'		:	True,
		't'			:	'h',
		'pfx'		:	'wgt'
		}
	k|=gnr.ArgKwargs(defaults,**k)
	k|=gnr.makeNames(**k)
	return QEditProp(**k)