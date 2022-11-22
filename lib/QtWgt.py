#!/usr/bin/env python

from . import gnr

def QtWgt(**k):
	def defaults(): return {
			'm'   :	[0,0,0,0]	,
			'pol':	'PP'			,
			}
	def Create():
		w=dict()
		w['Name']			=	k['pfx_name']
		w['name']			=	k['name']
		w['Wgt']			=	gnr.SubQWgt(k['pfx'])
		w['Mtd']			=	gnr.Mtds(w['Wgt'])
		w['Atr']			= gnr.Atrs(w['Wgt'])
		w							|= gnr.SetMtds(w)
		return w
	def Cfg():
		c= gnr.ArgKwargs(defaults, **k)
		c|={
			'sizepolicy'    :	gnr.sizePol(c.get('pol')),
			'margin'        :	c.get('m'),
		}
		return c
	def Init(w)     :
		Set=w['Set'];Read=w['Read']
		conf = {}
		conf['ObjectName']				=	w['Name']
		conf['SizePolicy']				=	w['Cfg']['sizepolicy']
		for prop in conf:
			Set[prop](conf[prop])
			w['Cfg'][prop]=Read[prop]()
		Set['ContentsMargins'](*w['Cfg']['margin'])
		return w
	w							= Create()
	w['Cfg']			= Cfg()
	w['Con']			= {}
	w['Fnx']			= {}
	return Init(w)

def make(n,**k):
	k|=gnr.makeNames(n)
	k|={'qt'				: gnr.PfxMap(k['pfx']),}
	return QtWgt(**k)

