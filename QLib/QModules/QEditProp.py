#!/usr/bin/env python
# Auth
import QLib.Create
from QLib.QElements import QTextButton,QIconButton,QLineEdit,QLabel
from QLib.QBases import QWidget
from QLib import gnr
from QLib.QElements import QtWgt
from Configs import Config,QDefaults

def Clean(**k):
	c={item : k.get(item) for item in k if item not in Config.QDefaults.Properties}
	return c

def QEditProp(**k):
	def Elements(wgt):
		l=Clean(**k)
		wgt['Elements'] |= gnr.Element(QLabel.make('Name', **l, ))
		wgt['Elements'] |= gnr.Element(QLineEdit.make('Field', ro=1,  **l,  ))
		wgt['Elements'] |= gnr.Element(QLineEdit.make('Dupl',  **l, 	))
		wgt['Elements'] |= gnr.Element(QTextButton.make('Set', pol='F.F',  **l, 	))
		wgt['Elements'] |= gnr.Element(QIconButton.make('Edit', bi=1,  **l, 	))
		return wgt
		
	def Fnx(wgt):
		s=gnr.Short(wgt,'Fnx')
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
		def Allign(max):
			sfn_set['Name']['MinimumWidth'](max)
		def Init(wgt):
			def init():
				sfn_set['Name']['Text'](sfn_get['Name']['Text']())
				sfn_set['Set']['Hidden'](True)
				sfn_set['Field']['ReadOnly'](True)
				sfn_set['Dupl']['Hidden'](True)
				wgt['Fnx']['Editable'](not k['ed'])
				return Internals(wgt)
			return init
		wgt= QLib.Create.Fnx(wgt)
		wgt['Fnx']['Edit'] 			=	Edit()
		wgt['Fnx']['txtText'] 	=	TxtText()
		wgt['Fnx']['setText']		=	SetText()
		wgt['Fnx']['Editable'] 	=	Editable()
		wgt['Fnx']['wLbl']			= s['Name']['Width']
		wgt['Fnx']['Allign']		= Allign
		wgt['Fnx']['Init']			=	Init(wgt)
		return wgt
	def Internals(wgt):
		wgt['Con']['Edit'](wgt['Fnx']['Edit'])
		wgt['Con']['Set'](wgt['Fnx']['setText'])
		wgt['Con']['Field']['returnPressed'](wgt['Fnx']['setText'])
		return wgt
	def Con(wgt):
		s=gnr.Short(wgt)
		# [print(a) for a in wgt]
		sCon=gnr.Short(wgt,'Con')
		sSig=gnr.Short(wgt,'Fnx','Sig')
		wgt['Con'] = wgt.get('Con') or {}
		wgt['Con']['Edit']= sCon['Edit']['clicked']
		wgt['Con']['Set']=	sCon['Set']['clicked']
		wgt['Con']['Field']	= {}
		wgt['Con']['Field']['returnPressed']= sSig['Field']['returnPressed'].connect
		return wgt
	def Init(wgt):
		wgt=gnr.QWgtInit(wgt)
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
# #
# def Elements(wgt):
# 	wgt['Elements'] |= gnr.Element(QLineEdit.make('Field', ro=1, k=k, ))
# 	wgt['Elements'] |= gnr.Element(QLineEdit.make('Dupl', k=k,	))
# 	wgt['Elements'] |= gnr.Element(QTextButton.make('Set', pol='F.F', k=k,	))
# 	wgt['Elements'] |= gnr.Element(QIconButton.make('Edit', bi=1, k=k,	))
# 	return wgt