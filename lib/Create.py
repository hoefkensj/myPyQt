#!/usr/bin/env python
# Auth


def Mtds(wgt):
	wgt['Mtd']={}
	wgt['Atr']={}
	wgt['Set']={}
	wgt['Read']={}
	all=dir(wgt['Wgt'])
	for mtdn in all:
		mtd = getattr(wgt['Wgt'], mtdn)
		if callable(mtd):
			if mtdn.startswith('set'):
				mtdcn		=	mtdn[3:]
				mtdsn		=	f'{mtdcn[0].casefold()}{mtdcn[1:]}'
				mtdin		=	f'is{mtdcn}'
				if mtdin in all:
					wgt['Set'][mtdcn]		=	mtd
					wgt['Read'][mtdcn]	=	getattr(wgt['Wgt'], mtdin)
				elif mtdsn in all:
					wgt['Set'][mtdcn]		=	mtd
					wgt['Read'][mtdcn]	=	getattr(wgt['Wgt'], mtdsn)
				else:
					wgt['Mtd'][mtdn]		=	mtd
			else :
				wgt['Mtd'][mtdn]		=	mtd
		else:
			wgt['Atr'][mtdn]		=	mtd

	return wgt

def preCreate(pfx,name):
	w		=		{
		'Name'    :	f'{pfx}_{name}'			,
		'name'		:	name								,
		'type'		:	pfx									,
	}
	return w

def QCreate(wgt,**k):
	w					=	preCreate(k['pfx'],k['name'])
	w['Wgt']	=	wgt()
	return Mtds(w)
def QCreateLay(wgt,**k):
	w					=	preCreate(k['pfx'],k['name'])
	w['Wgt']	=	wgt
	return Mtds(w)

