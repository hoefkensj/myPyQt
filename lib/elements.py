#!/usr/bin/env python

from .PyQtX import QtCore
from . import gnr
from ..assets import ico

from . import QtWgt

def iBtn(**k):
	def Arg(a,args={}):
		d	=	{
			'pfx'   :	'iBtn'				,
			'm'     :	[0,0,0,0]			,
			'hPol'  :	'P'						,
			'vPol'  :	'P'						,
			'w'     :	20						,
			'h'     :	20						,
			'bi'    :	False					,
			'ico'   :	ico.get(k.get('name'))	,
			'icowh' :	[32,32]				,
			'lbl'   :	None					,
			}
		args= args or k|d
		return args[a]

	def Cfg():
		def sizing():
			c={}
			c['hpol']					=	Arg('hPol')
			c['vpol']					=	Arg('vPol')
			c['sizepolicy']		=	gnr.sizePol(h=c['hpol'], v=c['vpol'])
			c['maxw']					=	Arg('w')
			c['maxh']					= Arg('h')
			c['maxsize']			=	gnr.makeSize(c['maxw'],c['maxh'])
			c['margin']				=	Arg('m')
			return c
		c		=		{}
		c['pfx_name']=	Arg('pfx_name')
		c		|=	gnr.Icon(Arg('ico'),Arg('icowh'))
		c		|=	sizing()
		c['qt']						= gnr.PfxMap(Arg('pfx'))
		c['checkable']		= Arg('bi')
		c['btnstyle']			=	gnr.tBtnStyles('I')
		return c

	def Init()     :
		setMtd=gnr.SetMtd(w)
		def init():
			C=w['Cfg']
			C|=setMtd('ObjectName', w['Name'])
			C|=setMtd('SizePolicy', C['sizepolicy'])
			C|=setMtd('Icon', C['icon'])
			C|=setMtd('IconSize', C['iconsize'])
			C|=setMtd('Checkable', C['checkable'])
			C|=setMtd('MaximumSize', C['maxsize'])
			C|=setMtd('ToolButtonStyle', C['btnstyle'])
		init()
		return init
	def Conn():
		c={}
		c['clicked'] = w['Mtd']['clicked']
		return c


	w={}
	w						|=		gnr.unPack(QtWgt.make(Arg('pfx_name')))
	w['Name']		=			Arg('pfx_name')
	w['Cfg']		|=		Cfg()
	w		|=		gnr.Mtds(w['Wgt'])
	w		|=		gnr.Atrs(w['Wgt'])
	w['Fnx']		|=		{}
	w['Con']		|=		Conn()
	w['Init']		= 		Init()
	return gnr.Pack(w)

def make_iBtn(*a,**k):
	pfx		=	'iBtn'
	name=a[0]
	Names=gnr.makeNames(name=name,pfx=pfx)
	kwargs={
	'pfx_name'  :	Names['pfx_name'],
	'pfx'       :	Names['pfx'],
	'name'      :	Names['name'],}
	ibtn 		=	iBtn(**kwargs,**k)
	return gnr.rePack(ibtn)

def chkBox(**k):
	def Wgt():
		n=Arg('pfx_name')
		wgt = QtWgt.make(n=n)
		return wgt[n]
	def Arg(a,Args={}):
		def read():
			arg={}
			arg['w']				= k.get("w")	or 20
			arg['h']				= k.get("h")	or 20
			arg['ico']			= k.get('ico') or ico.get(arg['name'])
			arg['lbl']			= k.get('lbl')
			arg['m']				= k.get('m') or [0,0,0,0]

			arg['bi']				= k.get('bi') 		or False
			arg['icowh']		= k.get('icowh')	or [32, 32]
			return arg
		if not Args:	Args= read()
		r = Args.get(a)
		return r
	def Props():
		P={
		'Name'              : 	Arg('pfx_name'),
		'b64Svg'            :		Arg('ico'),
		'Icon'              :		gnr.Icon(Arg('ico'))	,
		'IconSizes'         :		Arg('icowh'),
		'IconSize'          :		QtCore.QSize(*Arg('icowh')),
		'Checkable'         :		Arg('bi'),
		'MaximumSizes'      :		[Arg('w'), Arg('h')],
		'MaximumSize'       :		QtCore.QSize(Arg('w'), Arg('h')),
		'SizePolicy'        :		gnr.sizePol(h='P', v='P'),
			}
		return P
	def Mtd():
		wgt = w['Wgt']
		mtd=gnr.Mtds(wgt)
		return mtd
	def Atr():
		wgt = w['Wgt']
		atr=gnr.Atrs(wgt)
		return atr
	def Fnx():
		def toggle():
			state=w['Mtd']['isChecked']
			w['Mtd']['setChecked'](not state)
		f 					= {}
		f['Toggle']	= toggle
		return f
	def Init():
		P=w['Prp']
		M=w['Mtd']
		def init():
			M['setObjectName'](P['Name'])
			M['setSizePolicy'](P['SizePolicy'])
			M['setIcon'](P['Icon'])
			M['setIconSize'](P['IconSize'])
			M['setCheckable'](P['Checkable'])
			M['setMaximumSize'](P['MaximumSize'])
		init()
		return init
	def Conn():
		c={}
		c['clicked'] = w['Wgt'].clicked.connect
		c['clicked'](w['Mtd']['toggle'])
		return c

	w 					=			Wgt()
	w['Prp']		|=		Props()
	w['Mtd']		|=		Mtd()
	w['Atr']		|=		Atr()
	w['Fnx']		|=		Fnx()
	w['Con']		|=		Conn()
	w['Init']		= 		Init()
	return {w['Prp']['Name'] : w }




'''	  
def Spcr(**k):
	def Wgt():
		wgt = make(n=Arg('n'), t=Arg('qt'))
		return wgt[Arg('n')]

	def Arg(a):
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
	w['Arg']			=	Arg()
	# s['Wgt'] 			= QtWidgets.QSpacerItem(w, h, sPols(hPol), sPols(vPol))
	# s['Data']			=	Data(s)
	# s['Mtd']			=	Mtd(s)
	w['Init']			= Init()
	return s

def SpcFix(**k):
	def Wgt():
		wgt = make(n=Arg('n'), t=Arg('qt'))
		return wgt[Arg('n')]

	def Arg():
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
		wgt = make(n=Arg('n'), t=Arg('qt'))
		return wgt[Arg('n')]

	def Arg():
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
		wgt = make(n=Arg('n'), t=Arg('qt'))
		return wgt[Arg('n')]

	wgt=None

	def Arg():
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
	w['Arg']		=	Arg()
	w['Mtd']		= Mtd(b)
	w['Data']		=	Data(b)
	w['Fnx']		= Fnx()
	w['Conn']		=	Conn()
	w['Init']		= Init()
	return b

def iBtn(**k):
	def Wgt():
		wgt = make(n=Arg('n'), t=Arg('qt'))
		return wgt[Arg('n')]

	def Arg():
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
	w['Arg']		=	Arg()
	Mtd=     dClass('Mtds')('Wgt')
	w['Mtd']		= Mtd(b)
	w['Data']		=	Data(b)
	w['Fnx']		= Fnx()
	w['conn']		=	Conn()
	w['Init']		= Init()
	return b

def tBtn(**k):
	def Wgt():
		wgt = make(n=Arg('n'), t=Arg('qt'))
		return wgt[Arg('n')]

	def Arg():
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
	w['Arg']		= Arg()
	Mtd=     dClass('Mtds')('Wgt')
	w['Mtd']		= Mtd(b)
	w['Data']		=	Data(b)
	w['Fnx']		= Fnx()
	w['Conn']		=	Conn()
	w['Init']		= Init()
	return b

def Lbl(**k):
	def Wgt():
		wgt = make(n=Arg('n'), t=Arg('qt'))
		return wgt[Arg('n')]

	Mtd=     dClass('Mtds')('Wgt')
	def Arg():
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
	w['Arg']		=	Arg()
	w['Mtd']		= Mtd(l)
	w['Data']		= None
	w['Fnx']		= Fnx()
	w['Conn']		=	Conn()
	w['Init']		= Init()
	return w

def lEdit(**k):
	def Wgt():
		wgt = make(n=Arg('n'), t=Arg('qt'))
		return wgt[Arg('n')]

	def Arg():
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
	w['Arg'] = Arg()
	Mtd=     dClass('Mtds')('Wgt')
	w['Mtd']		= Mtd(l)
	w['Data']		=	Data(l)
	w['Fnx']		= Fnx()
	w['Conn']		=	Conn()
	w['Init']		= Init()
	return l

def Tree(**k):
	def Wgt():
		wgt = make(n=Arg('n'), t=Arg('qt'))
		return wgt[Arg('n')]

	def Arg():
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
	w['Arg']		=	Arg()
	w['Mtd']		= Mtd(t)
	w['Data']		=	Data(t)
	w['Fnx']		= Fnx()
	w['Conn']		=	Conn()
	w['Init']		= Init()
	return t

'''