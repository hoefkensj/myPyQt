#!/usr/bin/env python
import lib.Create

from static.QtLibs import QElements,QLayouts
from lib import gnr
from Configs import QDefaults,Config

def QLayout(**k):
	def Lay():
		return lib.Create.QCreateLay(**k)
	def Fnx(wgt):
		def Add(wgt):
			def add(component):
				wgt['Fnx']['Mtd']['addWidget'](component)
			return add

		wgt	=	gnr.makeConfigure(wgt)
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