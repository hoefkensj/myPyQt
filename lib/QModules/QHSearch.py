#!/usr/bin/env python
# Auth
from lib import gnr
from lib.QElements import QtWgt
from Configs import QDefaults,Config
from lib.QElements import QIconButton
from lib.QBases import QWidget
from lib.QModules	import QHSearchCtl,QHArrowsLR
def QHSearch(**k):
	def Elements(wgt):
		if 'Elements' not in wgt:wgt['Elements'] = {}
		parent=wgt['name']
		wgt['Elements'] |= gnr.Element(QtWgt.make(f'Field_{parent}', pfx='txtE', pol='E.F'))
		wgt['Elements'] |= gnr.Element(QIconButton.make(f'Reg_{parent}',AutoRaise=True, bi=True))
		wgt['Elements'] |=	gnr.Element(QHArrowsLR.make(f'<>_{parent}', bi=False))
		wgt['Elements'] |=	gnr.Element(QIconButton.make(f'Search_{parent}', bi=False))
		return wgt
	def Els(wgt):
		wgt['Els']=gnr.ShortNames(wgt)
		return wgt
	def Fnx(wgt):
		s=gnr.ShortNames(wgt)
		def ShowPN(wgt):
			def showpn(show):
				s['<>']['Fnx']['Set']['Hidden'](not show)
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
			s=gnr.ShortNames(wgt)
			def init():
				wgt['Fnx']['ShowPN'](False)
			return init
		wgt=gnr.Fnx(wgt)
		wgt['Fnx']['ShowPN']	= ShowPN(wgt)
		wgt['Fnx']['Visible'] =	Visible(wgt)
		wgt['Fnx']['Init']		=	Init(wgt)
		wgt['Fnx']['x']				=s['Field']['Fnx']['Mtd']['x']
		wgt['Fnx']['y']				=s['Field']['Fnx']['Mtd']['y']
		wgt['Fnx']['width']		=s['Field']['Fnx']['Mtd']['width']
		return wgt
	def Con(wgt):
		s=gnr.ShortNames(wgt)
		c = {}
		c['Reg']=s['Reg']['Fnx']['Sig']['toggled'].connect
		c['Search']=s['Search']['Fnx']['Sig']['clicked'].connect
		wgt['Con']=c
		return wgt
	def Init(wgt):
		wgt=gnr.minInit(wgt)
		return wgt
	w						=	QWidget.make(k['name'], **k)
	w						=	Config.make(w,**k)
	w						= Elements(w)
	w						=	Els(w)
	w						=	Fnx(w)
	w						=	Con(w)
	return Init(w)


def make(namestr,**k):
	k	= {
		**QDefaults.Properties						,
		'ed'        :	True								,
		'pol'       :	'E.F'								,
		't'         :	'H'									,
	} |	k	|	{
		'pfx'       :	'wgt'								,
		'name'      :	f'{namestr}Search'	,
	}
	return  QHSearch(**k)

