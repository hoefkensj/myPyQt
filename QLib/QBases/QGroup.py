#!/usr/bin/env python
import QLib.Create
from static import QtLibs
from QLib import Create
from Configs import Config
from QLib.QBases import QLayout

def QGroup(**k):
	def Lay(wgt):
		if k.get('t'):
			return QLayout.make(wgt, **k)
	def Fnx(wgt):
		def Add(wgt):
			def add(component):
				wgt['Lay']['Fnx']['Add'](component)
			return add
		wgt= QLib.Create.Fnx(wgt)
		wgt['Fnx']['Add']				=	Add(wgt)
		return wgt
	def Init(wgt):
		wgt=wgt['Fnx']['Configure']()
		return wgt
	w							=	Create.QCreate(QtLibs.QElements['grp'], **k)
	w							=	Config.make(w,**k)
	w['Elements'] = {}
	w['Lay']			= Lay(w)
	w							=	Fnx(w)
	return  Init(w)

def make(namestr,**k):
	preset={
		'Names'     :	['wgt',namestr,'Edit'],
		'pol'       :	'E.E'							,
	}
	return QGroup(**Config.preset(preset,**k))