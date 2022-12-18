#!/usr/bin/env python
import QLib.Create
from Configs import QDefaults,Config
from Configs import skel

def QLayout(**k):
	def Fnx(wgt):
		wgt['Fnx']['Add']	= wgt['Fnx']['Qt']['Mtd']['addWidget']
		return wgt
	w			= skel.QLayout
	w			= QLib.Create.QLayout(w,**k)
	l			= Fnx(l)
	return l

def make(widget,**k):
	namestr=widget['name']
	preset=QDefaults.QLayout|{
		'widget'    :	widget	,	}
	k=Config.preset(['lay',namestr],preset,**k)
	return QLayout(**k)