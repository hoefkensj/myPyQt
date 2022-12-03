#!/usr/bin/env python
# Auth
import inspect
def isbound(m):
	return hasattr(m, '__self__')
def Mtds(wgt):
	f = wgt.get('Fnx') or {}
	f['Mtd']=wgt.get('Mtd') or {}
	f['Mtd']['Wrappers']={}
	f['Atr']={}
	f['Set']={}
	f['Sig']={}
	f['Read']={}
	All=dir(wgt['Wgt'])
	for mtdn in All:
		mtd = getattr(wgt['Wgt'], mtdn)
		if callable(mtd):
			cls=getattr(mtd,'__class__')
			if mtdn.startswith('set'):
				mtdcn		=	mtdn[3:]
				mtdsn		=	f'{mtdcn[0].casefold()}{mtdcn[1:]}'
				mtdin		=	f'is{mtdcn}'
				if mtdin in All:
					f['Set'][mtdcn]		=	mtd
					f['Read'][mtdcn]	=	getattr(wgt['Wgt'], mtdin)
				elif mtdsn in All:
					f['Set'][mtdcn]		=	mtd
					f['Read'][mtdcn]	=	getattr(wgt['Wgt'], mtdsn)
				else:
					f['Mtd'][mtdn]		=	mtd
			elif cls.__name__ == 'pyqtBoundSignal':
					f['Sig'][mtdn]=mtd
			elif cls.__name__== 'method-wrapper':
				f['Mtd']['Wrappers'][mtdn]=mtd
			else :
				f['Mtd'][mtdn]		=	mtd
		else:
			f['Atr'][mtdn]		=	mtd
	wgt['Fnx']=f
	return wgt

def preCreate(pfx,name):
	w		=		{
		'Name'    :	f'{pfx}_{name}'			,
		'name'		:	name								,
		'type'		:	pfx									,
	}
	return w

def QCreate(*a,**k):
	w					=	preCreate(k['pfx'],k['name'])
	if a:
		w['Wgt']	=	a[0]()
		w=Mtds(w)
	return w
def QCreateLay(wgt,**k):
	w					=	preCreate(k['pfx'],k['name'])
	w['Wgt']	=	wgt
	return Mtds(w)

