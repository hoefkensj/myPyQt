#!/usr/bin/env python
from Configs import QDefaults
from Fnx import QMake

def QLineEdit(**k):
	def Fnx(wgt):
		def RO():	wgt['Qtm']['Set']['ReadOnly'](True)
		def RW():	wgt['Qtm']['Set']['ReadOnly'](False)
		wgt['Fnx'] = {}
		wgt['Fnx']['Write']		=	wgt['Qtm']['Set']['Text']
		wgt['Fnx']['Read']		=	wgt['Qtm']['Get']['Text']

		wgt['Fnx']['RO']			=	RO
		wgt['Fnx']['RW']			=	RW
		wgt['Fnx']['ED']			=	wgt['Qtm']['Get']['ReadOnly']
		return wgt

	return QMake.QBuild('QElm', 'txtE', Fnx, **k)

def make(name, **k):
		return QLineEdit(**(QDefaults.QLineEdit | k | {'Name': name}))