#!/usr/bin/env python
from Configs import QDefaults
from Fnx import QMake

def QLabel(**k):
	def Fnx(wgt):
		def Width():
			return wgt['Fnx']['Qtm']['Mtd']['width']()
		wgt['Fnx']={}
		wgt['Fnx']['Width']=Width
		return wgt


	return QMake.QBuild('QElm', 'lbl', Fnx, **k)

def make(name, **k):
	return QLabel(**(QDefaults.QLabel | k | {'Name': name}))



