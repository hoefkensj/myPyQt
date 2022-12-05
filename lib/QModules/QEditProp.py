#!/usr/bin/env python
# Auth
from lib.QElements import QTextButton,QIconButton,QLineEdit
from lib.QBases import QWidget
from lib import gnr
from lib.QElements import QtWgt
from Configs import Config,QDefaults
def QEditProp(**k):


	def Elements(wgt):
		es=[
		QtWgt.make('Name', pfx='lbl', pol='F.F', k=k),
		QLineEdit.make('Field',ro=1, k=k),
		QLineEdit.make('Dupl', k=k),
		QTextButton.make('Set', pol='F.F',k=k),
		QIconButton.make('Edit', bi=1,k=k)]
		for e in es:
			wgt['Elements'] |= gnr.Element(e)
		return wgt
		
	def Fnx(wgt):
		sfn_set=gnr.Short(wgt,'Fnx','Set')
		sfn_get=gnr.Short(wgt,'Fnx','Get')
		def TxtText():
			def txtText(text):
				sfn_set['Field']['Text'](text)
				sfn_set['Dupl']['Text'](text)
			return txtText
		def SetText():
			def setText():
				nText= 	sfn_get['Field']['Text']()
				sfn_set['Dupl']['Text'](nText)
				sfn_set['Edit']['Checked'](False)
				sfn_set['Set']['Hidden'](True)
				print(nText)
			return setText
		def Edit():
			def edit(state):
				sfn_set['Edit']['Checked'](state)
				sfn_set['Field']['ReadOnly'](not state)
				sfn_set['Set']['Hidden'](not state)
				if not state:
					sfn_set['Field']['Text'](str(sfn_get['Dupl']['Text']()))
			return edit
		def Editable():
			def editable(state):
				sfn_set['Edit']['Hidden'](state)
			return editable
		def Init(wgt):
			def init():
				sfn_set['Name']['Text'](w['name'].split('_')[0])
				sfn_set['Set']['Hidden'](True)
				sfn_set['Field']['ReadOnly'](True)
				sfn_set['Dupl']['Hidden'](True)
				wgt['Fnx']['Editable'](not k['ed'])
				return Internals(wgt)
			return init
		wgt=gnr.Fnx(wgt)
		wgt['Fnx']['Edit'] 			=	Edit()
		wgt['Fnx']['txtText'] 	=	TxtText()
		wgt['Fnx']['setText']		=	SetText()
		wgt['Fnx']['Editable'] 	=	Editable()
		wgt['Fnx']['Init']			=	Init(wgt)
		return wgt
	def Internals(wgt):
		wgt['Con']['Edit'](wgt['Fnx']['Edit'])
		wgt['Con']['Set'](wgt['Fnx']['setText'])
		wgt['Con']['Field']['returnPressed'](wgt['Fnx']['setText'])
		return wgt
	def Con(wgt):
		sCon=gnr.Short(wgt,'Con')
		sSig=gnr.Short(wgt,'Fnx','Sig')
		wgt['Con'] = wgt.get('Con') or {}
		wgt['Con']['Edit']= sCon['Edit']['clicked']
		wgt['Con']['Set']=	sCon['Set']['clicked']
		wgt['Con']['Field']	= {}
		wgt['Con']['Field']['returnPressed']= sSig['Field']['returnPressed'].connect
		return wgt
	def Init(wgt):
		wgt=gnr.minInit(wgt)
		return wgt
	w	= QWidget.make(k['name'], **k)
	w	=	Elements(w)
	w	=	Fnx(w)
	w	=	Con(w)
	return 	Init(w)


def make(namestr,**k):
	preset=	QDefaults.QEditProp
	k=Config.preset(['wgt',namestr],preset,**k)
	return QEditProp(**k)


# def Elements(wgt):
# 	elements=[
# 		QLineEdit.make('Field',	ro=1, k=k,	),
# 		QLineEdit.make('Dupl', k=k,	)	,
# 		QTextButton.make('Set', pol='F.F'	,	k=k,	),
# 		QIconButton.make('Edit', bi=1	,	k=k,	),
# 	]
# 	for e in elements:
# 		wgt['Elements'] |= gnr.Element(e)
# 	return wgt
#
# def Elements(wgt):
# 	wgt['Elements'] |= gnr.Element(QLineEdit.make('Field', ro=1, k=k, ))
# 	wgt['Elements'] |= gnr.Element(QLineEdit.make('Dupl', k=k,	))
# 	wgt['Elements'] |= gnr.Element(QTextButton.make('Set', pol='F.F', k=k,	))
# 	wgt['Elements'] |= gnr.Element(QIconButton.make('Edit', bi=1, k=k,	))
# 	return wgt