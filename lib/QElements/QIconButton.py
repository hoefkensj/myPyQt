#!/usr/bin/env python
# Auth

from lib import gnr,Create
from static.QtLibs import QElements

from Configs import QDefaults,Config
def QIconButton(**k):
	def Fnx(wgt):
		wgt=gnr.Fnx(wgt)
		return wgt
	def Con(wgt):
		c={}
		c['clicked'] = wgt['Fnx']['Sig']['clicked'].connect
		wgt['Con']=c
		return wgt
	def Init(wgt)     :
		wgt=wgt['Fnx']['Configure'](wgt)
		return wgt
	w						=			Create.QComponent(QElements['iBtn'], **k)
	w						=			Config.make(w,**k)
	w						=			Create.Mtds(w)
	w						=			Fnx(w)
	w						=			Con(w)
	return Init(w)

def make(namestr, **k):
	iconame=namestr.split('_')[0]
	preset=QDefaults.QIconButton|{
		'ico'       :	gnr.IconSet(iconame)	,
	}
	k=Config.preset(['iBtn',namestr],preset,**k)
	return QIconButton(**k)