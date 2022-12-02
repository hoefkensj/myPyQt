#!/usr/bin/env python
# Auth
import inspect
def isbound(m):
	return hasattr(m, '__self__')
def Mtds(wgt):
	wgt['Mtd']={}
	wgt['Mtd']['Wrappers']={}
	wgt['Atr']={}
	wgt['Set']={}
	wgt['Sig']={}
	wgt['Read']={}
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
					wgt['Set'][mtdcn]		=	mtd
					wgt['Read'][mtdcn]	=	getattr(wgt['Wgt'], mtdin)
				elif mtdsn in All:
					wgt['Set'][mtdcn]		=	mtd
					wgt['Read'][mtdcn]	=	getattr(wgt['Wgt'], mtdsn)
				else:
					wgt['Mtd'][mtdn]		=	mtd
			elif cls.__name__ == 'pyqtBoundSignal':
					wgt['Sig'][mtdn]=mtd
			elif cls.__name__== 'method-wrapper':
				wgt['Mtd']['Wrappers']=mtd
			else :
				wgt['Mtd'][mtdn]		=	mtd
		else:			wgt['Atr'][mtdn]		=	mtd

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
		Mtds(w)
	return w
def QCreateLay(wgt,**k):
	w					=	preCreate(k['pfx'],k['name'])
	w['Wgt']	=	wgt
	return Mtds(w)

