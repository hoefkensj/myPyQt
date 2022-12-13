#!/usr/bin/env python
import QLib.Create
from QLib.QBases import QWidget
from QLib import gnr,Create
from Configs import Config,QDefaults
def QModule(**k):
	def Elements(wgt):
		wgt['Elements']={}
		return wgt
	def Fnx(wgt):
		def Run(wgt):
			wgt['Fnx']['Generate'](wgt)
			return wgt
		wgt= QLib.Create.Fnx(wgt)
		wgt['Fnx']['Run']	=	Run
		return wgt
	def Init(wgt):
		wgt=wgt['Fnx']['Configure'](wgt)
		wgt=Create.Mtds(wgt)
		return wgt
	w	= QWidget.make(k['name'], **k)
	w	=	Elements(w)
	w	=	Fnx(w)
	w['Compile']=w['Fnx']['Run']
	return 	Init(w)


def make(namestr,**k):
	preset=	QDefaults.QEditProp
	k=Config.preset(['mod',namestr],preset,**k)
	return QModule(**k)