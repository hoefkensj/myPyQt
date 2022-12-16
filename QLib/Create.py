#!/usr/bin/env python
# Auth
import contextlib
from Qt import QtLibs
import sys
from Configs import Config

def isQtSignal(mtd):
	cls=getattr(mtd,'__class__')
	return cls.__name__ == 'pyqtBoundSignal'

def isMethodWrapper(mtd):
	cls=getattr(mtd,'__class__')
	return cls.__name__ == 'method-wrapper'
def isSetGetPair(mtd,pool):
		mtdcn		= mtd[3:]
		mtdsn		=	f'{mtdcn[0].casefold()}{mtdcn[1:]}'
		mtdin		=	f'is{mtdcn}'
		mtdsn=mtdsn*(mtdsn in pool)
		mtdin=mtdin*(mtdin in pool)
		getmtd=(mtdsn and mtdin) or mtdsn or mtdin
		return  (mtdcn,getmtd)

def Mtds(wgt):
	f = wgt.get('Fnx') or {}
	f['Mtd']=wgt.get('Mtd') or {}
	f['Mtd']['Wrappers']={}
	f['Atr']={}
	f['Set']={}
	f['set']={}
	f['Sig']={}
	f['Get']={}
	DirWgt=dir(wgt['Wgt'])
	for mtdn in DirWgt:
		mtd = getattr(wgt['Wgt'], mtdn)
		if not callable(mtd):
			continue
		cls=getattr(mtd,'__class__')
		if not mtdn.startswith('set') and \
				not isQtSignal(mtd) and \
			 		not isMethodWrapper(mtdn):
			f['Mtd'][mtdn] =	mtd
			continue
		if isQtSignal(mtd):
				f['Sig'][mtdn]=mtd
				continue
		elif isMethodWrapper(mtdn):
				f['Mtd']['Wrappers'][mtdn]=mtd
				continue
		elif mtdn.startswith('set'):
			# print(isSetGetPair(mtdn,DirWgt))
			shortmtd,getmtd=isSetGetPair(mtdn,DirWgt)
			if getmtd:
				f['Set'][shortmtd]	=	mtd
				f['Get'][shortmtd]	= getattr(wgt['Wgt'], getmtd)

	wgt['Fnx']=f
	return wgt


def QCreatePre(**k):
	pfx			=	k['pfx']
	type		=	QtLibs.QElements.get(pfx).__name__ if QtLibs.QElements.get(pfx) else None
	name		=	k['name']
	w				=	{
		'Name'    :	f'{pfx}_{name}'			,
		'name'    :	name								,
		'type'    :	type								,}
	return w
def QCreatePost(wgt,*selected,**k):
	wgt = Config.make(wgt, **k)
	wgt	= Fnx(wgt)
	if not selected:
		sel='W'
	else:
		sel=selected[0]
	if selected =='L':
		return wgt
	elif selected == 'W':
		wgt=Con(wgt)
		wgt['Lay']={}
		wgt['Elements']={}

	return wgt

def QCreate(fn):
	def create(*a,**k):
		w	=	QCreatePre(**k)
		w	=	fn(w,*a,**k)
		w	=	QCreatePost(w,**k)
		return w


	return create

@QCreate
def QEmpty(wgt,*a,**k):
	wgt['Wgt']	= None
	return wgt
@QCreate
def QApplication(wgt,*a,**k):
	wgt['Wgt']= QtLibs.QElements['app'](sys.argv)
	return wgt
@QCreate
def QComponent(wgt,qwgt,**k):
	wgt['Wgt']	=	qwgt()
	return wgt
@QCreate
def QLayout(lay,*a,**k):
	wgt			=	k.pop('widget')
	layout		=	QtLibs.QLayouts[k['t']]
	lay['Wgt']	=	layout(wgt['Wgt'])
	return lay

def SpecialCases(wgt):
	def HideCols(wgt):
		cols = wgt['Cfg']['hidecols']
		for col in cols:
			wgt['Fnx']['Set']['ColumnHidden'](col,True)
		return wgt
	Cases={
		'hidecols'        :	HideCols			,
	}
	for Case in Cases:
		if Case in  wgt['Cfg']:
			wgt=Cases[Case](wgt)
	return wgt

def AddFnx(fn):
	name=getattr(fn,'__name__')
	def addfnx(wgt,*a,**k):
		wgt['Fnx'][name]=fn()
		return wgt
	return addfnx


def Configure():
	def configure(wgt):
		for prop in wgt['Cfg']:
				with contextlib.suppress(KeyError):
					wgt['Fnx']['Set'][prop](wgt['Cfg'][prop])
		return wgt
	return configure


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
				True    :	wgt['Fnx']['Mtd']['show'],
				False   :	wgt['Fnx']['Mtd']['hide'],
				'exec'  :	wgt['Fnx']['Get']['Hidden']}
		wgt['Fnx']['Show']=show
	return wgt

def Fnx(wgt):
	wgt['Fnx']=wgt.get('Fnx') or {}
	wgt	=	Mtds(wgt)
	wgt['Fnx']['Configure']=Configure()
	return wgt
def sprint():
	def pr():
		print('success')
	return pr

def Con(wgt):
	name=wgt['name']
	wgt['Con']={}
	# wgt['Con'][name]={con:wgt['Fnx']['Sig'][con].connect for con in wgt['Fnx']['Sig']}
	print('#'*50)
	print(name)
	for key in wgt['Fnx']['Sig']:
		wgt['Con'][name][key]=wgt['Fnx']['Sig'][key]
		print('\t',key,' : ',wgt['Con'][name][key])

	return wgt
