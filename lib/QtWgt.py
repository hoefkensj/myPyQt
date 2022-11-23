#!/usr/bin/env python
import lib.Create

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
		'Kwargs'	:	{**k},
		'QtConf'	:	QtConf,
		'QtPos'		:	Pos,
	}
	return C

def Init(w)     :
	def Configure():
			for QtProp in w['Cfg']['QtConf']:
				w['Set'][QtProp](w['Cfg']['QtConf'][QtProp])
			w['Set']['ContentsMargins'](*w['Cfg']['QtPos']['ContentsMargins'])

	Configure()

	return w

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
	return Init(w)

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
