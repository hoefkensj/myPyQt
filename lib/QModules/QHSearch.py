#!/usr/bin/env python
# Auth
from lib import gnr
from lib.QElements import QtWgt,QIconButton,QLineEdit
from Configs import QDefaults,Config
from lib.QBases import QWidget
from lib.QModules	import QHArrowsLR

def QHSearch(**k):
	def Elements(wgt):
		es=[
			# QtWgt.make('Field',pfx='txtE',pol='E.F',),
			QLineEdit.make('Field'),
			QIconButton.make(	'Reg',AutoRaise=1,bi=1),
			QHArrowsLR.make('<>'),
			QIconButton.make('Search'),]
		for e in es:
			wgt['Elements'] |= gnr.Element(e)
		return wgt

	def Fnx(wgt):
		s=gnr.Short(wgt,'Fnx')
		def ShowPN(wgt):
			def showpn(show):
				s['<>']['Set']['Hidden'](not show)
			return showpn
		# def selNext(Tree):
		# 	def sel():
		# 		item=wgt.Found.pop(0)
		# 		Tree.setCurrentItem(wgt.Found[0])
		# 		wgt.Found.append(item)
		# 	return sel
		# def selPrev(Tree):
		# 	def sel():
		# 		item=wgt.Found.pop(-1)
		# 		Tree.setCurrentItem(item)
		# 		wgt.Found=[item,*wgt.Found]
		# 	return sel
		# wgt.showPN 	= dispPN(wgt)
		# wgt.selNext		=	selNext
		# wgt.selPrev		=	selPrev
		# return wgt
		def Visible(wgt):
			def visible(state):
				w['Wgt']['Set']['Visible'](state)
			return visible
		def Init(wgt):
			s=gnr.Short(wgt,'Fnx')
			def init():
				wgt['Fnx']['ShowPN'](False)
			return init
		wgt=gnr.Fnx(wgt)
		wgt['Fnx']['ShowPN']	= ShowPN(wgt)
		wgt['Fnx']['Visible'] =	Visible(wgt)
		wgt['Fnx']['Init']		=	Init(wgt)
		wgt['Fnx']['x']				=s['Field']['Mtd']['x']
		wgt['Fnx']['y']				=s['Field']['Mtd']['y']
		wgt['Fnx']['width']		=s['Field']['Mtd']['width']
		return wgt
	def Con(wgt):
		sfn=gnr.Short(wgt,'Fnx')
		wgt['Con']['Reg']=sfn['Reg']['Sig']['toggled'].connect
		wgt['Con']['Search']=sfn['Search']['Sig']['clicked'].connect
		return wgt
	def Init(wgt):
		wgt=gnr.minInit(wgt)
		return wgt
	w						=	QWidget.make(k['name'], **k)
	w						= Elements(w)
	w						=	Fnx(w)
	w						=	Con(w)
	return Init(w)


def make(namestr,**k):
	preset=	QDefaults.QHSearch
	k=Config.preset(['wgt',namestr],preset,**k)
	return  QHSearch(**k)

