#!/usr/bin/env python
# Auth
from ..QElements import QIconButton
from myPyQt.lib import QtWgt, gnr,QWgt


def QHArrows(**k):
	def defaults():return {
		'pfx'   :	'idw'				,
		'm'     :	[0,0,0,0]		,
		'pol'  :	'FF'				,
		't'			:	'h'					,
		}
	def Create(): return gnr.QtCreate(QWgt.make,defaults,**k)
	def Cfg():
		c=		gnr.ArgKwargs(defaults,**k)
		c|={
			'sizepolicy'    :	gnr.sizePol(c.get('pol')),
			'margin'        :	k.pop('m'),
		}
		def Optional():return {
			'maxw'          :	c.get('w'),
			'maxh'          : c.get('h'),
			'maxsize'       :	gnr.makeSize(c.get('w'),c.get('h')),
			}
		if c.get('w'):
			c|=Optional()
		return c
	def Elements():
		parent=w['name']
		e		= {}
		e|=gnr.Element(QIconButton.make(f'<_{parent}', h=15, w=15, bi=False))
		e|=gnr.Element(QIconButton.make(f'>_{parent}', h=15, w=15, bi=False))
		return e

	def Fnx(): return {}
	def Con():
		s=gnr.Short(w)
		c = {}
		c['iBtn_Prev']=	s['<']['Mtd']['clicked'].connect
		c['iBtn_Next']=	s['>']['Mtd']['clicked'].connect
		return c
	def Init(w):
		for element in w['Elements']:
			w['Wgt']['Add'](w['Elements'][element])
		s=gnr.Short(w)
		return w
	w							= Create()
	w['Elements'] = Elements()
	w['Fnx'] 			= 	Fnx()
	w['Con']			=	Con()
	return Init(w)

def make(name, pfx='wgt', **k):
	Names=gnr.makeNames(name=name,pfx=pfx)
	kwargs={
	'pfx_name'  :	Names['pfx_name'],
	'pfx'       :	Names['pfx'],
	'name'      :	Names['name'],
	'qt'        : gnr.PfxMap(pfx),}
	k|=kwargs
	return QHArrows(**k)