#!/usr/bin/env python
import lib.Create

from ..QElements import QIconButton
from myPyQt.lib import QtWgt, gnr,elements
from myPyQt.lib import QWgt


def QHIncDec(**k):
	def defaults():return {
		'pfx'   :	'idw'				,
		'm'     :	[5,0,5,0]			,
		'pol'  :	'FF'					,
		'w'     :	20						,
		'h'     :	20						,
		'lbl'   :	None					,
		't'     : 'h',
		}


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
		n=[f'Inc_{parent}',
    f'Dec_{parent}'
    ]
		e		= {}
		e[n[0]]=QIconButton.make(n[0], h=15, w=15, bi=False)
		e[n[1]]=QIconButton.make(n[1], h=15, w=15, bi=False)
		return e
	def Short():
		parent=w['name']
		s={}
		s['inc']=w['Elements'][f'Inc_{parent}']
		s['dec']=w['Elements'][f'Dec_{parent}']
		return s
	def Fnx():
		s=Short()
		def StateInc():
			def stateinc(state):
				s['inc']['Set']['Enabled'](state)
			return stateinc
		def StateDec():
			def statedec(state):
				s['Dec']['Set']['Enabled'](state)
			return statedec
		def Show():
			def show(state):
				w['Wgt']['Set']['Visible'](state)
				return show
		f = {}
		f['Inc'] 		=	StateInc()
		f['Dec'] 		= StateDec()
		f['IncDec'] =	Show()
		return f

	def Con():
		s=Short()
		c = {}
		c['Inc']=	s['inc']['Mtd']['clicked'].connect
		c['Dec']=	s['dec']['Mtd']['clicked'].connect
		return c


	def Init(w):
		for element in w['Elements']:
			w['Fnx']['Add'](w['Elements'][element])
		s=Short()
		return w

	w = lib.Create.QtCreate(QWgt.make, defaults, **k)
	w							|=	{'Elements' : Elements()}
	w							|=	{'Cfg' 			: Cfg()}
	w['Fnx'] 			|=	Fnx()
	w['Con']			|=	Con()
	return Init(w)

def make(name,pfx='wgt',**k):
	Names=gnr.makeNames(name=name,pfx=pfx)
	kwargs={
	'pfx_name'  :	Names['pfx_name'],
	'pfx'       :	Names['pfx'],
	'name'      :	Names['name'],
	'qt'        : gnr.PfxMap(pfx),}
	k|=kwargs
	return QHIncDec(**k)