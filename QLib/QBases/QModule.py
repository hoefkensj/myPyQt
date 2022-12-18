#!/usr/bin/env python
import QLib.Create
from QLib.QBases import QWidget
from QLib import gnr,Create
from Configs import Config,QDefaults
def QModule(**k):
	def Fnx(wgt):
		def Run(wgt):
			wgt['Fnx']['Gen']['Assemble'](wgt)
			return wgt

		wgt['Fnx']['Run']	=	Run
		return wgt
	def Init(wgt):
		return wgt
	w	= QWidget.make(k['name'], **k)
	w	=	Fnx(w)
	w['Compile']=w['Fnx']['Run']
	return 	Init(w)


def make(namestr,**k):
	preset=	QDefaults.QEditProp
	k=Config.preset(['mod',namestr],preset,**k)
	return QModule(**k)