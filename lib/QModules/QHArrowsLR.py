#!/usr/bin/env python
# Auth
from lib import gnr
from lib.QElements import QIconButton
from Configs import QDefaults,Config
from lib.QBases import QWidget

def QHArrowsLR(**k):
	def Elements(wgt):
		parent=wgt['name']
		wgt['Elements'] |= gnr.Element(QIconButton.make(f'<_{parent}', wh=[10,20],bi=False))
		wgt['Elements'] |= gnr.Element(QIconButton.make(f'>_{parent}', wh=[10,20],bi=False))
		return wgt
	def Fnx(wgt):
		def Init(wgt):
			def init():
				pass
			return init
		wgt=gnr.Fnx(wgt)
		wgt['Fnx']['Init']=Init(wgt)
		return wgt
	def Con(wgt):
		s=gnr.Short(wgt,'Fnx')
		wgt['Con']['<']=	s['<']['Sig']['clicked'].connect
		wgt['Con']['>']=	s['>']['Sig']['clicked'].connect
		return wgt
	def Init(wgt):
		wgt=gnr.minInit(wgt)
		return wgt
	w= QWidget.make(k['name'], **k)
	w		=			Config.make(w,**k)
	w 	= 		Elements(w)
	w		= 		Fnx(w)
	w		=			Con(w)
	return Init(w)

def make(namestr,**k):
	preset=	QDefaults.QHArrowsLR
	k=Config.preset(['wgt',namestr],preset,**k)
	return QHArrowsLR(**k)