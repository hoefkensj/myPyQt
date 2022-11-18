#!/usr/bin/env python
import lib.QElements.QIconButton
from . import QtWgt, gnr
from . import elements
import sys
from . import QWgt


def QIncDec(**k):
	def defaults():return {
		'pfx'   :	'idw'				,
		'm'     :	[5,0,5,0]			,
		'hPol'  :	'F'						,
		'vPol'  :	'F'						,
		'w'     :	20						,
		'h'     :	20						,
		'lbl'   :	None					,
		'ed'    :	True,
		}
	def Elements():
		parent=w['Cfg']['name']
		add=w['Fnx']['Add']
		e = {}
		e |= lib.QElements.QIconButton.make(f'Inc_{parent}', h=15, w=15, bi=False)
		e |= lib.QElements.QIconButton.make(f'Dec_{parent}', h=15, w=15, bi=False)
		for element in e:
			add(e[element])
		return e

		return wgt
	def ShortMtds():
		parent=w['Cfg']['name']
		inc=w['Elements'][f'iBtn_Inc_{parent}']['Mtd']
		dec=w['Elements'][f'iBtn_Dec_{parent}']['Mtd']
		return inc,dec
	def Con():
    inc,dec=ShortMtds()
		c = {}
		c['iBtn_Inc']=	inc['clicked'].connect
		c['iBtn_Dec']=	dec['clicked'].connect
		return c
	def init(w):
    Inc,Dec=ShortMtds()
		return w
	def fnx():
    Inc,Dec=ShortMtds()
		def StateInc():
			def stateinc(state):
				Inc['setEnabled'](state)
			return stateinc
		def StateDec():
			def statedec(state):
				Dec['setEnabled'](state)
			return statedec
		def Show():
			def show(state):
				w['Wgt']['Mtd']['setVisible'](state)
				return show
		f = {}
		f['Inc'] 		=	StateInc()
		f['Dec'] 		= StateDec()
		f['IncDec'] =	Show()
		return f
  k,Arg = gnr.ArgKwargs(defaults,**k)
	w ={}
	w=	QWgt.make(k.get('name'),t='h',vPol='P',hPol='P')
	w['Name']			=	k.get('pfx_name')
	w['Elements'] = Elements()
	# w['Cfg']			= Cfg()
	w['Fnx'] 			|= fnx()
	w['Con']			|=	Con()
	w			=	init(w)

	return w

def make(name,pfx='wgt',**k):
	Names=gnr.makeNames(name=name,pfx=pfx)
	kwargs={
	'pfx_name'  :	Names['pfx_name'],
	'pfx'       :	Names['pfx'],
	'name'      :	Names['name'],
	'qt'        : gnr.PfxMap(pfx),}
	qtwgt				=QIncDec(**kwargs,**k)
	return qtwgt