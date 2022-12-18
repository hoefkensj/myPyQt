#!/usr/bin/env python
import QLib.Create
from Configs import QDefaults,Config

def QLayout(**k):
	def Fnx(wgt):
		def Add(wgt):
			def add(component):
				wgt['Fnx']['Qt']['Mtd']['addWidget'](component)
			return add
		wgt['Fnx']['Add']	=	Add(wgt)
		return wgt
	def Init(wgt):
		wgt=wgt['Fnx']['Gen']['Configure'](wgt)
		return wgt
	l= QLib.Create.QLayout(**k)
	l			= Fnx(l)
	return Init(l)

def make(widget,**k):
	namestr=widget['name']
	preset=QDefaults.QLayout|{
		'widget'    :	widget	,	}
	k=Config.preset(['lay',namestr],preset,**k)
	return QLayout(**k)