#!/usr/bin/env python
from QLib.QStatic import QtLibs
from QLib import Create
from Configs import Config
from QLib.QBases import QLayout

def QGroup(**k):
	def Lay(wgt):
		if k.get('t'):
			return QLayout.make(wgt, **k)

	w							=	Create.QCreate(QtLibs.QElements['grp'], **k)
	w['Lay']			= Lay(w)

	return w

def make(namestr,**k):
	preset={
		'Names'     :	['wgt',namestr,'Edit'],
		'pol'       :	'E.E'							,
	}
	return QGroup(**Config.preset(preset, **k))