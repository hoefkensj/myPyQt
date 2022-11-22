#!/usr/bin/env python
import lib.Create

from . import gnr

def QtWgt(**k):

	def Create():
		w=dict()
		w['Name']			=	k['pfx_name']
		w['name']			=	k['name']
		w['Wgt']			=	gnr.SubQWgt(k['pfx'])
		w['Mtd']			=	lib.Create.Mtds(w['Wgt'])
		w['Atr']			= lib.Create.Atrs(w['Wgt'])
		w							|= lib.Create.SetMtds(w)
		return w
	def Cfg():
		c={
			'sizepolicy'    :	gnr.sizePol(k.get('pol')),
			'margin'        :	k.get('m'),
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
	def defaults(): return {
		'm'   :	[0,0,0,0]	,
		'pol':	'PP'			,
		}
	c={}
	c|=gnr.ArgKwargs(defaults,**k)
	c|=gnr.makeNames(pfx_name=n)
	print('pfx=',c['pfx'])
	c|={'qt'				: gnr.PfxMap(c['pfx']),}
	return QtWgt(**c)

