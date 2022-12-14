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
		wgt['Elements'] |= gnr.Element(QLabel.make('Name'))
		wgt['Elements'] |= gnr.Element(QLineEdit.make('Field',**k|{'ro':1 ,'pol':'E.F'}))
		wgt['Elements'] |= gnr.Element(QLineEdit.make('Dupl',**k))
		wgt['Elements'] |= gnr.Element(QTextButton.make('Set',**k|{'pol':'F.F'}))
		wgt['Elements'] |= gnr.Element(QIconButton.make('Edit',**k|{'bi':1}))
		return wgt
		
	def Fnx(wgt):
		sfn_mtd=gnr.ShortEl(wgt, 'Fnx', 'Mtd')
		sfn_set=gnr.ShortEl(wgt, 'Fnx', 'Set')
		sfn_get=gnr.ShortEl(wgt, 'Fnx', 'Get')
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
		def Allign():
			def allign(max):
				sfn_set['Name']['MinimumWidth'](max)
			return allign
		def Init():
			def init():
				lbl='{n} :'.format(n=wgt['name'])
				sfn_set['Name']['Text'](lbl)
				sfn_set['Set']['Hidden'](True)
				sfn_set['Field']['ReadOnly'](True)
				sfn_set['Dupl']['Hidden'](True)
				wgt['Fnx']['Editable'](not k['ed'])
				return wgt
			return init
		wgt['Fnx']['Generate']=QLib.Create.Generate()
		wgt['Fnx']['Configure']=QLib.Create.Configure()
		wgt['Fnx']['Edit'] 			=	Edit()
		wgt['Fnx']['txtText'] 	=	TxtText()
		wgt['Fnx']['setText']		=	SetText()
		wgt['Fnx']['Editable'] 	=	Editable()
		wgt['Fnx']['wLbl']			= sfn_mtd['Name']['width']
		wgt['Fnx']['Allign']		= Allign()
		wgt['Fnx']['Init']			=	Init()
		return wgt
	def Internals(wgt):
		sClk=gnr.sCon(wgt,'clicked')
		sClk['Edit'](wgt['Fnx']['Edit'])
		sClk['Set'](wgt['Fnx']['setText'])
		wgt['Con']['Field']['returnPressed'](wgt['Fnx']['setText'])
		return wgt
	def Con(wgt):
		#
		# sCon=gnr.ShortEl(wgt, 'Con')
		sSig=gnr.ShortEl(wgt, 'Fnx', 'Sig')
		wgt['Con'] = wgt.get('Con') or {}
		wgt=gnr.ModCon(wgt)
		# for el in wgt['Con']:
		# 	print(el)
		# 	for con in wgt['Con'][el]:
		# 		print('\t',con)
		# # wgt['Con']['Edit']=sCon['Edit']
		# # wgt['Con']['Set']=sCon['Set']
		# # wgt['Con']['Field']	= {}
		# # wgt['Con']['Field']['returnPressed']= sSig['Field']['returnPressed'].connect
		wgt=Internals(wgt)
		return wgt
	def Init(wgt):
		fn=wgt['Fnx']
		wgt=fn['Generate'](wgt)
		wgt=fn['Configure'](wgt)
		wgt=fn['Init']()
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

