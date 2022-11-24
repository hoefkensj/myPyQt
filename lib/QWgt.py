#!/usr/bin/env python
import lib.Create

from static.QtLibs import QElements,QLayouts
from . import gnr


def QWgt(**k):
	def Cfg():
		c={
			'ObjectName'			:	w['Name'],
			'ContentsMargins'	: k['margin'],
			'QSizePolicy'			:	gnr.makeSizePolicy(k['pol'])
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
		f['Configure']	=	gnr.Configure(wgt)
		f['Add']				=	Add(wgt)
		return f
	def Init(wgt):
		wgt=wgt['Fnx']['Configure']()
		# for prop in wgt['Cfg']:
		# 	wgt['Set'][prop](wgt['Cfg'][prop])
		return wgt
	w							=	lib.Create.QCreate(QElements['wgt'], **k)
	w['Elements'] = {}
	w['Cfg'] 			= Cfg()
	w['Lay']			= Lay(w)
	w['Fnx']			=	Fnx(w)
	return  Init(w)

def QLay(**k):
	def Lay():
		w	=	lib.Create.QCreate(QLayouts[k['t']], **k)
		w['Wgt'](k['widget'])
		return w
	def Cfg():
		c={
			'ObjectName'			:	w['Name'],
			'ContentsMargins'	: k['margin'],
			}
		return c
	def Fnx(wgt):
		def Add(wgt):
			def add(component):
				wgt['Mtd']['addWidget'](component['Wgt'])
			return add
		f={}
		f['Add']	=	Add(wgt)
		f['Configure'] = gnr.Configure(wgt)
		return f
	def Init(wgt):
		wgt=wgt['Fnx']['Configure']()
		return wgt
	w							=	Lay()
	w['Cfg']			= Cfg()
	w['Fnx']			= Fnx(w)
	return Init(w)

def make_QWgt(name,**k):
	k	=     {
		'margin'		:	[0,0,0,0]					,
		'pol'				:	'E.E'							,
	} |	k	|	{
		'pfx'				:	'wgt'							,
		'name'			:	name							,
	}
	return QWgt(**k)
	
def make_Qlay(widget,**k):
	name=widget['name']
	k	=			{
		'margin'    :	[0,0,0,0]					,
	}	|	k	|	{
		'pfx'				:	'lay'							,
		'name'			:	name							,
		'widget'		:	widget						,
	}
	return QLay(**k)

def make(namestr,**k):
	return make_QWgt(namestr,**k)