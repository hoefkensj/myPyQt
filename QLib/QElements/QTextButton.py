#!/usr/bin/env python
from QLib import gnr,Create
from static.QtLibs import QElements
from Configs import QDefaults,Config
def QtextButton(**k):
	def Con(wgt):
		wgt['Con']['clicked'] = wgt['Fnx']['Sig']['clicked'].connect
		return wgt
	def Init(wgt)     :
		wgt=gnr.minInit(wgt)
		return wgt
	w						=			Create.QComponent(QElements['tBtn'], **k)
	w						=			Con(w)
	return Init(w)

def make(namestr,**k):
	preset=QDefaults.QTextButton|{
		'txt'       :	namestr								,
	}
	k=Config.preset(['tBtn',namestr],preset,**k)
	return QtextButton(**k)