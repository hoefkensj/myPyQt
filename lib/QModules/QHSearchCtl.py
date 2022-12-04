#!/usr/bin/env python
# Auth
from lib import gnr
from lib.QElements import QIconButton
from lib.QBases import QWidget
from lib.QModules import QHArrowsLR
from Configs import QDefaults,Config
def QHSearchCtl(**k):
	def Elements(wgt):
		if 'Elements' not in wgt:wgt['Elements'] = {}
		parent=wgt['name']
		wgt['Elements'] |=	gnr.Element(QHArrowsLR.make(f'<>_{parent}', bi=False))
		wgt['Elements'] |=	gnr.Element(QIconButton.make(f'Search_{parent}', bi=False))
		return wgt
	def Fnx(wgt):
		def Init(wgt):
			def init():
				pass
			return init
		wgt=gnr.Fnx(w)
		wgt['Fnx']['Init']=Init(wgt)
		return wgt
	def Con(wgt):
		s=gnr.ShortFnx(wgt)
		wgt['Con'] = {}
		wgt['Con']['Search']=	s['Search']['Fnx']['Sig']['clicked'].connect
		return wgt
	w						= QWidget.make(k['name'], **k)
	w						=Config.make(w,**k)
	w						= Elements(w)
	w						=	Fnx(w)
	w			=	Con(w)
	return gnr.minInit(w)

def make(namestr,**k):
	k	= QDefaults.Properties	|	{
		'pol'       :	'P.P'								,
		't'         :	'H'									,
	} |	k	|	Config.names('wgt',namestr,'SCtl')
	return QHSearchCtl(**k)



