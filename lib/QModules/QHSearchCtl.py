#!/usr/bin/env python
# Auth
from ..QElements import QIconButton

from .. import gnr,QWgt
from . import QHArrows
def QHSearchCtl(**k):
	def defaults():return {
		'pfx'   :	'idw'				,
		'm'    :	[0,0,0,0]			,
		'hPol'  :	'F'						,
		'vPol'  :	'F'						,
		}
	def Create():
		Name=	k.get('pfx_name')
		name= k.get('name')
		w=QWgt.make(name,t='h',Pol='PP')
		w['Name']			= Name
		w['name']			=	name
		return w
	def Elements():
		e		= {}
		e|= gnr.sPack(QHArrows.make('PrevNext', bi=False))
		e|= QIconButton.make('Search', bi=False)
		return e
	def Fnx(): return {}
	def Con(e):
		c = {}
		c['iBtn_Search']=	e['iBtn_Search']['Mtd']['clicked'].connect
		c['iBtn_Prev']=e['wgt_PrevNext']['Con']['iBtn_Prev']
		c['iBtn_Next']=e['wgt_PrevNext']['Con']['iBtn_Next']
		return c
	def Init(w):
		for element in w['Elements']:
			w['Fnx']['Add'](w['Elements'][element])
		return w

	k 						= gnr.ArgKwargs(defaults,**k)
	w							=	Create()
	w['Elements'] = Elements()
	w['Fnx'] 			= Fnx()
	w['Con']			=	Con()
	return Init(w)


def make(name, pfx='wgt', **k):
	Names=gnr.makeNames(name=name,pfx=pfx)
	kwargs={
	'pfx_name'  :	Names['pfx_name'],
	'pfx'      :	Names['pfx'],
	'name'      :	Names['name'],
		'qt'        : gnr.PfxMap(pfx),}
	qtwgt 		=	QHSearchCtl(**kwargs, **k)
	return qtwgt