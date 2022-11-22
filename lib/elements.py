#!/usr/bin/env python


'''


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



def iBtn(**k):
	def Wgt():
		wgt = make(n=c.get('n'), t=c.get('qt'))
		return wgt[c.get('n')]

	def c.get():
		arg={}
		arg['n']				=	k.get("n")
		arg['w']				= k.get("w")	or 20
		arg['h']				= k.get("h")	or 20
		arg['bi']				= k.get('bi') or False
		arg['ico']			=	k.get('ico')
		arg['lbl']			= k.get('lbl')
		r = arg.get(a)
		return r
	def Fnx():
		f 					= {}
		return f
	def Init():
		F=w['Mtd']
		def Init():
			F['setObjectName'](f'iBtn{n}')
			F['setIcon'](Icon(n,ico=ico))
			F['setIconSize'](QtCore.QSize(32, 32))
			F['setCheckable'](bi)
			F['setMaximumSize'](QtCore.QSize(w, h))
			F['setToolButtonStyle'](QtCore.Qt.ToolButtonIconOnly)
			F['setMaximumHeight'](20)
		Init()
		return Init
	def Conn():
		c={}
		c['clicked'] = w['Wgt'].clicked.connect
		return c

	w={}
	w['Wgt'] 		= QtWidgets.QToolButton()
	w['Arg']		=	c.get()
	Mtd=     dClass('Mtds')('Wgt')
	w['Mtd']		= Mtd(b)
	w['Data']		=	Data(b)
	w['Fnx']		= Fnx()
	w['conn']		=	Conn()
	w['Init']		= Init()
	return b



def Lbl(**k):
	def Wgt():
		wgt = make(n=c.get('n'), t=c.get('qt'))
		return wgt[c.get('n')]

	Mtd=     dClass('Mtds')('Wgt')
	def c.get():
		arg={}
		arg['n']				=	k.get('n')
		arg['w']				= k.get('w')	or 20
		arg['h']				= k.get('h')	or 20
		arg['m']				= k.get('m')	or [0,0,0,0]
		arg['ico']			=	k.get('ico')
		arg['lbl']			= k.get('lbl') or n
		r = arg.get(a)
		return r
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

	w={}
	w['Wgt'] 		= Wgt()
	w['Arg']		=	c.get()
	w['Mtd']		= Mtd(l)
	w['Data']		= None
	w['Fnx']		= Fnx()
	w['Conn']		=	Conn()
	w['Init']		= Init()
	return w




'''