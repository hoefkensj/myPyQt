#!/usr/bin/env python
from QLib import Create
from Qt.QtLibs import QElements

from Configs import QDefaults,Config
def QLineEdit(**k):
	def Fnx(wgt):
		def RO():	wgt['Fnx']['Set']['ReadOnly'](True)
		def RW():	wgt['Fnx']['Set']['ReadOnly'](False)
		wgt['Fnx']['Write']		=	wgt['Fnx']['Set']['Text']
		wgt['Fnx']['Read']		=	wgt['Fnx']['Get']['Text']

		wgt['Fnx']['RO']			=	RO
		wgt['Fnx']['RW']			=	RW
		wgt['Fnx']['ED']			=	wgt['Fnx']['Get']['ReadOnly']
		return wgt

	def Con(wgt):
		return wgt
	def Init(wgt)     :
		wgt=wgt['Fnx']['Configure'](wgt)
		return wgt
	w						=			Create.QComponent(QElements['txtE'], **k)
	w						=			Fnx(w)
	w						=			Con(w)
	return Init(w)

def make(namestr, **k):
	preset=QDefaults.QLineEdit
	k=Config.preset(['txtE',namestr],preset,**k)
	return QLineEdit(**k)
