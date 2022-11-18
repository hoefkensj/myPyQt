#!/usr/bin/env python

from . import gnr

def QtWgt(**k):
	def defaults():
		d	=	{
			'm'   :	[0,0,0,0]	,
			'hPol':	'P'				,
			'vPol':	'P'				,
			}
		return d
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
		c={
			'spol'          :	[c.get('hPol'),c.get('vPol')],
			'sizepolicy'    :	gnr.sizePol(h=c.get('hPol'), v=c.get('vPol')),
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

def make(*a,**k):
	if a:
		Names=gnr.makeNames(n=a[0])
	else :
		print('couldnt make names')
	pfx_name	=	Names['pfx_name']
	pfx				=	Names['pfx']
	name			=	Names['name']
	qt				= gnr.PfxMap(pfx)
	qtwgt 		=	QtWgt(pfx_name=pfx_name,pfx=pfx,name=name,qt=qt,**k)

	return qtwgt

