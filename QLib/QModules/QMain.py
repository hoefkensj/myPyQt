#!/usr/bin/env python
import QLib.Create
from QLib import gnr,Create
from QLib.QBases import QWidget
from Configs import Config,QDefaults
def QMain(**k):
	def Elements(wgt):
		wgt['Elements']={}
		return wgt
	def Fnx(wgt):
		def Run(wgt):
			def run():
				wgt['Fnx']['Generate'](wgt)
				wgt['Fnx']['Configure'](wgt)
				return wgt
			return run
		wgt['Fnx']['Show']=	wgt['Fnx']['Mtd']['show']
		wgt['Fnx']['Run']	=	Run(wgt)
		return wgt
	def Init(wgt):

		return Create.Mtds(wgt)
	w							=		QWidget.make(k['name'], **k)
	w	=	Elements(w)
	w	=	Fnx(w)
	return Init(w)

def make(namestr,**k):
	preset=	QDefaults.QModule|{
	't'         :	'V'			,}
	k=Config.preset(['wgt',namestr],preset,**k)
	return QMain(**k)
