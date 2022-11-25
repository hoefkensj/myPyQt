#!/usr/bin/env python
import lib.Create
from static.QtLibs import QElements
from . import gnr

def QtWgt(**k):
	def Cfg():
		c={
			'ObjectName'			:	w['Name'],
			'ContentsMargins'	: k['margin'],
			'SizePolicy'			:	lib.gnr.makeSizePolicy(k['pol'])
			}
		return c
	def Fnx(wgt):
		f={}
		f['Configure']	=	lib.gnr.Configure(wgt)
		return f
	def Init(wgt):
		wgt=wgt['Fnx']['Configure']()
		return wgt
	w							=	lib.Create.QCreate(QElements[k['pfx']], **k)
	w['Cfg']			= Cfg()
	w['Con']			= {}
	w['Fnx']			= Fnx(w)
	return Init(w)

def make(namestr,**k):
	k	=     {
		'margin'		:	[0,0,0,0]					,
		'pol'				:	'E.E'							,
	} |	k	|	{
		'name'			:	namestr						,
	}
	return QtWgt(**k)
