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
		c['clicked'] = wgt['Sig']['clicked'].connect
		return c
	def Init(wgt)     :
		wgt=wgt['Fnx']['Configure']()
		return wgt
	w						=			Create.QCreate(QElements['tBtn'], **k)
	w						=			Config.make(w,**k)
	w						=			Fnx(w)
	w['Con']		=			Con(w)
	return Init(w)

def make(namestr,**k):
	preset={
		'Names'			:	['tBtn',namestr],
		'pol'       :	'P.P'									,
		'wh'        :	[20,20]								,
		'bi'        :	False									,
		'icowh'     :	[32,32]								,
		'txt'       :	namestr									,
		'btn'       :	'T'
	}
	return QtextButton(**Config.preset(preset,**k))