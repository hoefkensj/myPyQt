#!/usr/bin/env python
import lib.Create

from static.QtLibs import QElements,QLayouts
import lib.gnr


def QWgt(**k):
	def Cfg():
		c={
			'ObjectName'			:	w['Name'],
			'ContentsMargins'	: k['margin'],
			'SizePolicy'			:	lib.gnr.makeSizePolicy(k['pol']),
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
		f['Configure']	=	lib.gnr.Configure(wgt)
		f['Add']				=	Add(wgt)
		return f
	def Init(wgt):
		wgt=wgt['Fnx']['Configure']()
		return wgt
	w							=	lib.Create.QCreate(QElements['wgt'], **k)
	w['Elements'] = {}
	w['Cfg'] 			= Cfg()
	w['Lay']			= Lay(w)
	w['Fnx']			=	Fnx(w)
	return  Init(w)

def QLay(**k):
	def Lay():
		w	=	lib.Create.QCreateLay(QLayouts[k['t']](k['widget']['Wgt']), **k)

		return w
	def Cfg():
		c={
			'ObjectName'			:	w['Name'],
			'ContentsMargins'	: k['margin'],
			**k
			}
		return c
	def Fnx(wgt):
		def Add(wgt):
			def add(component):
				wgt['Mtd']['addWidget'](component)
			return add
		f={}
		f['Configure']	=	lib.gnr.Configure(wgt)
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
		'margin'		:	[0,0,0,0]					,
		'pol'				:	'E.E'							,
	} |	k	|	{
		'pfx'				:	'wgt'							,
		'name'			:	namestr						,
	}
	return QWgt(**k)
	
def make_Qlay(widget,**k):
	name=widget['name']
	k	=			{
		'margin'    :	[0,0,0,0]					,
		'layoutSpacing'	:	100							,
	}	|	k	|	{
		'pfx'				:	'lay'							,
		'name'			:	name							,
		'widget'		:	widget						,
	}
	return QLay(**k)

def make(namestr,**k):
	return make_QWgt(namestr,**k)