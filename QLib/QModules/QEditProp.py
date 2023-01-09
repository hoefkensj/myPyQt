#!/usr/bin/env python
# Auth
from QLib import gnr
from Configs import QDefaults
from Configs import Config
from QLib.QStatic import QtLibs
from pTree import pTree
from Fnx.debug import DebDec
import contextlib
from QLib.QElements import  QIconButton,QTextButton,QLabel,QLineEdit
from QLib.QBases import QWidget
from Fnx import QMake
def Clean(**k):
	c={item : k.get(item) for item in k if item not in Config.QDefaults.Properties}
	return c

def QEditProp(**k):
	def Mod():
		# GUI['Elements']|=gnr.Element(component)
		mod={}
		mod	|= QMake.Component(QLabel.make('Name'))
		mod	|= QMake.Component(QLineEdit.make('Field', ro=1))
		mod	|= QMake.Component(QLineEdit.make('Dupl'))
		mod	|= QMake.Component(QTextButton.make(f'Set'))
		mod	|= QMake.Component(QIconButton.make(f'Edit', bi=True))
		return mod


	def Fnx(wgt):
#SHORT#SHORT#SHORT
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
#SHORT
		# for el in wgt['Con']:
		# 	print(el)
		# 	for con in wgt['Con'][el]:
		# 		print('\t',con)
		# # wgt['Con']['Edit']=sCon['Edit']
		# # wgt['Con']['Set']=sCon['Set']
		# # wgt['Con']['Field']	= {}
		# # wgt['Con']['Field']['returnPressed']= sSig['Field']['returnPressed'].connect
		# wgt=Internals(wgt)
		return wgt
	# w	=	QWidget.make(k['Name'], t='H', **k)

	return QMake.QBuild('QMdl', 'Wgt', Fnx, **k)


def make(name,**k):
	return  QEditProp(**(QDefaults.QEditProp | k | {'Name': name}))
