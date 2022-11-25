#!/usr/bin/env python
# Auth
import assets.ico
import lib.Create
from static.QtLibs import QElements,QToolButtons
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
			'SizePolicy'				:	lib.gnr.makeSizePolicy(k['pol']),
			'Checkable'         :		k['bi'],
			'MaximumSize'       :		gnr.makeSize([k['w'],k['h']]),
			'ToolButtonStyle'   :		QToolButtons['I'],
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
	w							=	lib.Create.QCreate(QElements[k['pfx']], **k)
	w['Cfg']		=			Cfg()
	w['Fnx']		=			{}
	w['Con']		=			Con()
	return Init(w)


def make(namestr, **k):

	iconame=namestr.split('_')[0]
	k={
		'margin'    :	[0,0,0,0]					,
		'pol'     	:	'P.P'						,
		'w'       	:	20							,
		'h'       	:	20							,
		'bi'     		:	False						,
		'ico'     	:	gnr.IconSet(iconame)	,
		'icowh'   	:	[32,32]					,
		'lbl'     	:	None						,
		}|k|{
		'pfx'     	:	'iBtn'					,
		'name'      :	namestr							,

		}
	return QIconButton(**k)