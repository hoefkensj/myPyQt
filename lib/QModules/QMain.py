#!/usr/bin/env python
from lib import gnr,Create
from lib.QBases import QWidget
from Configs import Config
def QMain(**k):
	def Fnx(wgt):
		def Run(wgt):
			wgt['Fnx']['Generate']()
			wgt['Fnx']['Show']()
			return wgt
		wgt=gnr.Fnx(wgt)
		wgt['Fnx']['Run']	=	Run
		return wgt

	def Init(wgt):
		wgt=wgt['Fnx']['Configure'](wgt)
		return Create.Mtds(wgt)

	w						=		QWidget.make(k['name'], **k)
	w						=		Config.make(w,**k)
	w						=		Fnx(w)
	w['Elements']={}
	return Init(w)



def make(namestr,**k):
	preset={
	't'         :	'V'								,}
	k=Config.preset(['wgt',namestr],preset,**k)
	return QMain(**k)
