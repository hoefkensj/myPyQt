#!/usr/bin/env python


'''
def Spcr(**k):
	def Wgt():
		wgt = make(n=c.get('n'), t=c.get('qt'))
		return wgt[c.get('n')]

	def c.get(a):
		arg={}
		arg['n']	= k.get("n")	or 'N'
		arg['w']	= k.get('w')	or 0
		arg['h']	= k.get('h')	or 0
		arg['p']	= k.get('p')	or 'E'


		if arg['p'] == 'F' :
			arg['hPol'],arg['vPol']	= 'F','F' if arg['w'] else 'P','P'
			arg['vPol']		=	'F'	if arg['h'] else 'P'
		else:
			arg['hPol']		=	'E' if arg['w'] else 'P'
			arg['vPol']		=	'E'	if arg['h']k.get('h') else 'P'
		r = arg.get(a)
		return r
	def Init():
		def Init():
			# s['Mtd']['setObjectName'](f'spcEx{n}')
			s['Mtd']['setContentsMargins'](0,0,0,0)
		Init()
		return Init
	w={}
	w['Arg']			=	c.get()
	# s['Wgt'] 			= QtWidgets.QSpacerItem(w, h, sPols(hPol), sPols(vPol))
	# s['Data']			=	Data(s)
	# s['Mtd']			=	Mtd(s)
	w['Init']			= Init()
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

def lEdit(**k):
	def Wgt():
		wgt = make(n=c.get('n'), t=c.get('qt'))
		return wgt[c.get('n')]

	def c.get():
		arg={}
		arg['n']				=	k.get('n')
		arg['w']				= k.get('w')	or 20
		arg['h']				= k.get('h')	or 20
		arg['ro']				= k.get('ro')	or False

		r = arg.get(a)
		return r
	def Fnx():
		f 					= {}
		f['Read']		=	l['Mtd']['text']
		f['Write']	=	l['Mtd']['setText']
		f['makeRO']			=	l['Mtd']['setReadOnly']
		f['RO']					=	l['Mtd']['isReadOnly']
		return f
	def Init():
		# l['Wgt'] 	=	sPol( l['Wgt'] , h='E', v='P')
		def Init():
			l['Mtd']['setObjectName'](f'txt{n}')
			l['Mtd']['setReadOnly'](ro)
		Init()
		return Init
	def Conn():
		c={}
		c['Entered']=l['Mtd']['returnPressed'].connect
		c['Changed']=l['Mtd']['textChanged'].connect
		c['Edited']=l['Mtd']['textEdited'].connect
		return c

	w={}
	w['Wgt'] 		= Wgt()
	w['Arg'] = c.get()
	Mtd=     dClass('Mtds')('Wgt')
	w['Mtd']		= Mtd(l)
	w['Data']		=	Data(l)
	w['Fnx']		= Fnx()
	w['Conn']		=	Conn()
	w['Init']		= Init()
	return l

def Tree(**k):
	def Wgt():
		wgt = make(n=c.get('n'), t=c.get('qt'))
		return wgt[c.get('n')]

	def c.get():
		arg={}
		arg['n']				= k.get('n') or 'Tree'
		arg['m']				= k.get('m') or [0,0,0,0]
		r = arg.get(a)
		return r
	def Fnx():
		f 					= {}
		f['setHeader']				= t['Mtd']['setHeader']
		f['addTopLevelItem']	=	t['Mtd']['addTopLevelItem']
		f['setColumnWidth']		=	t['Mtd']['setColumnWidth']
		f['setCurrentItem']		=	t['Mtd']['setCurrentItem']
		f['expandAll']				= t['Mtd']['expandAll']
		f['collapseAll']			= t['Mtd']['collapseAll']
		return f
	def Init():
		t['Wgt'] 	=	sPol(t['Wgt'], h='E', v='mE')
		def Init():
			t['Mtd']['setObjectName'](f'tree{n}')
			t['Mtd']['setAlternatingRowColors'](True)
			t['Mtd']['setAnimated'](True)
			t['Mtd']['setHeaderHidden'](True)
			t['Mtd']['setColumnCount'](5)
			t['Mtd']['hideColumn'](2)
			t['Mtd']['hideColumn'](3)
			t['Mtd']['hideColumn'](4)
			t['Mtd']['setMinimumHeight'](10)
			t['Mtd']['setAllColumnsShowFocus'](True)
			t['Mtd']['setMinimumHeight'](50)
			t['Mtd']['setContentsMargins'](*m)
			Init()
		return Init
	def Conn():
		c={}
		c['itemClicked']=t['Mtd']['itemClicked'].connect
		return c

	w={}
	w['Wgt'] 		= Wgt()
	w['Arg']		=	c.get()
	w['Mtd']		= Mtd(t)
	w['Data']		=	Data(t)
	w['Fnx']		= Fnx()
	w['Conn']		=	Conn()
	w['Init']		= Init()
	return t

'''