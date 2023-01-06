#!/usr/bin/env python
from Configs import QDefaults
from Fnx import QMake

def QIconCheckBox(**k):
	def Fnx(wgt):
		def toggle():
			state=wgt['Fnx']['Qt']['Get']['Checked']
			wgt['Fnx']['Qt']['Set']['Checked'](not state)
		wgt['Fnx']={}
		wgt['Fnx']['Toggle']			= toggle
		return wgt
	k|={'ico': k.get('Name')}

	return QMake.QBuild('QElm', 'chkB', Fnx, **k)

def make(name, **k):
	return QIconCheckBox(**(QDefaults.QIconCheckBox | k | {'Name': name}))

