#!/usr/bin/env python
import QLib.Create
from static import QtLibs
from QLib import Create
from Configs import Config
from QLib.QBases import QLayout

def QWidget(**k):
	def Lay(wgt):
		if k.get('t'):
			return QLayout.make(wgt, **k)
	def Fnx(wgt):
		def Add(wgt):
			def add(component):
				wgt['Lay']['Fnx']['Add'](component)
			return add
		wgt= QLib.Create.Fnx(wgt)
		wgt= QLib.Create.Generate(wgt)
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