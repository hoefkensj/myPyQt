#!/usr/bin/env python



from static import QtLibs
from lib import gnr,Create
from Configs import QDefaults,Config
from lib.QElements import QLayout

def QWidget(**k):
	def Lay(wgt):
		if k.get('t'):
			return QLayout.make(wgt,**k)
	def Fnx(wgt):
		def Add(wgt):
			def add(component):
				wgt['Lay']['Fnx']['Add'](component)
			return add
		wgt=gnr.Fnx(wgt)
		wgt['Fnx']['Add']				=	Add(wgt)
		return wgt
	def Init(wgt):
		wgt=wgt['Fnx']['Configure'](wgt)
		return wgt
	w							=	Create.QComponent(QtLibs.QElements['wgt'], **k)
	w['Elements'] = {}
	w['Lay']			= Lay(w)
	w							=	Fnx(w)
	return  Init(w)

def make(namestr,**k):
	preset={
		'pol'				:	'E.E'							,}
	k=Config.preset(['wgt',namestr],preset,**k)
	return QWidget(**k)