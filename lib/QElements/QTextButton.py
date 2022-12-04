#!/usr/bin/env python
from lib import gnr,Create
from static.QtLibs import QElements

from Configs import QDefaults,Config
def QtextButton(**k):
	def Fnx(wgt):
		wgt=gnr.Fnx(wgt)
		return wgt
	def Con(wgt):
		c={}
		c['clicked'] = wgt['Fnx']['Sig']['clicked'].connect
		return c
	def Init(wgt)     :
		wgt=wgt['Fnx']['Configure'](wgt)
		return wgt
	w						=			Create.QComponent(QElements['tBtn'], **k)
	w						=			Config.make(w,**k)
	w						=			Fnx(w)
	w['Con']		=			Con(w)
	return Init(w)

def make(namestr,**k):
	preset={
		'pol'       :	'P.P'									,
		'bi'        :	False									,
		'txt'       :	namestr								,
		'btn'       :	'T'
	}
	k=Config.preset(['tBtn',namestr],preset,**k)
	return QtextButton(**k)