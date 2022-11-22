#!/usr/bin/env python
#def lEdit(**k):
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