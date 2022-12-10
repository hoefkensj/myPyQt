#!/usr/bin/env python
import QLib.Create
from QLib import gnr,Create
from QLib.QBases import QWidget
from Configs import Config,QDefaults
def QModule(*a,**k):
	def Elements(wgt):
		if a:
			wgt['Elements']=a[0]
		else:
			wgt['Elements']={}
		return wgt
	def Fnx(wgt):
		def Init(wgt):
			wgt=wgt['Fnx']['Generate'](wgt)
			wgt=wgt['Fnx']['Configure'](wgt)
			return wgt



		wgt['Fnx']['Init']	= Init
		return wgt

	def Init(wgt):
		wgt=wgt['Fnx']['Init'](wgt)
		return wgt
	w	= QWidget.make(k['name'], **k)
	w	=	Elements(w)
	w	=	Fnx(w)
	return 	Init(w)


def make(namestr,**k):
	preset=	QDefaults.QModule
	Elements=k.pop('Elements')
	k=Config.preset(['wgt',namestr],preset,**k)
	return QModule(Elements,**k)