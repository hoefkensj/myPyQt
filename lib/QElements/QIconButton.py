#!/usr/bin/env python
# Auth

import lib.Create
from static.QtLibs import QElements,QToolButtons
import lib.gnr

def QIconButton(**k):
	def Cfg():
		c={
			'ObjectName'				:		w['Name'],
			'SizePolicy'				:		lib.gnr.makeSizePolicy(k['pol']),
			'Checkable'					:		k['bi'],
			'MaximumSize'				:		lib.gnr.makeSize(k['wh']),
			'ToolButtonStyle'		:		QToolButtons['I'],
			'ContentsMargins'		:		k['margin'],
			**lib.gnr.Icon(k['ico'], k['icowh'])
		}
		return c
	def Fnx(wgt):
		f={}
		f['Configure']	=	lib.gnr.Configure(wgt)
		return f
	def Con(wgt):
		c={}
		c['clicked'] = wgt['Mtd']['clicked'].connect
		return c
	def Init(wgt)     :
		wgt=wgt['Fnx']['Configure']()
		return wgt
	w						=			lib.Create.QCreate(QElements['iBtn'], **k)
	w['Cfg']		=			Cfg()
	w['Fnx']		=			Fnx(w)
	w['Con']		=			Con(w)
	return Init(w)

def make(namestr, **k):
	iconame=namestr.split('_')[0]
	k	= {
		'margin'    :	[0,20,100,0]							,
		'pol'       :	'P.P'									,
		'wh'        :	[20,20]								,
		'bi'        :	False									,
		'ico'       :	lib.gnr.IconSet(iconame)	,
		'icowh'     :	[32,32]								,
		'lbl'       :	None									,
	} |	k	|	{
		'name'      :	namestr								,
		'pfx'       :	'iBtn'								,
	}
	return QIconButton(**k)