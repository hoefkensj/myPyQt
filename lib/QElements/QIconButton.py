#!/usr/bin/env python
# Auth

from lib import gnr,Create
from static.QtLibs import QElements

from Configs import QDefaults,Config
def QIconButton(**k):
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
	w						=			Create.QCreate(QElements['iBtn'], **k)
	w						=			Config.make(w,**k)
	w						=			Fnx(w)
	w['Con']		=			Con(w)
	return Init(w)

def make(namestr, **k):
	iconame=namestr.split('_')[0]
	preset={
		'pol'       :	'P.P'									,
		'wh'        :	[20,20]								,
		'bi'        :	False									,
		'ico'       :	gnr.IconSet(iconame)	,
		'isize'     :	[32,32]								,
		'lbl'       :	None									,
		'btn'       :	'I'										,
	}
	k=Config.preset(['iBtn',namestr],preset,**k)
	return QIconButton(**k)