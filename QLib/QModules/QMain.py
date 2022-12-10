#!/usr/bin/env python
import QLib.Create
from QLib import gnr,Create
from QLib.QBases import QWidget
from Configs import Config
def QMain(**k):
	def Fnx(wgt):
		def Run(wgt):
			def run():
				wgt['Fnx']['Generate'](wgt)
				wgt['Fnx']['Show']()
				return wgt
			return run
		wgt= QLib.Create.Fnx(wgt)
		wgt=QLib.Create.Show(wgt)
		wgt['Fnx']['Run']	=	Run(wgt)
		return wgt
	def Init(wgt):
		wgt=wgt['Fnx']['Configure'](wgt)
		return Create.Mtds(wgt)
	w							=		QWidget.make(k['name'], **k)
	w							=		Fnx(w)
	w['Elements']	=		{}
	return Init(w)

def make(namestr,**k):
	preset={
	't'         :	'V'			,}
	k=Config.preset(['wgt',namestr],preset,**k)
	return QMain(**k)
