#!/usr/bin/env python
import lib.Create

from .PyQtX import QWidget
from . import gnr


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
	def Lay(w):
		if k.get('t'):
			l= make_Qlay(w,**k) 
		else:
			l= None
		return l
	def Fnx(w):
		return w
	def Init(wgt):
		return wgt
	w=Create()
	w['Cfg'] 			= Cfg()
	w['Lay']			= Lay(w)
	w['Fnx']			=	Fnx(w)
	w['Elements'] = {}
	return  Init(w)

def QLay(**k):
	def Create():
		lay=k['layout']()
		l=lib.Create.QCreate(lay,'Lay',**k)
		return l
	def Cfg():
		c={
			'ObjectName'			:	k['pfx_name'],
			'ContentsMargins'	: k['margin'],
			}
		return c
	def Fnx(l):
		return l
	def Init(wgt):
		return wgt

		return f
	l							= Create()
	l['Cfg']			= Cfg()
	l['Fnx']			= Fnx(l)

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

def make(namestr,**k):
	return make_QWgt(namestr,**k)