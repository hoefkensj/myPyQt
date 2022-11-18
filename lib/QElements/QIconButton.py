#!/usr/bin/env python
# Auth
from ...assets import ico
from .. import QtWgt,gnr

def QIconButton(**k):
	def defaults(): return{
				'pfx'   :	'iBtn'				,
				'm'     :	[0,0,0,0]			,
				'pol'  :	'PP'					,
				'w'     :	20						,
				'h'     :	20						,
				'bi'    :	False					,
				'ico'   :	ico.get(k.get('name').split('_')[0])	,
				'icowh' :	[32,32]				,
				'lbl'   :	None					,
				}
	def Create():
		w=dict()
		w['Name']			=	k['pfx_name']
		w['name']			=	k['name']
		w['Wgt']			=	QtWgt.make(gnr.ArgKwargs(defaults,**k))
		w['Mtd']			=	gnr.Mtds(w['Wgt'])
		w['Atr']			= gnr.Atrs(w['Wgt'])
		w							|= gnr.SetMtds(w)
		return w

	def Cfg():
		c=gnr.ArgKwargs(defaults,**k)
		c|={
			'sizepolicy'    :	gnr.sizePol('Pol'),
			'maxw'          :	c.get('w'),
			'maxh'          : c.get('h'),
			'maxsize'       :	gnr.makeSize(c.get('w'),c.get('h')),
			'margin'        :	c.pop('m'),
			'checkable'     :	c.pop('bi'),
			'btnstyle'      :	gnr.tBtnStyles('I'),
			**gnr.Icon(c.get('ico'),c.get('icowh')),
		}
		return c

	def Init(w)     :
		setMtd=gnr.SetMtd(w)
		C=w['Cfg']
		w['Cfg']|=setMtd('ObjectName', w['Name'])
		w['Cfg']|=setMtd('SizePolicy', C['sizepolicy'])
		w['Cfg']|=setMtd('Icon', C['icon'])
		w['Cfg']|=setMtd('IconSize', C['iconsize'])
		w['Cfg']|=setMtd('Checkable', C['checkable'])
		w['Cfg']|=setMtd('MaximumSize', C['maxsize'])
		w['Cfg']|=setMtd('ToolButtonStyle', C['btnstyle'])
		return w

	def Conn():
		c={}
		c['clicked'] = w['Mtd']['clicked'].connect
		return c



	w						=			Create()
	w['Cfg']		=			Cfg()
	w['Fnx']		|=		{}
	w['Con']		|=		Conn()
	return Init(w)
def make(*a, **k):
	pfx		=	'iBtn'
	name=a[0]
	Names=gnr.makeNames(name=name,pfx=pfx)
	kwargs={
	'pfx_name'  :	Names['pfx_name'],
	'pfx'       :	Names['pfx'],
	'name'      :	Names['name'],}
	ibtn 		=	QIconButton(**kwargs, **k)
	return ibtn