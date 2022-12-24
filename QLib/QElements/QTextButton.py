#!/usr/bin/env python
from QLib import Create
from QLib.QStatic import QElements
from Configs import QDefaults
from Configs import Config

def QtextButton(**k):
	def Con(wgt):

		return wgt
	def Init(wgt)     :

		return wgt
	w						=			Create.QComponent(QElements['tBtn'], **k)
	w						=			Con(w)
	return Init(w)

def make(namestr,**k):
	preset=QDefaults.QTextButton
	k=k|{'lbl'       :	namestr								,	}
	k= Config.preset(['tBtn', namestr], preset, **k)
	return QtextButton(**k)