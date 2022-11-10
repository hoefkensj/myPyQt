#!/usr/bin/env python


from .PyQtX import QWidget
from .gnr import Layouts,Mtds,Atrs,ArgKwargs,makeNames,sizePol


def Wgt(**k):
	def Wgt():
		return QWidget()

	def Arg(a,args={}):
		def defaults():
			d	=	{
			'm'		:	[0,0,0,0]	,
			'pfx'	:	'wgt'			,
			'l'		:	None			,
			'hPol':	'E'				,
			'vPol':	'E'				,
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
		c['hpol']					=	Arg('hPol')
		c['vpol']					=	Arg('vPol')
		c['sizepolicy']		=	sizePol(h=c['hpol']	, v=c['vpol']	)
		c['layouttype']		=	Arg('t')
		c['layout']				=	Layouts(c['layouttype']).__name__,
		c['margin']				=	Arg('m')
		return c
	def cfg(a):
		cfg=w['Cfg']
		return cfg[a]


	def Elements():
		e={}
		return e

	def Mtd():
		wgt = w['Wgt']
		mtd=Mtds(wgt)
		return mtd

	def Atr():
		wgt = w['Wgt']
		atr=Atrs(wgt)
		return atr

	def Lay():
		wgt=w['Wgt']
		l = Layout(w=wgt,**k) if cfg('layouttype') else None
		return l

	def Fnx():
		def Add(i):
			w['Lay']['Mtd']['addWidget'](i['Wgt'])
			w['Elements'][i['Cfg']['name']]= i
		f={}
		f['Add'] = Add
		return f

	def Init():
		def init():
			w['Mtd']['setObjectName'](cfg('pfx_name'))
			w['Mtd']['setContentsMargins'](*cfg('margin'))
			w['Mtd']['setSizePolicy'](cfg('sizepolicy'))
		init()
		return init

	w= {}
	w['Wgt']			=	Wgt()
	w['Cfg']			= Cfg()
	w['Mtd']			=	Mtd()
	w['Atr']			= Atr()
	w['Lay']			= Lay()
	w['Fnx']			=	Fnx()
	w['Elements']	= Elements()
	w['Init']			=	Init()
	return w

def Layout(**k):
	def Arg(a,args={}):
		def defaults():
			d	=	{
			'm'		:	[0,0,0,0]	,
			'pfx'	:	'lay'			,
			'hPol':	'E'				,
			'vPol':	'E'				,
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
		c['widget']				=	Arg('w')
		c['pfx_name']			= names('pfx_name')
		c['pfx']					= names('pfx')
		c['name']					=	names('name')
		c['hpol']					=	Arg('hPol')
		c['vpol']					=	Arg('vPol')
		c['sizepolicy']		=	sizePol(h=c['hpol']	, v=c['vpol']	)
		c['layouttype']		=	Arg('t')
		c['layout']				=	Layouts(c['layouttype']).__name__,
		c['margin']				=	Arg('m')
		return c
	def cfg(a,cfg={}):
		cfg=cfg or Cfg()
		return cfg[a]

	def Lay():
		nlay=Layouts(Arg('t'))
		lay=nlay(cfg('widget'))
		return lay
	def Mtd():
		wgt = l['Lay']
		mtd=Mtds(wgt)
		return mtd
	def Atr():
		wgt = l['Lay']
		atr=Atrs(wgt)
		return atr
	def Add():
		return  l['Mtd']['addWidget']

	def Init():
		def init():
			l['Mtd']['setObjectName'](cfg('pfx_name'))
			l['Mtd']['setContentsMargins'](*cfg('margin'))
		init()
		return init

	l= {}
	l['Lay']			=	Lay()
	l['Cfg']			= Cfg()
	l['Mtd']			=	Mtd()
	l['Atr']			= Atr()
	l['Add']			= Add()
	l['Init']			=	Init()
	return l

if __name__ == '__main__':
	import sys
	
	#
	# for k in GUI:
	# 	print(k)
	# 	if isinstance(GUI.get(k),dict):
	# 		for l in GUI.get(k):
	# 			print(l,GUI[k].get(l))
				# if isinstance(GUI[k].get(l),dict):
				# 	for m in GUI[k].get(l):
				# 		print(m,GUI[k][l])
