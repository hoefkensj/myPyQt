#!/usr/bin/env python
import Fnx.make
import QLib.Create

from static.QtLibs import QElements,QLayouts
import QLib.gnr
from Configs import QDefaults

def QWgt(**k):
	def Cfg():
		c={
			'ObjectName'      :	w['Name'],
			'ContentsMargins' : k['margin'],
			'SizePolicy'      :	Fnx.make.SizePolicy(k['pol']),
			**k
			}
		return c
	def Lay(wgt):
		if k.get('t'):
			return make_Qlay(wgt,**k)
	def Fnx(wgt):
		def Add(wgt):
			def add(component):
				wgt['Lay']['Fnx']['Add'](component)
			return add
		f={}
		f['Configure']	=	QLib.Create.Configure(wgt)
		f['Add'] = Add(wgt)
		return f
	def Init(wgt):
		wgt=wgt['Fnx']['Configure']()
		return wgt
	w							=	QLib.Create.QCreate(QElements['wgt'], **k)
	w['Elements'] = {}
	w['Cfg'] 			= Cfg()
	w['Lay']			= Lay(w)
	w['Fnx']			=	Fnx(w)
	return  Init(w)

def QLay(**k):
	def Lay():
		w	=	QLib.Create.QCreateLay(QLayouts[k['t']](k['widget']['Wgt']), **k)

		return w
	def Cfg():
		c={
			'ObjectName'      :	w['Name'],
			'ContentsMargins' : k['margin'],
			**k
			}
		return c
	def Fnx(wgt):
		def Add(wgt):
			def add(component):
				wgt['Fnx']['Mtd']['addWidget'](component)
			return add
		f={}
		f['Configure']	= QLib.Create.Configure(wgt)
		f['Add']	=	Add(wgt)
		return f
	def Init(wgt):
		wgt=wgt['Fnx']['Configure']()
		return wgt
	w							=	Lay()
	w['Cfg']			= Cfg()
	w['Fnx']			= Fnx(w)
	return Init(w)

def make_QWgt(namestr,**k):
	k	=     {
		'margin'    :	[0,0,0,0]					,
		'pol'       :	'E.E'							,
	} |	k	|	{
		'pfx'       :	'wgt'							,
		'name'      :	namestr						,
	}
	return QWgt(**k)
	
def make_Qlay(widget,**k):
	name=widget['name']
	k	=     {
		**QDefaults.Properties					,
	} |	k	|	{
		'pfx'       :	'lay'							,
		'name'      :	name							,
		'widget'    :	widget						,
	}
	return QLay(**k)

def make(namestr,**k):
	return make_QWgt(namestr,**k)