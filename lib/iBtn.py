#!/usr/bin/env python
from PyQt5 import QtCore
from gnr import qwMtd,Icon,Mtds,Atrs,Layouts
from QtWgt import make

def iBtn(**k):
	def Wgt():
		wgt = make(n=(Arg("n")), t='tBtn')
		return wgt[Arg("n")]

	def Arg(a):
		arg={}
		arg['n']				=	k.get("n")
		arg['w']				= k.get("w")	or 20
		arg['h']				= k.get("h")	or 20
		arg['bi']				= k.get('bi') or False
		arg['ico']			=	k.get('ico')
		arg['lbl']			= k.get('lbl')
		arg['m']				= k.get('m') or [0,0,0,0]
		arg['qt']				= 'tBtn'
		r = arg.get(a)
		return r

	def Props():
		p={
			'Name' 		: f'iBtn_{Arg("n")}',
			}
		return p

	def Mtd():
		wgt = w['Wgt']
		mtd=Mtds(wgt)
		return mtd

	def Atr():
		wgt = w['Wgt']
		atr=Atrs(wgt)
		return atr

	def Fnx():
		f 					= {}
		return f

	def Init():
		def Init():
			w['Mtd']['setObjectName'](f'iBtn_{Arg("n")}')
			w['Mtd']['setIcon'](Icon(n=Arg("n"),ico=Arg("ico")))
			w['Mtd']['setIconSize'](QtCore.QSize(32, 32))
			w['Mtd']['setCheckable'](Arg("bi"))
			w['Mtd']['setMaximumSize'](QtCore.QSize(Arg("w"), Arg("h")))
			w['Mtd']['setToolButtonStyle'](QtCore.Qt.ToolButtonIconOnly)
			w['Mtd']['setMaximumHeight'](20)
		Init()
		return Init

	def Conn():
		c={}
		c['clicked'] = w['Mtd']['clicked']
		return c

	w={}
	w 					|=		Wgt()
	w['Prp']		|=		Props()
	w['Mtd']		|=		Mtd()
	w['Atr']		|=		Atr()
	w['Fnx']		|=		Fnx()
	w['con']		|=		Conn()
	w['Init']		= 		Init()
	return {w['Prp']['Name'] : w}
