#!/usr/bin/env python
import QLib.Create

from static.QtLibs import QElements,QLayouts
from QLib import gnr
from Configs import QDefaults,Config

def QLayout(**k):
	def Lay():
		return QLib.Create.QLayout(**k)
	def Fnx(wgt):
		def Add(wgt):
			def add(component):
				wgt['Fnx']['Mtd']['addWidget'](component)
			return add

		wgt	=	QLib.Create.Configure(wgt)
		wgt['Fnx']['Add']	=	Add(wgt)
		return wgt
	def Init(wgt):
		wgt=wgt['Fnx']['Configure'](wgt)
		return wgt
	w			=	Lay()
	w			=	Config.make(w,**k)
	w			= Fnx(w)
	return Init(w)

def make(widget,**k):
	name=widget['name']
	k	=     {
		**QDefaults.Properties					,
	} |	k	|	{
		'pfx'       :	'lay'							,
		'name'      :	name							,
		'widget'    :	widget						,
	}
	return QLayout(**k)