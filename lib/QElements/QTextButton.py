#!/usr/bin/env python
def tBtn(**k):
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
		arg['lbl']			= k.get('lbl') or k.get("n")
		r = arg.get(a)
		return r
	def Fnx():
		f 					= {}
		return f
	def Init():
		F=w['Mtd']
		def Init():
			F['setObjectName'](f'tBtn{n}')
			F['setText'](lbl)
			F['setCheckable'](bi)
			F['setMaximumSize'](QtCore.QSize(w, h))
			F['setToolButtonStyle'](QtCore.Qt.ToolButtonTextOnly)
			F['setMaximumHeight'](20)
		Init()
		return Init
	def Conn():
		c={}
		c['clicked'] = w['Wgt'].clicked.connect
		return c

	w={}
	w['Wgt'] 		= Wgt()
	w['Arg']		= c.get()
	Mtd=     dClass('Mtds')('Wgt')
	w['Mtd']		= Mtd(b)
	w['Data']		=	Data(b)
	w['Fnx']		= Fnx()
	w['Conn']		=	Conn()
	w['Init']		= Init()
	return b
