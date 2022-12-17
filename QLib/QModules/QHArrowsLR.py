#!/usr/bin/env python
# Auth
import QLib.Create
from QLib import gnr
from QLib.QElements import QIconButton
from Configs import QDefaults,Config
from QLib.QBases import QWidget

def QHArrowsLR(**k):
	def Elements(wgt):
		parent=wgt['name']
		wgt['Elements'] |= gnr.Element(QIconButton.make(f'<', wh=[10,20],bi=False,k=k))
		wgt['Elements'] |= gnr.Element(QIconButton.make(f'>', wh=[10,20],bi=False,k=k))
		return wgt
	def Fnx(wgt):
		def Init(wgt):
			def init():
				pass
			return init

		wgt['Fnx']['Init']=Init(wgt)
		return wgt
	def Con(wgt):
		wgt['Gen']['ConnectElements'](wgt)
			# s=gnr.ShortEl(wgt, 'Fnx')
			# wgt['Con']['<']=	s['<']['Sig']['clicked'].connect
			# wgt['Con']['>']=	s['>']['Sig']['clicked'].connect
		return wgt
	def Init(wgt):
		wgt=gnr.QWgtInit(wgt)
		return wgt
	w		= QWidget.make(k['name'], **k)
	w 	= 		Elements(w)
	w		= 		Fnx(w)
	w		=			Con(w)
	return Init(w)

def make(namestr,**k):
	preset=	QDefaults.QHArrowsLR
	k=Config.preset(['wgt',namestr],preset,**k)
	return QHArrowsLR(**k)