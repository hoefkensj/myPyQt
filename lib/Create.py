#!/usr/bin/env python
# Auth
import inspect
from static import QtLibs
import sys
from Configs import Config


def isbound(m):
	return hasattr(m, '__self__')
def Mtds(wgt):
	f = wgt.get('Fnx') or {}
	f['Mtd']=wgt.get('Mtd') or {}
	f['Mtd']['Wrappers']={}
	f['Atr']={}
	f['Set']={}
	f['Sig']={}
	f['Get']={}
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
					f['Get'][mtdcn]	=	getattr(wgt['Wgt'], mtdin)
				elif mtdsn in All:
					f['Set'][mtdcn]		=	mtd
					f['Get'][mtdcn]	=	getattr(wgt['Wgt'], mtdsn)
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

# def preCreate(pfx,name):
# 	w		=		{
# 		'Name'    :	f'{pfx}_{name}'			,
# 		'name'		:	name								,
# 		'type'		:	pfx									,
# 	}
# 	return w

# def QCreate(*a,**k):
# 	w					=	preCreate(k['pfx'],k['name'])
# 	if a:
# 		w['Wgt']	=	a[0]()
# 		w					=	Mtds(w)
# 	w	=		Config.make(w,**k)
# 	return w

# def QCreateApp(**k):
# 	w					=	preCreate(k['pfx'],k['name'])
# 	w['Wgt']	=	QtLibs.QElements['app'](sys.argv)
# 	w=Mtds(w)
# 	return w
#
# def QCreateLay(**k):
# 	wgt					=	k.pop('widget')
# 	layout			=	QtLibs.QLayouts[k['t']]
# 	l	=	preCreate(k['pfx'],k['name'])
# 	l['Wgt']		=	layout(wgt['Wgt'])
# 	l=Mtds(l)
# 	return l
#
#
def QCreate(fn):
	def Pre(**k):
		pfx			=	k['pfx']
		type		=	QtLibs.QElements.get(pfx).__name__ if QtLibs.QElements.get(pfx) else None
		name		=	k['name']
		w				=	{
			'Name'    :	f'{pfx}_{name}'			,
			'name'		:	name								,
			'type'		:	type								,}
		return w
	def create(*a,**k):
		w	=	Pre(**k)
		w	=	fn(w,*a,**k)
		w	=	Post(w,**k)
		return w
	def Post(wgt,**k):
		wgt = Config.make(wgt,**k)
		wgt['Lay']={}
		wgt	=	Mtds(wgt)
		wgt['Con']={}
		wgt['Elements']={}
		return wgt
	return create

@QCreate
def QEmpty(wgt,*a,**k):
	wgt['Wgt']	= None
	return wgt
@QCreate
def QApplication(wgt,*a,**k):
	wgt['Wgt']=QtLibs.QElements['app'](sys.argv)
	return wgt
@QCreate
def QComponent(wgt,qwgt,**k):
	wgt['Wgt']	=	qwgt()
	return wgt
@QCreate
def QLayout(lay,*a,**k):
	wgt					=	k.pop('widget')
	layout			=	QtLibs.QLayouts[k['t']]
	lay['Wgt']	=	layout(wgt['Wgt'])
	return lay

