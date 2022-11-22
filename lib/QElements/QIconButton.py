#!/usr/bin/env python
# Auth
import assets.ico
import lib.Create

from .. import QtWgt, gnr

def QIconButton(**k):

	def Cfg():
		icons=gnr.Icon(k['ico'],k['icowh'])
		g={
			'maxw'              :		k['w'],
			'maxh'              : 	k['h'],
			'ContentsMargins'   :		k['margin'],
		}
		QtConf={
			'ObjectName'        :		w['Name'],
			'SizePolicy'        :		gnr.sizePol(k['pol']),
			'Checkable'         :		k['bi'],
			'MaximumSize'       :		gnr.makeSize(k['w'],k['h']),
			'ToolButtonStyle'   :		gnr.tBtnStyles('I'),
			**icons
		}

		c={
			'Config'  : k,
			'General' : g,
			'QtConf' : QtConf,
		}
		return c
	def Con():
		c={}
		c['clicked'] = w['Mtd']['clicked'].connect
		return c

	def Init(w)     :

		return w
	w = lib.Create.QtCreate(QtWgt.make, **k)
	w['Cfg']		=			Cfg()
	w['Fnx']		=			{}
	w['Con']		=			Con()
	return Init(w)


def make(n, **k):
	def defaults(): return	{
					'margin'  :	[0,0,0,0]				,
					'pol'     :	'PP'						,
					'w'       :	20							,
					'h'       :	20							,
					'bi'      :	False						,
					'ico'     :	gnr.IconSet(n)	,
					'icowh'   :	[32,32]					,
					'lbl'     :	None						,
					'pfx'     :	'iBtn'					,
					}
	k|=gnr.ArgKwargs(defaults,**k)
	k|=gnr.makeNames(**k)
	return QIconButton(**k)