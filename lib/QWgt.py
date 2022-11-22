#!/usr/bin/env python
import lib.Create

from .PyQtX import QWidget
from . import gnr

def Cfg(**k):
	QtConf={
		'ObjectName': k['pfx_name'],
		'SizePolicy':	gnr.sizePol(k['pol']),
		}
	Pos={
		'ContentsMargins'	: k['margin']
		}
	C={
		'Kwargs' 	:	{**k},
		'QtConf'	:	QtConf,
		'QtPos'		:	Pos,
	}
	return C


def QWgt(**k):

	def Fnx():
		def Add():
			def add(i)
				w['Lay']['Fnx']['Add'](i['Wgt'])
				w['Elements'][i['Name']]=i

		f={}
		f['Add'] = Add
		return f
	def Init(w)     :
		Set=w['Set']
		Read=w['Read']
		conf = {}
		conf['ObjectName']				=	w['Name']
		conf['SizePolicy']				=	w['Cfg']['sizepolicy']
		for prop in conf:
			Set[prop](conf[prop])
			w['Cfg'][prop]=Read[prop]()
		Set['ContentsMargins'](*w['Cfg']['margin'])
		return w

	w							= lib.Create.QtCreate(QWidget, **k)
	w['Cfg']			= Cfg(**k)
	w['Elements']	=	{}
	w['Lay']			= make_Qlay(w,**k) if k.get('t') else None
	w['Fnx']			=	Fnx()
	w['Con']			= {}
	w['Add']			= w['Fnx']['Add']

	return  Init(w)

def QLay(**k):
	def Fnx():
		def Add():
			fnAdd=l['Mtd']['addWidget']
			def add(wgt):
				fnAdd(wgt)
			return add
		return {
		'Add' : Add(),
		}
	def Init(l):
		Cfg=l['Cfg']
		def Configure():
			Cfg=l['Cfg'];	Qt=Cfg['QtConf'];	Pos=Cfg['QtPos']
			for QtProp in Qt:
				l['Set'][QtProp](Qt[QtProp])
			l['Set']['ContentsMargins'](*Pos['ContentsMargins'])
		def readCfg():
			All={}
			for key in l['Read']:
				All[key]=l['Read'][key]()
			return All

		return l

	l							= lib.Create.QlCreate(k['layout'], **k)
	l['Cfg']			= Cfg(**k)
	l['Fnx']			= Fnx()
	l['Add']			= l['Fnx']['Add']
	return Init(l)

def make_QWgt(name,**k):
	def defaults():	return {
			'margin'    :	[0,0,0,0]	,
			't'         :	None			,
			'pol'       :	'EE'			,
		}
	k|={
		'pfx'       :	'wgt'					,
		'name'      :	name			,
		'pfx_name'  :	f'wgt_{name}'	,
		}
	k|=gnr.ArgKwargs(defaults,**k)
	return QWgt(**k)
	
def make_Qlay(widget,**k):
	name=widget['name']
	layout:gnr.Layouts(k['t'])
	k|={
		'pfx'       :	'lay'					,
		'name'      :	name			,
		'pfx_name'  :	f'lay_{name}'	,
		'widget'    :	widget				,
		'layout'    :	layout				,
		}

	return QLay(**k)

def make(n,**k):
	return make_QWgt(n,**k)