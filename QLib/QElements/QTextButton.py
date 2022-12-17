#!/usr/bin/env python
from QLib import gnr,Create
from QStatic.QtLibs import QElements
from Configs import QDefaults,Config
def QtextButton(**k):
	def Con(wgt):

		return wgt
	def Init(wgt)     :
		wgt=gnr.QElementInit(wgt)
		return wgt
	w						=			Create.QComponent(QElements['tBtn'], **k)
	w						=			Con(w)
	return Init(w)

def make(namestr,**k):
	preset=QDefaults.QTextButton
	k=k|{'lbl'       :	namestr								,	}
	k=Config.preset(['tBtn',namestr],preset,**k)
	return QtextButton(**k)