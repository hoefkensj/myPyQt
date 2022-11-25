#!/usr/bin/env python
import lib.Create
from static.QtLibs import QElements
from . import gnr

def QtWgt(**k):
	def Cfg():
		if k.get('ctl'):
			k.pop('ctl')
		c={
			'ObjectName'			:	w['Name'],
			'ContentsMargins'	: k.pop('margin'),
			'SizePolicy'			:	lib.gnr.makeSizePolicy(k.pop('pol')),
			**k
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
	l=k.get('k') or {}
	k	=     {
		'margin'		:	[0,0,0,0]					,
		'pol'				:	'E.E'							,
	} |	l	|	k	|	{
		'name'			:	namestr						,
	}
	return QtWgt(**k)
