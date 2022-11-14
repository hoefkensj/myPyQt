#!/usr/bin/env python


from .PyQtX import QWidget
from . import gnr


def QWgt(**k):
	def defaults():
		d	=	{
			'margin'		:	[0,0,0,0]	,
			'pfx'	:	'wgt'			,
			't'		:	None			,
			'hPol':	'E'				,
			'vPol':	'E'				,
		}
		return d
	def Cfg():
		c=k
		c['sizepolicy']		=	gnr.sizePol(h=c['hPol'], v=c['vPol'])
		c['layout_name']	= gnr.Layouts(k.get('t')),
		# c['size']					=	gnr.makeSize(k.get('w'),k.get('h')) if k.get('w' or 'h') else None
		return c
	def Lay():
		l = make_Qlay(w['Wgt'],**k) if k.get('t') else None
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
	def Init(w)     :
		setMtd=gnr.SetMtd(w)
		set=gnr.Set(w)
		conf={}
		conf['ObjectName']				=	w['Name']
		conf['SizePolicy']				=	w['Cfg']['sizepolicy']
		for prop in conf:
			 w['Cfg']	|=	setMtd(prop,conf[prop])
		set['ContentsMargin'](*w['Cfg']['margin'])
		return w
	k,Arg = gnr.ArgKwargs(defaults,**k)
	w= {}
	w['Name']			=	k.get('pfx_name')
	w['Wgt']			=	QWidget()
	w['Cfg']			= Cfg()
	w['Mtd']			=	gnr.Mtds(w['Wgt'])
	w['Atr']			= gnr.Atrs(w['Wgt'])
	w['Elements']	=	{}
	w['Lay']			= Lay()
	w['Fnx']			=	Fnx()
	w['Con']			= {}
	w			=	Init(w)
	return  w

def QLay(**k):
	def defaults():
		d = {
			'm'		: [0, 0, 0, 0],
			'pfx'	: 'lay'	,
			'hPol': 'E'				,
			'vPol': 'E'				,
		}
		return d


	def Lay():
		nlay=gnr.Layouts(k.get('t'))['layout']
		lay=nlay(k.get('w'))
		return lay
	def Cfg():
		c={}
		c['widget']				=	k.get('w')
		c['pfx_name']			= k.get('pfx_name')
		c['pfx']					= k.get('pfx')
		c['name']					=	k.get('name')
		c['hpol']					=	k.get('hPol')
		c['vpol']					=	k.get('vPol')
		c['sizepolicy']		=	gnr.sizePol(h=c['hpol'], v=c['vpol'])
		c['layouttype']		=	k.get('t')
		c['layout_name']	= gnr.Layouts(c['layouttype'])['name'],
		c['layout']				= gnr.Layouts(c['layouttype'])['layout'],
		c['margin']				=	k.get('m')
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

	k,Arg = gnr.ArgKwargs(defaults, **k)
	l= {}
	l['Name']			=	k.get('pfx_name')
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
	'pfx_name'	:	Names['pfx_name'],
	'pfx'				:	Names['pfx'],
	'name'			:	Names['name'],
	'qt'				: gnr.PfxMap(pfx),}
	qwgt 		=	QWgt(**kwargs,**k)
	return qwgt
	
def make_Qlay(widget,**k):
	k.pop('pfx')
	pfx='lay'
	name=k.pop('name')
	wgt_name=k.pop('pfx_name')
	Names=gnr.makeNames(name=name, pfx=pfx)
	kwargs={
	'pfx_name'	:	Names['pfx_name'],
	'pfx'				:	Names['pfx'],
	'name'			:	Names['name'],
	'w'					: widget,}
	qlay 		=	QLay(**kwargs,**k)
	return qlay

def make(name,**k):
	return make_QWgt(name,**k)