#!/usr/bin/env python
from QLib.QElements import QIconButton
from QLib.QBases import QWidget
from QLib import gnr
from Configs import Config,QDefaults

def QHIncDec(**k):
	def Elements(wgt):
		wgt['Elements'] |=gnr.Element(QIconButton.make(f'Inc', h=15, w=15, bi=False))
		wgt['Elements'] |=gnr.Element(QIconButton.make(f'Dec', h=15, w=15, bi=False))
		return wgt
	def Fnx(wgt):
		def StateInc():
			def stateinc(state):
				s['inc']['Set']['Enabled'](state)
			return stateinc
		def StateDec():
			def statedec(state):
				s['Dec']['Set']['Enabled'](state)
			return statedec
		def Show():
			def show(state):
				w['Wgt']['Set']['Visible'](state)
				return show
		wgt['Fnx']['Inc'] 		=	StateInc()
		wgt['Fnx']['Dec'] 		=	StateDec()
		wgt['Fnx']['IncDec'] 	=	Show()
		return wgt
	def Con(wgt):
		s=gnr.sCon(wgt)
		return wgt
	def Init(wgt):
		wgt['Gen']['Assemble'](wgt)
		wgt['Gen']['Configure'](wgt)
		return wgt

	w	=		QWidget.make(k['name'], **k)
	w = 	Elements(w)
	w	= 	Fnx(w)
	w	=		Con(w)
	return Init(w)

def make(namestr,**k):
	preset=	QDefaults.QHIncDec
	k=Config.preset(['wgt',namestr],preset,**k)
	return QHIncDec(**k)