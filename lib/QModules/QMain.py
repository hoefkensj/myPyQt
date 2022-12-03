#!/usr/bin/env python
from lib import gnr
from lib.QBases import QWidget
from Configs import Config,QDefaults
def QMain(**k):
	def Fnx(wgt):
		def Init(wgt):
			def init():
				wgt['Fnx']['Show'](False)
			return init

		wgt=gnr.Fnx(wgt)

		wgt['Fnx']['Init'] = Init(wgt)
		return wgt



	def Init(wgt):
		wgt=gnr.minInit(wgt)

		return wgt



	w						=		QWidget.make(k['name'], **k)
	w						=		Config.make(w,**k)
	w						=		Fnx(w)
	w['Add']		=		w['Fnx']['Add']
	return Init(w)



def make(namestr,**k):
	preset={
	't'         :	'V'								,}
	k=Config.preset(['wgt',namestr],preset,**k)
	return QMain(**k)
