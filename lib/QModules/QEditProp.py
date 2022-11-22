#!/usr/bin/env python
# Auth
import lib.Create

from .. import QtWgt, gnr,QWgt
from ..QElements import QIconButton

def QEditProp(**k):

	def Cfg():


	def Elements():
		parent=w['name']
		e		= {}
		e|= gnr.Element(QtWgt.make(f'lbl_Name_{parent}',pol='FF'))
		e|= gnr.Element(QtWgt.make(f'txt_Field_{parent}',pol='EF'))
		e|= gnr.Element(QtWgt.make(f'txt_Dupl_{parent}',pol='EF'))
		e|= gnr.Element(QtWgt.make(f'tBtn_Set_{parent}',pol='EF', w=50, h=32))
		e|= gnr.Element(QIconButton.make(f'Enable_{parent}', bi=True))
		return e

	def Fnx():
		s=gnr.Short(w)
		def txtText():
			def txtText(text):
				s['Field']['Set']['Text'](text)
				s['Dupl']['Set']['Text'](text)
			return txtText
		def setText():
			def setText():
				nText= 	s['txt']['Set']['Text']()
				s['Dupl']['Set']['Text'](nText)
				s['Enable']['Set']['Checked'](False)
				s['Set']['Set']['Hidden'](True)
				# fnSet(nText)
			return setText
		def edit():
			def edit(state):
				s['Enable']['Set']['Checked'](state)
				s['Field']['Set']['ReadOnly'](not state)
				s['Set']['Set']['Hidden'](not state)
				if not state:
					s['Field']['Set']['Text'](s['dup']['Read']['Text']())
			return edit
		def editable():
			def editable(state):
				s['Enable']['Set']['Hidden'](state)
			return editable
		f = {}
		f['Edit'] 		=	edit()
		f['txtText'] 	=	txtText()
		f['setText']	=	setText()
		f['Editable'] =	editable()
		return f

	def Con():
		s=gnr.Short(w)
		c = {}
		c['Enable']= s['Set']['Mtd']['clicked'].connect
		c['Set']=	s['Set']['Mtd']['clicked'].connect
		c['Field']	= {}
		c['Field']['returnPressed']= s['txt']['Mtd']['returnPressed'].connect

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

		
	w 						=		lib.Create.QtCreate(QWgt.make, **k)
	w							|=	{'Elements' : Elements()}
	w							|=	{'Cfg' 			: Cfg()}
	w['Fnx'] 			|=	Fnx()
	w['Con']			|=	Con()
	return Init(w)


def make(name,**k):
	def defaults():	return {
		'm'         :	[0,0,0,0]					,
		'pol'       :	'EF'							,
		'lbl'       :	None							,
		'ed'        :	True							,
		't'         :	'h'								,}
	k|={
		'pfx'       :	'wgt'							,
		'name'      :	f'{name}Edit'			,
		'pfx_name'  :	f'wgt_{name}Edit'	,
		}
	k|=gnr.ArgKwargs(defaults,**k)
	return QEditProp(**k)