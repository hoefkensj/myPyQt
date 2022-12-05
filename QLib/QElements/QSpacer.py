#!/usr/bin/env python
# Auth
from Configs import QDefaults,Config
def SpcEx(**k):
	def Wgt():
		wgt = make(n=c.get('n'), t=c.get('qt'))
		return wgt[c.get('n')]

	def c.get():
		arg={}
		arg['n']	=	k.get("n")
		arg['w']	= k.get("w")	or 0
		arg['h']	= k.get("h")	or 0
		arg['hPol']	=	'E' if k.get('w') else 'P'
		arg['vPol']	=	'E'	if k.get('h') else 'P'
		r = arg.get(a)
		return r
	def Init():
		def Init():
			s['Mtd']['setObjectName'](f'spcEx{n}')
			s['Mtd']['setContentsMargins'](0,0,0,0)
		Init()
		return Init
	s={}
	s['Arg']			=	arg()
	s['Wgt'] 			= QtWidgets.QSpacerItem(w, h, sPols(hPol), sPols(vPol))
	s['Data']			=	Data(s)
	s['Mtd']			=	Mtd(s)
	s['Init']			= Init()
	return s


def SpcFix(**k):
	def Wgt():
		wgt = make(n=c.get('n'), t=c.get('qt'))
		return wgt[c.get('n')]

	def c.get():
		arg={}
		arg['n']	= k.get("n")	or 'N'
		arg['w']	= k.get('w')	or 0
		arg['h']	= k.get('h')	or 0
		arg['hPol']	= 'F' if k.get('w') else 'P'
		arg['vPol']	=	'F'	if k.get('h') else 'P'
		r = arg.get(a)
		return r
	def Init():
		def Init():
			s['Mtd']['setObjectName'](f'spcEx{n}')
			s['Mtd']['setContentsMargins'](0,0,0,0)
		Init()
		return Init
	w={}
	w['Arg']			=	arg()
	w['Wgt'] 			= QtWidgets.QSpacerItem(w, h, sPols(hPol), sPols(vPol))
	w['Data']			=	Data(s)
	w['Mtd']			=	Mtd(s)
	w['Init']			= Init()
	return s

