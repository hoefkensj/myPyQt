#!/usr/bin/env python
from QLib import Create
from Configs import QDefaults
from Configs import Config
import Fnx
def QIconButton(**k):
	def Con(wgt):
		return wgt
	def Init(wgt)     :
		return wgt
	w						=			Create.QComponent('iBtn', **k)
	w						=			Con(w)
	return Init(w)

def make(namestr, **k):
	iconame=namestr.split('_')[0]
	preset=QDefaults.QIconButton|{
		'ico'       :	Fnx.qmake.IconSet(iconame)	,
		'Name'      : namestr,
	}
	k = Config.preset(preset, **k)
	return QIconButton(**k)