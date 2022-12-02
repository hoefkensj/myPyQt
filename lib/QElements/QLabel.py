#!/usr/bin/env python
import lib.Create

from Configs import QDefaults,Config
def QLabel(**k):

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
		mtd= lib.Create.Mtds(wgt)
		return mtd

	def Atr():
		wgt = w['Wgt']
		atr= lib.Create.Atrs(wgt)
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


# def Lbl(**k):
# 	def Wgt():
# 		wgt = make(n=c.get('n'), t=c.get('qt'))
# 		return wgt[c.get('n')]
#
# 	Mtd=     dClass('Mtds')('Wgt')
# 	def c.get():
# 		arg={}
# 		arg['n']				=	k.get('n')
# 		arg['w']				= k.get('w')	or 20
# 		arg['h']				= k.get('h')	or 20
# 		arg['m']				= k.get('m')	or [0,0,0,0]
# 		arg['ico']			=	k.get('ico')
# 		arg['lbl']			= k.get('lbl') or n
# 		r = arg.get(a)
# 		return r
# 	def Fnx():
# 		f 					= {}
# 		return f
# 	def Init():
# 		# l['Wgt'] 	=sPol(l['Wgt'] , h='P', v='P')
# 		def Init():
# 			l['Mtd']['setObjectName'](f'lbl_{n}')
# 			l['Mtd']['setText'](f'{lbl}')
# 			l['Mtd']['setContentsMargins'](*m)
# 		Init()
# 		return Init
# 	def Conn():
# 		c={}
# 		return c
#
# 	w={}
# 	w['Wgt'] 		= Wgt()
# 	w['Arg']		=	c.get()
# 	w['Mtd']		= Mtd(l)
# 	w['Data']		= None
# 	w['Fnx']		= Fnx()
# 	w['Conn']		=	Conn()
# 	w['Init']		= Init()
# 	return w




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