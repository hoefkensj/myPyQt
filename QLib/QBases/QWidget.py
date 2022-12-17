#!/usr/bin/env python
import QLib.Create
from QStatic import QtLibs
from QLib import Create,gnr
from Configs import Config,QDefaults
from QLib.QBases import QLayout


def QWidget(**k):
	def Lay(wgt):
		if k.get('t'):
			wgt['Lay']=QLayout.make(wgt, **k)
		return wgt
	def Fnx(wgt):
		wgt['Fnx']['Add']		=	wgt['Lay']['Fnx']['Add']
		return wgt
	def Init(wgt):
		return gnr.QWgtInit(wgt)
	w				=	Create.QBase(QtLibs.QElements['wgt'], **k)
	w['Elements']	=	{}
	w				=	Lay(w)
	w				=	Fnx(w)
	w['Con']		=	{}
	return  Init(w)

def make(namestr,**k):
	preset=QDefaults.QWidget
	k=Config.preset(['wgt',namestr],preset,**k)
	return QWidget(**k)