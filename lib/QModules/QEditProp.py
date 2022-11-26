#!/usr/bin/env python
# Auth
import lib.Create
import lib.gnr
import lib.QElements.QTextButton
import lib.QElements.QIconButton
import lib.QtWgt
import lib.QWgt

def QEditProp(**k):
	def Cfg():
		c={
			'ObjectName'        :		w['Name'],
			'SizePolicy'        :		lib.gnr.makeSizePolicy(k['pol']),
			'ContentsMargins'   :		k['margin'],
			**k
		}
		return c
	def Elements():
		parent=w['name']

		e		= {}
		e|= lib.gnr.Element(lib.QtWgt.make(f'Name_{parent}', pfx='lbl', pol='F.F',k=k))
		e|= lib.gnr.Element(lib.QtWgt.make(f'Field_{parent}', pfx='txtE', pol='E.F',k=k))
		e|= lib.gnr.Element(lib.QtWgt.make(f'Dupl_{parent}', pfx='txtE', pol='E.F',k=k))
		e|= lib.gnr.Element(lib.QElements.QTextButton.make(f'Set_{parent}', pol='E.F', wh=[50, 32]))
		e|= lib.gnr.Element(lib.QElements.QIconButton.make(f'Edit_{parent}', bi=True))
		return e

	def Fnx(wgt):
		s={name.split('_')[1]:wgt['Elements'][name] for name in wgt['Elements']}
		def TxtText():
			def txtText(text):
				s['Field']['Set']['Text'](text)
				s['Dupl']['Set']['Text'](text)
			return txtText
		def SetText():
			def setText():
				nText= 	s['Field']['Set']['Text']()
				s['Dupl']['Set']['Text'](nText)
				s['Edit']['Set']['Checked'](False)
				s['Set']['Set']['Hidden'](True)
				# fnSet(nText)
			return setText
		def Edit():
			def edit(state):
				s['Edit']['Set']['Checked'](state)
				s['Field']['Set']['ReadOnly'](not state)
				s['Set']['Set']['Hidden'](not state)
				if not state:
					s['Field']['Set']['Text'](s['Dupl']['Read']['Text']())
			return edit
		def Editable():
			def editable(state):
				s['Edit']['Set']['Hidden'](state)
			return editable
		def Init(wgt):
			def init():
				s={name.split('_')[1]:wgt['Elements'][name]for name in wgt['Elements']}
				s['Name']['Set']['Text'](w['name'].split('_')[0])
				s['Set']['Set']['Hidden'](True)
				s['Field']['Set']['ReadOnly'](True)
				s['Dupl']['Set']['Hidden'](True)
				wgt['Fnx']['Editable'](not k['ed'])
			return init
		f = {}
		f['Edit'] 			=	Edit()
		f['txtText'] 		=	TxtText()
		f['setText']		=	SetText()
		f['Editable'] 	=	Editable()
		f['Configure']	=	lib.gnr.Configure(wgt)
		f['Generate'] 	= lib.gnr.Generate(wgt)
		f['Init']				=	Init(wgt)
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
		wgt['Fnx']['Configure']()
		wgt['Fnx']['Generate']()
		wgt['Fnx']['Init']()
		return wgt

		
	w=lib.QWgt.make(k['name'],**k)
	w['Cfg']		=			Cfg()
	w['Elements'] = Elements()
	w['Fnx'] 			|=	Fnx(w)
	w['Con']			=	Con(w)
	return Init(w)


def make(namestr,**k):
	k={
		'ed' 				:	True						,
		't'					:	'H'							,
		'margin'		:	[0,0,0,0]					,
		'pol'				:	'E.F'							,
	} |	k	|	{
		'pfx'				:	'wgt'							,
		'name'			:	f'{namestr}_Edit'		,
	}
	return QEditProp(**k)