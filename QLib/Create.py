#!/usr/bin/env python
# Auth
import contextlib
from static import QtLibs
import sys
from Configs import Config

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
				mtdcn		= mtdn[3:]
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

def QCreate(fn):
	def Pre(**k):
		pfx			=	k['pfx']
		type		=	QtLibs.QElements.get(pfx).__name__ if QtLibs.QElements.get(pfx) else None
		name		=	k['name']
		w				=	{
			'Name'    :	f'{pfx}_{name}'			,
			'name'    :	name								,
			'type'    :	type								,}
		return w

	def create(*a,**k):
		w	=	Pre(**k)
		w	=	fn(w,*a,**k)
		w	=	Post(w,**k)
		return w

	def Post(wgt,**k):
		wgt = Config.make(wgt, **k)
		wgt['Lay']={}
		wgt	=	Mtds(wgt)
		wgt	= QElemntFnx(wgt)
		wgt['Con']={}
		wgt['Elements']={}
		return wgt
	return create

def LCreate(fn):
	def Pre(**k):
		pfx			=	k['pfx']
		type		=	QtLibs.QElements.get(pfx).__name__ if QtLibs.QElements.get(pfx) else None
		name		=	k['name']
		w				=	{
			'Name'    :	f'{pfx}_{name}'			,
			'name'    :	name								,
			'type'    :	type								,}
		return w

	def create(*a,**k):
		w	=	Pre(**k)
		w	=	fn(w,*a,**k)
		w	=	Post(w,**k)
		return w

	def Post(wgt,**k):
		wgt = Config.make(wgt, **k)
		wgt	=	Mtds(wgt)
		wgt	= QElemntFnx(wgt)
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

@LCreate
def QLayout(lay,*a,**k):
	wgt			=	k.pop('widget')
	layout		=	QtLibs.QLayouts[k['t']]
	lay['Wgt']	=	layout(wgt['Wgt'])
	return lay

def AddFnx(fn):
	name=getattr(fn,'__name__')
	def addfnx(wgt,*a,**k):
		wgt['Fnx'][name]=fn()
		return wgt
	return addfnx

@AddFnx
def Configure():
	def configure(wgt):
		for prop in wgt['Cfg']:
			if prop in wgt['Fnx']['Set']:
				wgt['Fnx']['Set'][prop](wgt['Cfg'][prop])
			elif prop in wgt['Fnx']['Mtd']:
				wgt['Fnx']['Mtd'][prop](wgt['Cfg'][prop])
			else:
				with contextlib.suppress(KeyError):
					wgt['Fnx'][prop](wgt['Cfg'][prop])
		return wgt
	return configure

@AddFnx
def Generate():
	def generate(wgt):
		for element in 	wgt['Elements']:
			wgt['Fnx']['Add'](wgt['Elements'][element]['Wgt'])
		return wgt
	return generate

def Show(wgt):
	def show(*a):
		if a:
			mtd[a[0]]()
		else:
			state=mtd['exec']()
			mtd[state]()
	if wgt['Fnx']['Mtd'].get('show'):
		mtd={
				True		:	wgt['Fnx']['Mtd']['show'],
				False		:	wgt['Fnx']['Mtd']['hide'],
				'exec'	:	wgt['Fnx']['Get']['Hidden']}
		wgt['Fnx']['Show']=show
	return wgt

def QElemntFnx(wgt):
	wgt = Configure(wgt)
	wgt	= Generate(wgt)
	wgt	= Show(wgt)
	return wgt

def QModuleFnx(wgt):
	wgt = Configure(wgt)
	wgt	= Show(wgt)
	return wgt