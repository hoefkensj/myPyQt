#!/usr/bin/env python
from QLib import Create
from QLib.QStatic import QElements

from Configs import QDefaults
from Configs import Config

def QLineEdit(**k):
	def Fnx(wgt):
		def RO():	wgt['Fnx']['Qt']['Set']['ReadOnly'](True)
		def RW():	wgt['Fnx']['Qt']['Set']['ReadOnly'](False)
		wgt['Fnx']['Write']		=	wgt['Fnx']['Qt']['Set']['Text']
		wgt['Fnx']['Read']		=	wgt['Fnx']['Qt']['Get']['Text']

		wgt['Fnx']['RO']			=	RO
		wgt['Fnx']['RW']			=	RW
		wgt['Fnx']['ED']			=	wgt['Fnx']['Qt']['Get']['ReadOnly']
		return wgt

	def Init(wgt)     :
		wgt=wgt['Fnx']['Gen']['Configure'](wgt)
		return wgt
	w						=			Create.QComponent(QElements['txtE'], **k)
	w						=			Fnx(w)

	return Init(w)

def make(namestr, **k):
	preset=QDefaults.QLineEdit
	k= Config.preset(['txtE', namestr], preset, **k)
	return QLineEdit(**k)
