#!/usr/bin/env python
# Auth
from assets import ico
from lib import QtWgt
from lib import gnr
from lib import gnr
from lib import gnr
from lib import gnr
from lib import gnr
from lib import gnr
from lib import gnr
from lib import gnr

def QIconCheckBox(**k):
	def defaults(): return{
			'pfx'   :	'iBtn'				,
			'm'     :	[0,0,0,0]			,
			'pol'  :	'FP'					,
			'w'     :	20						,
			'h'     :	20						,
			'ico'   :	ico.get(k.get('name').split('_')[0])	,
			'icowh' :	[32,32]				,
			}

	def Create():
		w=dict()
		w['Name']			=	k['pfx_name']
		w['name']			=	k['name']
		w['Wgt']			=	QtWgt.make(**gnr.ArgKwargs(defaults,**k))
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
			**gnr.Icon(c.get('ico'),c.get('icowh')),
			}
		return c
	def Fnx():
		def toggle():
			state=w['Mtd']['isChecked']
			w['Mtd']['setChecked'](not state)
		f 					= {}
		f['Toggle']	= toggle
		return f
	def Init(w):
		c=w['Cfg']
		w['Set']['ObjectName'](c['Name'])
		w['Set']['SizePolicy'](c['SizePolicy'])
		w['Set']['Icon'](c['Icon'])
		w['Set']['IconSize'](c['IconSize'])
		w['Set']['Checkable'](c['Checkable'])
		w['Set']['MaximumSize'](c['MaximumSize'])

		return init
	def Conn():
		c={}
		c['clicked'] = w['Wgt'].clicked.connect
		c['clicked'](w['Mtd']['toggle'])
		return c

	w 					=			Wgt()
	w['Prp']		|=		Props()
	w['Mtd']		|=		Mtd()
	w['Atr']		|=		Atr()
	w['Fnx']		|=		Fnx()
	w['Con']		|=		Conn()
	w['Init']		= 		Init()
	return {w['Prp']['Name'] : w }