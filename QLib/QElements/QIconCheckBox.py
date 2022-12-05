#!/usr/bin/env python
from QLib import gnr,Create
from static.QtLibs import QElements
from Configs import QDefaults,Config
def QIconCheckBox(**k):
	def Fnx(wgt):
		def toggle():
			state=wgt['Fnx']['Get']['Checked']
			wgt['Fnx']['Set']['Checked'](not state)
		wgt['Fnx']['Toggle']			= toggle
		return wgt
	def Con(wgt):
		wgt['Con']['clicked'] = w['Wgt'].clicked.connect
		wgt['Con']['clicked'](wgt['Fnx']['Toggle'])
		return wgt
	def Init(wgt)     :
		wgt=gnr.minInit(wgt)
		return wgt
	w						=			Create.QCreate(QElements['iChk'], **k)
	w						=			Fnx(w)
	w['Con']		=			Con()
	return Init(w)

def make(namestr, **k):
	iconame=namestr.split('_')[0]
	preset=QDefaults.QIconButton|{
		'ico'       :	gnr.IconSet(iconame)	,
	}
	k=Config.preset(['iChk',namestr],preset,**k)
	return QIconCheckBox(**k)