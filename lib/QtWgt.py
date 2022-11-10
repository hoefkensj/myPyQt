#!/usr/bin/env python

from .gnr import sizePol, Mtds, Atrs, ArgKwargs,makeNames,Pfx2Qt,qwMtd

def QtWgt(**k):
	def Wgt():
		wgt= qwMtd(m=cfg('qt'))
		return wgt()

	def Arg(a,args={}):
		def defaults():
			d	=	{
			'm'   :	[0,0,0,0]	,
			'hPol':	'P'				,
			'vPol':	'P'				,
			}
			return d

		def readkwargs():
			arg=ArgKwargs(defaults=defaults(),**k)
			return arg

		args = args or readkwargs()
		return args(a)

	def Cfg():
		def names(n,names={}):
			names = names or makeNames(n=Arg('n'))
			return names[n]

		c={}
		c['pfx_name']			= names('pfx_name')
		c['pfx']					= names('pfx')
		c['name']					=	names('name')
		c['qt']						= Pfx2Qt(c['pfx'])
		c['hpol']					=	Arg('hPol')
		c['vpol']					=	Arg('vPol')
		c['sizepolicy']		=	sizePol(h=c['hpol']	, v=c['vpol']	)
		c['margin']				=	Arg('m')
		return c
	def cfg(a,c={}):
		c=c or Cfg()
		return c[a]

	def Mtd():
		wgt = w['Wgt']
		mtd=Mtds(wgt)
		return mtd

	def Atr():
		wgt = w['Wgt']
		atr=Atrs(wgt)
		return atr
	def Conn():
		c={}
		return c
	def Fnx():
		f={}
		return f
	def Init():
		C=w['Cfg']
		def init():
			w['Mtd']['setObjectName'](C['name'])
			w['Mtd']['setContentsMargins'](*C['margin'])
			w['Mtd']['setSizePolicy'](C['sizepolicy'])
		init()
		return {'Init' : Init}

	w= {}
	w['Wgt']			=	Wgt()
	w['Cfg']			= Cfg()
	w['Mtd']			=	Mtd()
	w['Atr']			= Atr()
	w['Con']			= Conn()
	w['Fnx']			=	Fnx()
	w['Init']			=	Init()
	return w

def make(n,**k):
	return {n : QtWgt(n=n,**k)}

