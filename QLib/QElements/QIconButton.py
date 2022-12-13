#!/usr/bin/env python
from QLib import gnr,Create
from Qt.QtLibs import QElements
from Configs import QDefaults,Config
def QIconButton(**k):
	def Con(wgt):
		return wgt
	def Init(wgt)     :
		wgt=gnr.QElementInit(wgt)
		return wgt
	w						=			Create.QComponent(QElements['iBtn'], **k)
	w						=			Con(w)
	return Init(w)

def make(namestr, **k):
	iconame=namestr.split('_')[0]
	preset=QDefaults.QIconButton|{
		'ico'       :	gnr.IconSet(iconame)	,
	}
	k=Config.preset(['iBtn',namestr],preset,**k)
	return QIconButton(**k)