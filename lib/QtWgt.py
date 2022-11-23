#!/usr/bin/env python
import lib.Create

from . import gnr

def QtWgt(**k):
	def Create():
		wgt=k['QtFn']()
		w=lib.Create.QCreate(wgt,'Wgt',**k)
		return w
	def Fnx():
		def Configure():
			for prop in w['Cfg']:
				if prop == 'ContentsMargins':
					w['Set']['ContentsMargins'](*w['Cfg']['ContentsMargins'])
				else:
					if prop in w['Read'].keys():
						w['Set'][prop](w['Cfg'][prop])
		def Init(wgt):
			Configure()
			return wgt
		f={}
		f['Configure']=Configure
		return f
	w							=Create()
	w['Cfg']			= Cfg(**k)
	w['Con']			= {}
	w['Fnx']			= {}
	return w

def make(namestr,**k):
	name=gnr.makeName(namestr)
	pfx=gnr.makePfx(namestr)
	k={
		'margin'		:	[0,0,0,0]					,
		'pol'				:	'PP'							,
		}|k|{
		'pfx'				:	pfx								,
		'name'			:	name							,
		'pfx_name'	: f'{pfx}_{name}'			,
		}

	k|={'QtFn' : gnr.SubQWgt(k['pfx'])}
	return QtWgt(**k)
