#!/usr/bin/env python
# Auth
import lib.Create
import lib.gnr
import lib.QElements.QTextButton
import lib.QElements.QIconButton
import lib.QtWgt

def QEditProp(**k):
	def Cfg():
		c={
			'ObjectName'        :		w['Name'],
			'SizePolicy'        :		lib.gnr.makeSizePolicy(k['pol']),
			'ContentsMargins'   :		k['margin'],
		}
		return c
	def Elements():
		parent=w['name']

		e		= {}
		e|= lib.gnr.Element(lib.QtWgt.make(f'Name_{parent}', pfx='lbl', pol='F.F'))
		e|= lib.gnr.Element(lib.QtWgt.make(f'Field_{parent}', pfx='txtE', pol='E.F'))
		e|= lib.gnr.Element(lib.QtWgt.make(f'Dupl_{parent}', pfx='txtE', pol='E.F'))
		e|= lib.gnr.Element(lib.QElements.QTextButton.make(f'Set_{parent}', pol='E.F', wh=[50, 32]))
		e|= lib.gnr.Element(lib.QElements.QIconButton.make(f'Edit_{parent}', bi=True))
		return e

	def Fnx(wgt):
		s={name.split('_')[1]:wgt['Elements'][name] for name in wgt['Elements']}


		def txtText():
			def txtText(text):
				s['Field']['Set']['Text'](text)
				s['Dupl']['Set']['Text'](text)
			return txtText
		def setText():
			def setText():
				nText= 	s['Field']['Set']['Text']()
				s['Dupl']['Set']['Text'](nText)
				s['Edit']['Set']['Checked'](False)
				s['Set']['Set']['Hidden'](True)
				# fnSet(nText)
			return setText
		def edit():
			def edit(state):
				s['Edit']['Set']['Checked'](state)
				s['Field']['Set']['ReadOnly'](not state)
				s['Set']['Set']['Hidden'](not state)
				if not state:
					s['Field']['Set']['Text'](s['Dupl']['Read']['Text']())
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
		f['Generate'] = lib.gnr.Generate()
		return f

	def Con(w):
		s={name.split('_')[1]:w['Elements'][name]for name in w['Elements']}
		c = {}
		c['Edit']= s['Edit']['Con']['clicked']
		c['Set']=	s['Set']['Con']['clicked']
		c['Field']	= {}
		c['Field']['returnPressed']= s['Field']['Mtd']['returnPressed'].connect

		c['Edit'](w['Fnx']['Edit'])
		c['Set'](w['Fnx']['txtText'])
		c['Field']['returnPressed'](w['Fnx']['txtText'])
		return c

	def Init(wgt):
		s={name.split('_')[1]:w['Elements'][name]for name in w['Elements']}
		s['Name']['Set']['Text'](w['name'])
		s['Set']['Set']['Hidden'](True)
		# s['Set']['Set']['Text']('Set')
		s['Field']['Set']['ReadOnly'](True)
		s['Dupl']['Set']['Hidden'](True)
		wgt['Fnx']['Editable'](not k['ed'])
		wgt['Fnx']['Generate']()
		return wgt

		
	w=lib.QWgt.make(k['name'],**k)
	w['Elements'] = Elements()
	w['Fnx'] 			|=	Fnx(w)
	w['Con']			=	Con(w)
	return Init(w)


def make(namestr,**k):
	k={
		'ed'        :	True							,
		'margin'    :	[0,0,0,0]					,
		'pol'       :	'E.F'							,
		't'         :	'H'								,
	} |	k	|	{
		'pfx'       :	'wgt'							,
		'name'      :	namestr							,
	}
	return QEditProp(**k)