#!/usr/bin/env python

from . import gnr

def QtWgt(**k):
	def Arg(a,args={}):
		d	=	{
			'm'   :	[0,0,0,0]	,
			'hPol':	'P'				,
			'vPol':	'P'				,
			}
		args = args or gnr.ArgKwargs(defaults=d, **k)
		return args(a)
	def Cfg():
		c={
			'pfx_name'      : Arg('pfx_name'),
			'pfx'           : Arg('pfx'),
			'name'          :	Arg('name'),
			'qt'            : Arg('qt'),
			'spol'          :	[Arg('hPol'),Arg('vPol')],
			'sizepolicy'    :	gnr.sizePol(h=Arg('hPol'), v=Arg('vPol')),
			'margin'        :	Arg('m'),
		}
		return c
	def Init():
		setMtd=gnr.SetMtd(w)
		C=w['Cfg']
		def init():
			setMtd('ObjectName',C['pfx_name'])
			setMtd('ContentsMargins',*C['margin'])
			setMtd('SizePolicy',C['sizepolicy'])
		init()
		return Init

	w= {}
	w['Name']			= Arg('pfx_name')
	w['Wgt']			=	gnr.SubQWgt(Arg('pfx'))()
	w['Cfg']			= Cfg()
	w['Mtd']			=	gnr.Mtds(w['Wgt'])
	w['Atr']			= gnr.Atrs(w['Wgt'])
	w['Con']			= {}
	w['Fnx']			= {}
	w['Init']			=	Init()
	return gnr.Pack(w)

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

	return gnr.rePack(qtwgt)

