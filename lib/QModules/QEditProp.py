#!/usr/bin/env python
# Auth
import lib.Create

from .. import QtWgt, gnr,QWgt
from ..QElements import QIconButton

def QEditProp(**k):

	def Elements():
		parent=w['name']

		e		= {}
		e|= gnr.Element(QtWgt.make(f'Name_{parent}',pfx='lbl',pol='F.F'))
		e|= gnr.Element(QtWgt.make(f'Field_{parent}',pfx='txtE',pol='E.F'))
		e|= gnr.Element(QtWgt.make(f'Dupl_{parent}',pfx='txtE',pol='E.F'))
		e|= gnr.Element(QtWgt.make(f'Set_{parent}',pfx='tBtn',pol='E.F', w=50, h=32))
		e|= gnr.Element(QIconButton.make(f'Edit_{parent}', bi=True))
		return e

	def Fnx(w):
		s={name.split('_')[1]:w['Elements'][name]for name in w['Elements']}

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
		s={name.split('_')[1]:w['Elements'][name]for name in w['Elements']}
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
		s={name.split('_')[1]:w['Elements'][name]for name in w['Elements']}
		s['Name']['Set']['Text'](w['name'])
		s['Set']['Set']['Hidden'](True)
		s['Set']['Set']['Text']('Set')
		s['Field']['Set']['ReadOnly'](True)
		s['Dupl']['Set']['Hidden'](True)
		w['Fnx']['Editable'](not k['ed'])

		return w

		
	w=lib.QWgt.make(k['name'],**k)
	w['Elements'] = Elements()
	w['Fnx'] 			|=	Fnx(w)
	w['Con']			=	Con()
	return Init(w)


def make(namestr,**k):
	k={
		'lbl'       :	None							,
		'ed'        :	True							,
		'margin'    :	[0,0,0,0]					,
		'pol'       :	'E.F'							,
		't'         :	'H'								,
	}	|	k	|	{
		'pfx'       :	'wgt'							,
		'name'      :	namestr							,
	}
	return QEditProp(**k)