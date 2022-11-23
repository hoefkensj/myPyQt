#!/usr/bin/env python
import lib.Create

from .PyQtX import QWidget
from . import gnr

#
# def Init(w)     :
# 	def Configure():
# 			for QtProp in w['Cfg']['QtConf']:
# 				w['Set'][QtProp](w['Cfg']['QtConf'][QtProp])
# 			w['Set']['ContentsMargins'](*w['Cfg']['QtPos']['ContentsMargins'])
# 	def readCfg():
# 			All = {}
# 			for key in w['Read']:
# 				if  key not in ['Property','Stretch']:
# 					All[key]=w['Read'][key]()
# 			return All
# 	Configure()
# 	w['Cfg']['All']=readCfg()
# 	return w

def QWgt(**k):
	def Create():
		wgt=lib.PyQtX.QWidget()
		w=lib.Create.QCreate(wgt,'Wgt',**k)
		return w
	def Cfg():
		c={
			'ObjectName'			:	k['pfx_name'],
			'ContentsMargins'	: k['margin'],
			}
		return c
	def Lay():
		if k.get('t'):
			l= make_Qlay(w,**k) 
		else:
			l= None
		return l
	def Fnx(w):
		def Generate():
			for element in w['Elements']:
				wgt=w['Elements'].get(element)
				w['Add'](wgt['Wgt'])
		def Configure():
			for prop in w['Cfg']:
				if prop == 'ContentsMargins':
					w['Set']['ContentsMargins'](*w['Cfg']['ContentsMargins'])
				else:
					if prop in w['Read'].keys():
						w['Set'][prop](w['Cfg'][prop])
		def Init(wgt):
			Configure()
			Generate()
			return wgt
		f={}
		f['Generate']= Generate
		f['Configure']=Configure
		f['Add']= w['Lay']['Add']
		f['Init']=Init
		return f
	w=Create()
	w['Cfg'] 			= Cfg()
	w['Lay']			= Lay()
	w['Fnx']			=	Fnx(w)
	w['Add']			= w['Fnx']['Add']
	w['Elements'] = {}
	w['Init']			=	w['Fnx']['Init']
	return  w['Init'](w)

def QLay(**k):
	def Create():
		lay=k['layout']()
		l=lib.Create.QCreate(lay,'lay',**k)
		return l
	def Cfg():
		c={
			'ObjectName'			:	k['pfx_name'],
			'ContentsMargins'	: k['margin'],
			}
		return c
	def Fnx(l):
		def Configure():
			for prop in l['Cfg']:
				if prop == 'ContentsMargins':
					l['Set']['ContentsMargins'](*l['Cfg']['ContentsMargins'])
				else:
					if prop in l['Read'].keys():
						l['Set'][prop](l['Cfg'][prop])

		def Init(wgt):
			Configure()
			return wgt
		f={}
		f['Add']= l['Mtd']['addWidget']
		f['Configure']= Configure
		f['Init']= Init
		return f
	l							= Create()
	l['Cfg']			= Cfg()
	l['Fnx']			= Fnx(l)
	l['Add']			= l['Fnx']['Add']
	return l

def make_QWgt(namestr,**k):
	name=gnr.makeName(namestr)
	k={
		'margin'    :	[0,0,0,0]					,
		'pol'       :	'EE'							,
		't'         :	'v'								,
		}|k|{
		'pfx'       :	'wgt'							,
		'name'      :	name							,
		'pfx_name'  :	f'wgt_{name}'			,
		}
	return QWgt(**k)
	
def make_Qlay(widget,**k):
	name=widget['name']
	layout=gnr.Layouts(k['t'])
	k={
		'margin'    :	[0,0,0,0]					,
		}|k|{
		'pfx'       :	'lay'							,
		'name'      :	name							,
		'pfx_name'  :	f'lay_{name}'			,
		'widget'		:	widget						,
		'layout'		:	layout						,
		}
	return QLay(**k)

def make(name,**k):
	return make_QWgt(name,**k)