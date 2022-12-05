#!/usr/bin/env python
from lib import gnr,Create
from static.QtLibs import QElements

from Configs import QDefaults,Config
def QLineEdit(**k):
	def Fnx(wgt):
		wgt=gnr.Fnx(wgt)
		def RO():	wgt['Fnx']['Set']['ReadOnly'](True)
		def RW():	wgt['Fnx']['Set']['ReadOnly'](False)
		wgt['Fnx']['Read']		=	wgt['Fnx']['Get']['Text']
		wgt['Fnx']['Write']		=	wgt['Fnx']['Set']['Text']
		wgt['Fnx']['RO']			=	RO
		wgt['Fnx']['RW']			=	RW
		wgt['Fnx']['ED']			=	wgt['Fnx']['Get']['ReadOnly']
		return wgt

	def Con(wgt):
		wgt['Con']['Entered']	=wgt['Fnx']['Sig']['returnPressed'].connect
		wgt['Con']['Changed']	=wgt['Fnx']['Sig']['textChanged'].connect
		wgt['Con']['Edited']	=wgt['Fnx']['Sig']['textEdited'].connect
		return wgt
	def Init(wgt)     :
		wgt=gnr.minInit(wgt)
		return wgt
	w						=			Create.QComponent(QElements['txtE'], **k)
	w						=			Fnx(w)
	w						=			Con(w)
	return Init(w)

def make(namestr, **k):
	preset=QDefaults.QLineEdit|{}
	k=Config.preset(['txtE',namestr],preset,**k)
	return QLineEdit(**k)
