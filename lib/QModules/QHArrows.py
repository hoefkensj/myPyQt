#!/usr/bin/env python
# Auth
import lib.QElements.QIconButton
from .. import QWgt
from .. import elements
from .. import gnr


def QHArrows(**k):
	def defaults():return {
		'pfx'   :	'idw'				,
		'm'     :	[0,0,0,0]			,
		'hPol'  :	'F'						,
		'vPol'  :	'F'						,
		}
	def Elements():
		parent=k.get('name')
		e		= {}
		e|= lib.QElements.QIconButton.make(f'Prev_{parent}', bi=False)
		e|= lib.QElements.QIconButton.make(f'Next_{parent}', bi=False)
		return e
	def ShortMtds():
		parent=k.get('name')
		Prev=w['Elements'][f'iBtn_Prev_{parent}']['Mtd']
		Next=w['Elements'][f'iBtn_Next_{parent}']['Mtd']
		return Prev,Next
	def Fnx(): return {}
	def Con():
    inc,dec=ShortMtds()
		c = {}
		c['iBtn_Prev']=	inc['clicked'].connect
		c['iBtn_Next']=	dec['clicked'].connect
		return c
	def Init(w):
		for element in w['Elements']:
			w['Fnx']['Add'](w['Elements'][element])
		return w

	k = gnr.ArgKwargs(defaults,**k)
	w ={}
	w	=	QWgt.make(k.get('name'),t='h',vPol='P',hPol='P')
	w['Name']			=	k.get('pfx_name')
	w['Elements'] = Elements()
	w['Fnx'] 			|= 	Fnx()
	w['Con']			|=	Con()
	return Init(w)

def make(name, pfx='wgt', **k):
	Names=gnr.makeNames(name=name,pfx=pfx)
	kwargs={
	'pfx_name'  :	Names['pfx_name'],
	'pfx'       :	Names['pfx'],
	'name'      :	Names['name'],
		'qt'        : gnr.PfxMap(pfx),}
	qtwgt 		=	QHArrows(**kwargs,**k)
	return qtwgt