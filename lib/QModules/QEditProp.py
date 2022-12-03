#!/usr/bin/env python
# Auth
from lib.QElements import QTextButton,QIconButton
from lib.QBases import QWidget
from lib import gnr
from lib.QElements import QtWgt
from Configs import Config
from Configs import QDefaults
def QEditProp(**k):
	def Elements(wgt):
		parent=wgt['name']
		wgt['Elements'] = wgt.get('Elements') or {}
		wgt['Elements'] |= gnr.Element(QtWgt.make(f'Name_{parent}', pfx='lbl', pol='F.F', k=k))
		wgt['Elements'] |= gnr.Element(QtWgt.make(f'Field_{parent}', pfx='txtE', pol='E.F', k=k))
		wgt['Elements'] |= gnr.Element(QtWgt.make(f'Dupl_{parent}', pfx='txtE', pol='E.F', k=k))
		wgt['Elements'] |= gnr.Element(QTextButton.make(f'Set_{parent}', pol='E.F', wh=[50, 32]))
		wgt['Elements'] |= gnr.Element(QIconButton.make(f'Edit_{parent}', bi=True))
		return wgt

	def Fnx(wgt):
		s=gnr.ShortNames(wgt)
		def ReConfigure(wgt):
			for element in wgt['Elements']:
				wgt['Elements'][element]['Fnx']['ReConfigure'](element)
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
				s['Edit']['Fnx']['Set']['Hidden'](state)
			return editable
		def Init(wgt):
			def init():
				s=gnr.ShortNames(wgt)
				s['Name']['Fnx']['Set']['Text'](w['name'].split('_')[0])
				s['Set']['Fnx']['Set']['Hidden'](True)
				s['Field']['Fnx']['Set']['ReadOnly'](True)
				s['Dupl']['Fnx']['Set']['Hidden'](True)
				wgt['Fnx']['Editable'](not k['ed'])
				return wgt
			return init
		wgt=gnr.Fnx(wgt)
		wgt['Fnx']['Reconfigure'] =	ReConfigure
		wgt['Fnx']['Edit'] 			=	Edit()
		wgt['Fnx']['txtText'] 		=	TxtText()
		wgt['Fnx']['setText']		=	SetText()
		wgt['Fnx']['Editable'] 	=	Editable()
		wgt['Fnx']['Init']				=	Init(wgt)

		return wgt

	def Con(wgt):
		s=gnr.ShortNames(w)
		wgt['Con'] = wgt.get('Con') or {}
		wgt['Con']['Edit']= s['Edit']['Con']['clicked']
		wgt['Con']['Set']=	s['Set']['Con']['clicked']
		wgt['Con']['Field']	= {}
		# [print(mtd,s[mtd]) for mtd in s]
		wgt['Con']['Field']['returnPressed']= s['Field']['Fnx']['Sig']['returnPressed'].connect

		wgt['Con']['Edit'](wgt['Fnx']['Edit'])
		wgt['Con']['Set'](wgt['Fnx']['txtText'])
		wgt['Con']['Field']['returnPressed'](wgt['Fnx']['txtText'])
		return wgt
	def Init(wgt):
		wgt=gnr.minInit(wgt)
		return wgt
	w	= QWidget.make(k['name'], **k)
	w	=	Config.make(w,**k)
	w	=	Elements(w)
	w	=	Fnx(w)
	w	=	Con(w)
	return 	Init(w)


def make(namestr,**k):
	preset=	QDefaults.QEditProp
	k=Config.preset(['wgt',namestr],preset,**k)
	return QEditProp(**k)
