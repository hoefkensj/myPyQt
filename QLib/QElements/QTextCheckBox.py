#!/usr/bin/env python
def chkBox(**k):
	def Wgt():
		wgt = make(n=c.get('n'), t=c.get('qt'))
		return wgt[c.get('n')]

	wgt=None

	def c.get():
		arg={}
		arg['n']				=	k.get("n")
		arg['w']				= k.get("w")	or 20
		arg['h']				= k.get("h")	or 20
		arg['ico']			=	k.get('ico')
		arg['lbl']			= k.get('lbl')
		r = arg.get(a)
		return r
	def Mtd():
		Mtds(Wgt())

	def Fnx():
		def toggle():
			state=w['Mtd']['isChecked']
			w['Mtd']['setChecked'](not state)
		f 					= {}
		f['Toggle']	= toggle
		return f
	def Init():
		w['Wgt'] 	=	sPol( w['Wgt'] , h='P', v='P')
		def Init():
			w['Mtd']['setObjectName'](f'chk{n}')
			w['Mtd']['setIcon'](Icon(n,ico=ico))
			w['Mtd']['setIconSize'](QtCore.QSize(w-5, h-5))
			w['Mtd']['setMaximumSize'](QtCore.QSize(w*3, h))
		Init()
		return Init
	def Conn():
		c={}
		c['clicked'] = w['Wgt'].clicked.connect
		c['clicked'](w['Mtd']['toggle'])
		return c

	w={}
	w['Wgt'] 		= Wgt()
	w['Arg']		=	c.get()
	w['Mtd']		= Mtd(b)
	w['Data']		=	Data(b)
	w['Fnx']		= Fnx()
	w['Conn']		=	Conn()
	w['Init']		= Init()
	return b