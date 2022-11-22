#!/usr/bin/env python
# Auth
import lib.Create

from ..QElements import QIconButton
from .. import gnr,QWgt
from . import QHArrows

def QHSearchCtl(**k):
	def defaults():return {
		'pfx'   :	'wgt'				,
		'm'    :	[0,0,0,0]		,
		'pol'  :	'PF'				,
		}
	def Create(): return lib.Create.QtCreate(QWgt.make, defaults, **k)
	def Cfg():
		c=		gnr.ArgKwargs(defaults,**k)
		c|={
			'sizepolicy'    :	gnr.sizePol(c.get('pol')),
			'margin'        :	c.pop('m'),
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
		n=[f'PrevNext_{parent}',
    f'Search_{parent}']
		e		= {}
		e[n[0]]=QHArrows.make(n[0], bi=False)
		e[n[1]]=QIconButton.make(n[1], bi=False)
		return e
	def Short():
		parent=w['name']
		s={}
		s['<>']=w['Elements'][f'PrevNext_{parent}']
		# s['Srch']=w['Elements'][f'Search_{parent}']
		return s

	def Fnx(): return {}
	def Con():
		s=Short()
		c = {}
		# c['iBtn_Search']=	s['Srch']['Mtd']['clicked'].connect
		c['iBtn_Prev']=s['<>']['Con']['iBtn_Prev']
		c['iBtn_Next']=s['<>']['Con']['iBtn_Next']
		return c
	def Init(w):

		for element in w['Elements']:
			w['Add'](w['Elements'][element])
		return w

	w							=	Create()
	w['Cfg']			= Cfg()
	w['Elements'] = Elements()
	w['Fnx'] 			|= Fnx()
	w['Con']			|=	Con()
	return Init(w)


def make(name, pfx='wgt', **k):
	Names=gnr.makeNames(name=name,pfx=pfx)
	kwargs={
	'pfx_name'  :	Names['pfx_name'],
	'pfx'      :	Names['pfx'],
	'name'      :	Names['name'],
		'qt'        : gnr.PfxMap(pfx),}
	k|=kwargs
	return QHSearchCtl(**k)