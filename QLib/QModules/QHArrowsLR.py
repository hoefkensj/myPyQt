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
		wgt['Elements'] |= gnr.Element(QIconButton.make(f'<_{parent}', wh=[10,20],bi=False,k=k))
		wgt['Elements'] |= gnr.Element(QIconButton.make(f'>_{parent}', wh=[10,20],bi=False,k=k))
		return wgt
	def Con(wgt):
		s=gnr.Short(wgt,'Fnx')
		wgt['Con']['<']=	s['<']['Sig']['clicked'].connect
		wgt['Con']['>']=	s['>']['Sig']['clicked'].connect
		return wgt
	def Init(wgt):
		wgt=gnr.QWgtInit(wgt)
		return wgt
<<<<<<< HEAD
	w		= 		QWidget.make(k['name'], **k)
=======
	w= QWidget.make(k['name'], **k)
	w		=			Config.make(w,**k)
>>>>>>> parent of 8640264... Update workspace.xml, QDefaults.py, and 47 more files...
	w 	= 		Elements(w)
	w		=			Con(w)
	return Init(w)

def make(namestr,**k):
	preset=	QDefaults.QHArrowsLR
	k=Config.preset(['wgt',namestr],preset,**k)
	return QHArrowsLR(**k)