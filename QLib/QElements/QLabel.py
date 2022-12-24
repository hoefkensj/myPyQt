#!/usr/bin/env python
from QLib import gnr,Create
from QLib.QStatic import QElements
from Configs import QDefaults
from Configs import Config

def QLabel(**k):
	def Fnx(wgt):
		def Width():
			return wgt['Fnx']['Qt']['Mtd']['width']()
		wgt['Fnx']['Width']=Width
		return wgt
	def Init(wgt)     :
		wgt=gnr.QElementInit(wgt)
		return wgt
	w		=			Create.QComponent(QElements['lbl'], **k)
	w		=			Fnx(w)

	return Init(w)

def make(namestr, **k):
	preset=QDefaults.QLabel|{
		'lbl'       :	f'{k.get("name")}'								,
	}
	k= Config.preset(['lbl', namestr], preset, **k)
	return QLabel(**k)
