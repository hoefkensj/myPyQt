#!/usr/bin/env python
import lib.Create
from static.QtLibs import QElements,QToolButtons
import lib.gnr
def QtextButton(**k):
	def Cfg():
		c={
			'ObjectName'				:		w['Name'],
			'SizePolicy'				:		lib.gnr.makeSizePolicy(k['pol']),
			'Checkable'					:		k['bi'],
			'MaximumSize'				:		lib.gnr.makeSize(k['wh']),
			'MaximumHeight'			:		20,
			'ToolButtonStyle'		:		QToolButtons['T'],
			'ContentsMargins'		:		k['margin'],
			'Text'							:		w['name'].split('_')[0],

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
	w						=			lib.Create.QCreate(QElements['tBtn'], **k)
	w['Cfg']		=			Cfg()
	w['Fnx']		=			Fnx(w)
	w['Con']		=			Con(w)
	return Init(w)

def make(namestr, **k):
	k	= {
		'margin'    :	[0,0,0,0]							,
		'pol'       :	'P.P'									,
		'wh'        :	[20,20]								,
		'bi'        :	False									,
		'icowh'     :	[32,32]								,
		'lbl'       :	namestr									,
	} |	k	|	{
		'name'      :	namestr								,
		'pfx'       :	'iBtn'								,
	}
	return QtextButton(**k)