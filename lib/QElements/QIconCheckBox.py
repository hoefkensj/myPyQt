#!/usr/bin/env python
# Auth
import lib.Create
from assets import ico
from lib import QtWgt
from lib import gnr


def QIconCheckBox(**k):

	def Create():
		w=dict()
		w['Name']			=	k['pfx_name']
		w['name']			=	k['name']
		w['Wgt']			=	QtWgt.make(**gnr.ArgKwargs(defaults,**k))
		w['Mtd']			=	lib.Create.Mtds(w['Wgt'])
		w['Atr']			= lib.Create.Atrs(w['Wgt'])
		w							|= lib.Create.SetMtds(w)
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

	def Conn():
		c={}
		c['clicked'] = w['Wgt'].clicked.connect
		c['clicked'](w['Mtd']['toggle'])
		return c

	w 					=			lib.Create.QtCreate(QtWgt.make, **k)
	w['Cfg']		=			Cfg()
	w['Fnx']		=			{}
	w['Con']		=			Con()
	return Init(w)

def make(n, **k):
	def defaults(): return		{
			'pfx'     :	'chk'						,
			'margin'  :	[0,0,0,0]				,
			'pol'     :	'FP'						,
			'icowh'   :	[32,32]					,
			'ico'     :	gnr.IconSet(n)	,
			'lbl'     :	None						,
					}
	k|=gnr.ArgKwargs(defaults,**k)
	k|=gnr.makeNames(**k)
	return QIconCheckBox(**k)