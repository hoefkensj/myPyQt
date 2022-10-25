#!/usr/bin/env python


from  PyQt5.QtWidgets import QWidget,QApplication
import gnr


def Wgt(**k):

	def Wgt():
		return QWidget()

	def Arg(a):
		arg={}
		arg['n']			= k.get("n")
		arg['t']			= k.get("t")
		arg['m']			=	k.get("m") or [0,0,0,0]
		arg['l']			=	k.get("l")
		r = arg.get(a)
		return r

	def Elements():
		e={}
		return e
	
	def Props():
		name 		= Arg('n')
		layout 	= gnr.Layouts(Arg('t'))
		return locals()

	def Mtd():
		wgt = w['Wgt']
		mtd=gnr.Mtd()
		return mtd(wgt)

	def Atr():
		wgt = w['Wgt']
		atr=gnr.Atr()
		return atr(wgt)

	def Lay():
		wgt=w['Wgt']
		l = Layout(w=wgt,**k) if Arg('t') else None
		return l

	def Fnx():
		def Add(i):
			w['Lay']['Add'](i['Wgt'])
			w['Elements'][i['Prp']['name']]= i
		f={}
		f['Add'] = Add
		return f
	
	def Init():
		def init():
			w['Mtd']['setObjectName'](f'wgt_{Arg("n")}')
			w['Mtd']['setContentsMargins'](*Arg('m'))

		init()
		return init

	w= {}
	w['Wgt']			=	Wgt()
	w['Elements']	= Elements()
	w['Prp']			= Props()
	w['Mtd']			=	Mtd()
	w['Atr']			= Atr()
	w['Lay']			= Lay()
	w['Fnx']			=	Fnx()
	w['Init']			=	Init()
	return w

def Layout(**k):
	def Arg(a):
		arg={}
		arg['n']			= k.get("n")
		arg['t']			= k.get("t")
		arg['m']			=	k.get("m") or [0,0,0,0]
		arg['l']			=	k.get("l")
		arg['w']			=	k.get("w")
		r = arg.get(a)
		return r
	def Lay():
		nlay=gnr.Layouts(Arg('t'))
		lay=nlay(Arg('w'))
		return lay
	def Props():
		name 		= Arg('n')
		layout 	= gnr.Layouts(Arg('t')).__name__
		return locals()

	def Mtd():
		wgt = l['Lay']
		mtd=gnr.Mtd()
		return mtd(wgt)

	def Atr():
		wgt = l['Lay']
		atr=gnr.Atr()
		return atr(wgt)

	def Add():
		return  l['Mtd']['addWidget']

	def Init():
		def init():
			l['Mtd']['setObjectName'](f'lay_{Arg("n")}')
			l['Mtd']['setContentsMargins'](*Arg('m'))
		init()
		return init

	l= {}
	l['Lay']			=	Lay()
	l['Prp']			= Props()
	l['Mtd']			=	Mtd()
	l['Atr']			= Atr()
	l['Add']			= Add()
	l['Init']			=	Init()
	return l

if __name__ == '__main__':
	import sys
	
	#
	# for k in GUI:
	# 	print(k)
	# 	if isinstance(GUI.get(k),dict):
	# 		for l in GUI.get(k):
	# 			print(l,GUI[k].get(l))
				# if isinstance(GUI[k].get(l),dict):
				# 	for m in GUI[k].get(l):
				# 		print(m,GUI[k][l])
