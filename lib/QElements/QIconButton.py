#!/usr/bin/env python
# Auth
import assets.ico
import lib.Create

from .. import QtWgt, gnr

def QIconButton(**k):
	def Create():
		wgt=k['QtFn']()
		w=lib.Create.QCreate(wgt,'Wgt',**k)
		return w
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
	w						= Create()
	w['Cfg']		=			Cfg()
	w['Fnx']		=			{}
	w['Con']		=			Con()
	return Init(w)


def make(namestr, **k):
	name=gnr.makeName(namestr)
	iconame=name.split('_')[0]
	k={
		'margin'    :	[0,0,0,0]					,
		'pol'     	:	'PP'						,
		'w'       	:	20							,
		'h'       	:	20							,
		'bi'     		:	False						,
		'ico'     	:	gnr.IconSet(iconame)	,
		'icowh'   	:	[32,32]					,
		'lbl'     	:	None						,
		}|k|{
		'pfx'     	:	'iBtn'					,
		'name'      :	name							,
		'pfx_name'  :	f'iBtn_{name}'			,
		}
	k|={'QtFn' : gnr.SubQWgt(k['pfx'])}
	return QIconButton(**k)