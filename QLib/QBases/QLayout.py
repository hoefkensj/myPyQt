#!/usr/bin/env python
import QLib.Create
from Configs import QDefaults,Config

def QLayout(**k):
	def Fnx(wgt):
		def Add(wgt):
			def add(component):
				wgt['Fnx']['Mtd']['addWidget'](component)
			return add
		wgt['Fnx']['Add']	=	Add(wgt)
		return wgt
	def Init(wgt):
		wgt=wgt['Gen']['Configure'](wgt)
		return wgt
	wgt=k.pop('widget')
	wgt['Lay']= QLib.Create.QLayout(**k)

	l			= Fnx(w)
	return Init(w)

def make(widget,**k):
	namestr=widget['name']
	preset=QDefaults.QLayout|{
		'widget'    :	widget	,	}
	k=Config.preset(['lay',namestr],preset,**k)
	return QLayout(**k)