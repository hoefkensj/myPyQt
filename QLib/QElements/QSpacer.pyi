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