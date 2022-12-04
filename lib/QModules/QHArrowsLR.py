#!/usr/bin/env python
# Auth
from lib import gnr
from lib.QElements import QIconButton
from Configs import QDefaults,Config
from lib.QBases import QWidget

def QHArrowsLR(**k):
	def Elements(wgt):
		wgt['Elements'] = wgt.get('Elements') or {}
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
		wgt['Con'] = wgt.get('Con') or {}
		s=gnr.Short(wgt,'Fnx')
		wgt['Con']['<']=	s['<']['Sig']['clicked'].connect
		wgt['Con']['>']=	s['>']['Sig']['clicked'].connect
		return wgt
	w= QWidget.make(k['name'], **k)
	w		=			Config.make(w,**k)
	w 	= 		Elements(w)
	w		= 		Fnx(w)
	w		=			Con(w)
	return gnr.minInit(w)

def make(namestr,**k):
	preset=	QDefaults.QHArrowsLR
	k=Config.preset(['wgt',namestr],preset,**k)
	return QHArrowsLR(**k)