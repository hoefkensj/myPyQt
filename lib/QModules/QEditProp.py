#!/usr/bin/env python
# Auth
import lib.Create

from .. import QtWgt, gnr,QWgt
from ..QElements import QIconButton

def QEditProp(**k):
	def Create():
		w=lib.QWgt.make(k['pfx_name'])
		return w

	def Elements():
		parent=w['name']
		e		= {}
		e|= gnr.Element(QtWgt.make(f'lbl_Name_{parent}',pol='FF'))
		e|= gnr.Element(QtWgt.make(f'txt_Field_{parent}',pol='EF'))
		e|= gnr.Element(QtWgt.make(f'txt_Dupl_{parent}',pol='EF'))
		e|= gnr.Element(QtWgt.make(f'tBtn_Set_{parent}',pol='EF', w=50, h=32))
		e|= gnr.Element(QIconButton.make(f'Edit_{parent}', bi=True))
		return e

	def Fnx(w):
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
				s['Edit']['Set']['Hidden'](state)
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
		c['Edit']= s['Set']['Mtd']['clicked'].connect
		c['Set']=	s['Set']['Mtd']['clicked'].connect
		c['Field']	= {}
		c['Field']['returnPressed']= s['Field']['Mtd']['returnPressed'].connect

		c['Edit'](w['Fnx']['Edit'])
		c['Set'](w['Fnx']['txtText'])
		c['Field']['returnPressed'](w['Fnx']['txtText'])
		return c

	def Init(w):
		s=gnr.Short(w)
		s['Name']['Set']['Text'](w['name'])
		s['Set']['Set']['Hidden'](True)
		s['Set']['Set']['Text']('Set')
		s['Field']['Set']['ReadOnly'](True)
		s['Dupl']['Set']['Hidden'](True)
		w['Fnx']['Editable'](not k['ed'])
		Set=w['Set']
		Read=w['Read']
		conf = {}
		conf['ObjectName']				=	w['Name']
		conf['SizePolicy']				=	gnr.sizePol(k['pol'])
		for prop in conf:
			Set[prop](conf[prop])
			w['Cfg'][prop]=Read[prop]()
		Set['ContentsMargins'](*k['margin'])
		w['Fnx']['Generate']()
		return w

		
	w 						=		Create()
	w['Elements'] = Elements()
	w['Fnx'] 			|=	Fnx(w)
	w['Con']			=	Con()
	return Init(w)


def make(namestr,**k):
	name=lib.gnr.makeName(namestr)
	k={
		'lbl'       :	None							,
		'ed'        :	True							,
		'margin'    :	[0,0,0,0]					,
		'pol'       :	'EF'							,
		't'         :	'h'								,
		}|k|{
		'pfx'       :	'wgt'							,
		'name'      :	name							,
		'pfx_name'  :	f'wgt_{name}'			,
		}
	return QEditProp(**k)