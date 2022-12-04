#!/usr/bin/env python
from lib.QElements import QIconButton
from lib.QBases import QWidget
from lib import gnr
from Configs import Config


def QHIncDec(**k):
	def Elements():
		parent=w['name']
		e		= {}
		e|=gnr.Element(QIconButton.make(f'Inc_{parent}', h=15, w=15, bi=False))
		e|=gnr.Element(QIconButton.make(f'Dec_{parent}', h=15, w=15, bi=False))
		return e
	def Fnx():
		s=Short()
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
		f = {}
		f['Inc'] 		=	StateInc()
		f['Dec'] 		= StateDec()
		f['IncDec'] =	Show()
		return f

	def Con(wgt):
		s=gnr.ShortFnx(wgt)
		c = {}
		c['Inc']=	s['inc']['Mtd']['clicked'].connect
		c['Dec']=	s['dec']['Mtd']['clicked'].connect
		return c


	def Init(w):
		for element in w['Elements']:
			w['Fnx']['Add'](w['Elements'][element])
		s=Short()
		return w

	w= QWidget.make(k['name'], **k)
	w	=	Config.Cfg(w,**k)
	w['Elements']=Elements()
	w['Fnx'] 			|=	Fnx()
	w['Con']			|=	Con()
	return Init(w)

def make(name,pfx='wgt',**k):
	Names=gnr.makeNames(name=name,pfx=pfx)
	kwargs={
	'pfx_name'  :	Names['pfx_name'],
	'pfx'       :	Names['pfx'],
	'name'      :	Names['name'],
	'qt'        : gnr.PfxMap(pfx),}
	k|=kwargs
	return QHIncDec(**k)