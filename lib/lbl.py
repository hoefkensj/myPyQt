#!/usr/bin/env python
from  PyQt5.QtWidgets import QLabel
import gnr
def Lbl(**k):

	def Wgt():
		return QLabel()

	def Arg(a):
		arg={}
		arg['n']			= k.get("n")
		arg['m']			= k.get("m") or [0,0,0,0]
		r = arg.get(a)
		return r

	def Props():
		name 		= Arg('n')
		return locals()

	def Mtd():
		wgt = w['Wgt']
		mtd=gnr.Mtds(wgt)
		return mtd

	def Atr():
		wgt = w['Wgt']
		atr=gnr.Atrs(wgt)
		return atr

	def Fnx():
		f={}
		return f
	def Init():
		def init():
			w['Mtd']['setObjectName'](f'lbl_{Arg("n")}')
			w['Mtd']['setContentsMargins'](*Arg('m'))

		init()
		return init

	w= {}
	w['Wgt']			=	Wgt()
	w['Prp']			= Props()
	w['Mtd']			=	Mtd()
	w['Atr']			= Atr()
	w['Fnx']			=	Fnx()
	w['Init']			=	Init()
	return w







	def Lbl(**k):
    n,w,h,m,ico,lbl= [*[0] * 6]
		Mtd=     dClass('Mtds')('Wgt')
		def Arg():
			nonlocal n,w,h,ico,lbl,m
			n		=	k['n']				=	k.get('n')
			w		=	k['w']				= k.get('w')	or 20
			h		=	k['h']				= k.get('h')	or 20
			m		=	k['m']				= k.get('m')	or [0,0,0,0]
			ico	=	k['ico']			=	k.get('ico')
			lbl	=	k['lbl']			= k.get('lbl') or n
			return k
		def Fnx():
			f 					= {}
			return f
		def Init():
			# l['Wgt'] 	=sPol(l['Wgt'] , h='P', v='P')
			def Init():
				l['Mtd']['setObjectName'](f'lbl_{n}')
				l['Mtd']['setText'](f'{lbl}')
				l['Mtd']['setContentsMargins'](*m)
			Init()
			return Init
		def Conn():
			c={}
			return c

		l={}
		l['Wgt'] 		= QtWidgets.QLabel()
		l['Arg']		=	Arg()
		l['Mtd']		= Mtd(l)
		l['Data']		= None
		l['Fnx']		= Fnx()
		l['Conn']		=	Conn()
		l['Init']		= Init()
		return l