#!/usr/bin/env python
from QStatic import QtLibs
from QLib import Create,gnr
from Configs import Config,QDefaults
from QLib.QBases import QLayout

def QBase(**k):
	def Lay(wgt):
		if k.get('t'):
			wgt['Lay']=QLayout.make(wgt, **k)
		return wgt
	def Fnx(wgt):
		def Add(wgt):
			def add(component):
				cmpWgt=component['Wgt']
				wgt['Lay']['Fnx']['Add'](cmpWgt)
				wgt['Fnx'][component['name']]=component['Fnx']
				wgt['Con'][component['name']]=component['Con']
				return wgt
			return add
		wgt['Fnx']['Add']		= Add(wgt)

		return wgt

	w				=	Create.QBase(QtLibs.QElements['wgt'], **k)
	w['Elements']	=	{}
	w				=	Lay(w)
	w				=	Fnx(w)
	w['Con']		=	{}
	return  w

def make(namestr,**k):
	preset=QDefaults.QWidget
	k=Config.preset(['wgt',namestr],preset,**k)
	return QWidge