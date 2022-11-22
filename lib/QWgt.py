#!/usr/bin/env python


from .PyQtX import QWidget
from . import gnr

def QWgt(**k):
	def defaults():	return {
			'margin'    :	[0,0,0,0]	,
			't'   :	None			,
			'pol':	'EE'			,
		}
	def Create(): return gnr.QCreate(QWidget,defaults,**k)

	def Cfg():
		c=gnr.ArgKwargs(defaults,**k)
		pol=c.get('pol')
		if not pol:	pol=''.join(c.get('hPol'),c.get('vPol'))
		c['sizepolicy']		=	gnr.sizePol(pol)
		c['layout_name']	= gnr.Layouts(c.get('t')),
		# c['size']					=	gnr.makeSize(k.get('w'),k.get('h')) if k.get('w' or 'h') else None
		return c
	def Lay():
		l = make_Qlay(w,**w['Cfg']) if k.get('t') else None
		return l
	def Fnx():
		def Add(i):
			w['Lay']['Fnx']['Add'](i['Wgt'])
			w['Elements'][i['Name']]=i

		f={}
		f['Add'] = Add
		return f
	def Init(w)     :
		Set=w['Set']
		Read=w['Read']
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
	w['Elements']	=	{}
	w['Lay']			= Lay()
	w['Fnx']			=	Fnx()
	w['Con']			= {}
	w['Add']			= w['Fnx']['Add']

	return  Init(w)

def QLay(**k):
	def defaults():return  {
			'm'   : [0, 0, 0, 0],
			'pfx' : 'lay'	,
			'pol': 'EE'		,
		}
	def Create():
		nlay=gnr.Layouts(k.get('t'))
		l=dict()
		l['Lay']=nlay['layout'](k.get('w'))
		l['Name']			=	k.get('pfx_name')
		l['name']			=	k.get('name')
		l['Mtd']			=	gnr.Mtds(l['Lay'])
		l['Atr']			= gnr.Atrs(l['Lay'])
		l							|= gnr.SetMtds(l)
		return l
	def Cfg():
		c									=	gnr.ArgKwargs(defaults, **k)
		c['sizepolicy']		=	gnr.sizePol(c['pol'])
		c['layouttype']		=	c.get('t')

		layout						=	gnr.Layouts(c['layouttype'])
		c['layout_name']	= layout['name']
		c['layout']				=	layout['layout']
		c['margin']				=	c.pop('m')
		return c
	def Fnx():
		def Add():
			return  l['Mtd']['addWidget']
		f=dict()
		f['Add']=Add()
		return f
	def Init(l):
		Set=l['Set']
		Read=l['Read']
		conf = {}
		conf['ObjectName']				=	l['Name']
		for prop in conf:
			Set[prop](conf[prop])
			l['Cfg'][prop]=Read[prop]()
		Set['ContentsMargins'](*l['Cfg']['margin'])
		return l

	l							= Create()
	l['Cfg']			= Cfg()

	l['Fnx']			= Fnx()
	l['Add']			= l['Fnx']['Add']
	return Init(l)

def make_QWgt(n,**k):
	Names=gnr.makeNames(name=n, pfx='wgt')
	kwargs={
	'pfx_name'  :	Names['pfx_name'],
	'pfx'       :	Names['pfx'],
	'name'      :	Names['name'],
	'qt'        : gnr.PfxMap('wgt'),}
	k|=kwargs
	return QWgt(**k)
	
def make_Qlay(widget,**k):
	pfx='lay'
	name=widget['name']

	Names=gnr.makeNames(name=name, pfx=pfx)
	kwargs={
	'pfx_name'  :	Names['pfx_name'],
	'pfx'       :	Names['pfx'],
	'name'      :	Names['name'],
	'w'         : widget['Wgt'],}
	k|=kwargs
	return QLay(**k)

def make(n,**k):
	return make_QWgt(n,**k)