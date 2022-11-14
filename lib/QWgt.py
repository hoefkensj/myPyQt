#!/usr/bin/env python


from .PyQtX import QWidget
from . import gnr


def QWgt(**k):
	def Arg(a,args={}):
		d	=	{
			'm'   :	[0,0,0,0]	,
			'pfx' :	'wgt'			,
			't'   :	None			,
			'hPol':	'E'				,
			'vPol':	'E'				,
			}
		args= args or d|k
		return args[a]
	def Cfg():
		c={}
		c['pfx_name']			= Arg('pfx_name')
		c['pfx']					= Arg('pfx')
		c['name']					=	Arg('name')
		c['hpol']					=	Arg('hPol')
		c['vpol']					=	Arg('vPol')
		c['sizepolicy']		=	gnr.sizePol(h=c['hpol'], v=c['vpol'])
		c['layouttype']		=	Arg('t')
		c['layout_name']	= gnr.Layouts(Arg('t')),
		c['margin']				=	Arg('m')
		return c
	def Lay():
		l = make_Qlay(w['Wgt'],**k) if Arg('t') else None
		return l
	def Fnx():
		def Add(i):
			try:
				w['Lay']['Add'](i['Wgt'])
				w['Elements'][i['Name']]=i
			except KeyError:
				print(i)

		f={}
		f['Add'] = Add
		return f
	def Init():
		setMtd=gnr.SetMtd(w)
		C=w['Cfg']
		def init():
			setMtd('ObjectName', w['Name'])
			setMtd('ContentsMargins', *C['margin'])
			setMtd('SizePolicy', C['sizepolicy'])
		init()
		return init
	w= {}
	w['Name']			=	Arg('pfx_name')
	w['Wgt']			=	QWidget()
	w['Cfg']			= Cfg()
	w['Mtd']			=	gnr.Mtds(w['Wgt'])
	w['Atr']			= gnr.Atrs(w['Wgt'])
	w['Elements']	=	{}
	w['Lay']			= Lay()
	w['Fnx']			=	Fnx()
	w['Init']			=	Init()
	return  w

def QLay(**k):
	def Arg(a,args={}):
		d = {
			'm'   : [0, 0, 0, 0],
			'pfx' : 'lay'	,
			'hPol': 'E'				,
			'vPol': 'E'				,
		}
		args = args or gnr.ArgKwargs(defaults=d, **k)
		return args(a)
	def Lay():
		nlay=gnr.Layouts(Arg('t'))['layout']
		lay=nlay(Arg('w'))
		return lay
	def Cfg():
		c={}
		c['widget']				=	Arg('w')
		c['pfx_name']			= Arg('pfx_name')
		c['pfx']					= Arg('pfx')
		c['name']					=	Arg('name')
		c['hpol']					=	Arg('hPol')
		c['vpol']					=	Arg('vPol')
		c['sizepolicy']		=	gnr.sizePol(h=c['hpol'], v=c['vpol'])
		c['layouttype']		=	Arg('t')
		c['layout_name']	= gnr.Layouts(c['layouttype'])['name'],
		c['layout']				= gnr.Layouts(c['layouttype'])['layout'],
		c['margin']				=	Arg('m')
		return c
	def Add():
		return  l['Mtd']['addWidget']
	def Init():
		setMtd=gnr.SetMtd(l)
		C=l['Cfg']
		def init():
			setMtd('ObjectName', l['Name'])
			setMtd('ContentsMargins', *C['margin'])
		init()
		return init


	l= {}
	l['Name']			=	Arg('pfx_name')
	l['Lay']			=	Lay()
	l['Cfg']			= Cfg()
	l['Mtd']			=	gnr.Mtds(l['Lay'])
	l['Atr']			= gnr.Atrs(l['Lay'])
	l['Add']			= Add()
	l['Init']			=	Init()
	return l

def make_QWgt(name,pfx='wgt',**k):
	Names=gnr.makeNames(name=name, pfx=pfx)
	kwargs={
	'pfx_name'  :	Names['pfx_name'],
	'pfx'       :	Names['pfx'],
	'name'      :	Names['name'],
	'qt'        : gnr.PfxMap(pfx),}
	qwgt 		=	QWgt(**kwargs,**k)
	return qwgt
	
def make_Qlay(widget,**k):
	k.pop('pfx')
	pfx='lay'
	name=k.pop('name')
	wgt_name=k.pop('pfx_name')
	Names=gnr.makeNames(name=name, pfx=pfx)
	kwargs={
	'pfx_name'  :	Names['pfx_name'],
	'pfx'       :	Names['pfx'],
	'name'      :	Names['name'],
	'w'         : widget,}
	qlay 		=	QLay(**kwargs,**k)
	return qlay

def make(name,**k):
	return make_QWgt(name,**k)