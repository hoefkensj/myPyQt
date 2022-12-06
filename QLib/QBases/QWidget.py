#!/usr/bin/env python
import QLib.Create
from static import QtLibs
from QLib import Create,gnr
from Configs import Config
from QLib.QBases import QLayout


def QWidget(**k):
	def Lay(wgt):
		if k.get('t'):
			return QLayout.make(wgt, **k)
	def Fnx(wgt):
		wgt= QLib.Create.Fnx(wgt)
		wgt= QLib.Create.Generate(wgt)
		wgt['Fnx']['Add']		=	wgt['Lay']['Fnx']['Add']
		return wgt
	def Init(wgt):
		return gnr.QWgtInit(wgt)
	w							=	Create.QComponent(QtLibs.QElements['wgt'], **k)
	w['Elements'] = {}
	w['Lay']			= Lay(w)
	w							=	Fnx(w)
	return  Init(w)

def make(namestr,**k):
	preset=Config.QDefaults.QWidget
	k=Config.preset(['wgt',namestr],preset,**k)
	return QWidget(**k)