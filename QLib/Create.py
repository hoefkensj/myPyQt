#!/usr/bin/env python
# Auth
import contextlib
from QStatic import QtLibs
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
def Entry(fn):
	name=getattr(fn,'__name__')
	return {name: fn}

def Generate(wgt):
	wgt['Gen']|=Entry(Config.Config)
	wgt['Gen']|=Entry(Fnxs)
	wgt['Gen']|=Entry(Assemble)
	wgt['Gen']|=Entry(Configure)
	wgt['Gen']|=Entry(ConnectElements)
	return wgt

def Mtds(wgt):
	wgt['Fnx'] = wgt.get('Fnx') or {}
	wgt['Con'] = wgt.get('Con') or {}
	wgt['Fnx']['Mtd']=wgt.get('Mtd') or {}
	wgt['Fnx']['Mtd']['Wrappers']={}
	wgt['Fnx']['Mtd']['Atr']={}
	wgt['Fnx']['Set']={}
	wgt['Fnx']['Get']={}
	wgt['Fnx']['Sig']={}
	wgt['Fnx']['set']={}


	DirWgt=dir(wgt['Wgt'])
	for mtdn in DirWgt:
		mtd = getattr(wgt['Wgt'], mtdn)
		if not callable(mtd):
			wgt['Fnx']['Mtd']['Atr'][mtdn]=mtd
			continue
		cls=getattr(mtd,'__class__')
		if not mtdn.startswith('set') and \
				not isQtSignal(mtd) and \
			 		not isMethodWrapper(mtdn):
			wgt['Fnx']['Mtd'][mtdn] =	mtd
			continue
		if isQtSignal(mtd):
				wgt['Fnx']['Sig'][mtdn]=mtd
				wgt['Con'][mtdn]=mtd.connect

				continue
		elif isMethodWrapper(mtdn):
				wgt['Fnx']['Mtd']['Wrappers'][mtdn]=mtd
				continue
		elif mtdn.startswith('set'):
			# print(isSetGetPair(mtdn,DirWgt))
			shortmtd,getmtd=isSetGetPair(mtdn,DirWgt)
			if getmtd:
				wgt['Fnx']['Set'][shortmtd]	=	mtd
				wgt['Fnx']['Get'][shortmtd]	= getattr(wgt['Wgt'], getmtd)
			else:
				wgt['Fnx']['set'][shortmtd]	=	mtd
	return wgt


def QCreatePre(**k):
	pfx				=	k['pfx']
	wgttype		=	QtLibs.QElements.get(pfx).__name__ if QtLibs.QElements.get(pfx) else None
	name			=	k['name']
	w							=	{}
	w['Name']			=	f'{pfx}_{name}'
	w['name']			=	name
	w['type'] 		=	wgttype
	w['Wgt']			=	''
	w['Cfg']			= {}
	w['Gen']			=	{}
	w['Fnx']			=	{}
	w['Con']			=	{}
	w['Elements']	=	{}
	return w

def QCreatePost(wgt,**k):
	wgt = Generate(wgt)
	wgt['Gen']['Config']=wgt['Gen']['Config']()
	wgt['Gen']['Fnxs'](wgt)
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

def QApplication(*a,**k):
	@QCreate
	def qapplication(wgt,*a,**k):
		wgt['Wgt']= QtLibs.QElements['app'](sys.argv)
		return wgt
	wgt=qapplication(*a,**k)
	wgt['Gen']['Config'](wgt,**k)
	return wgt

def QBase(qwgt,**k):
	@QCreate
	def qbase(wgt,*a,**k):
		wgt['Wgt']	=	qwgt()
		return wgt
	wgt=qbase(qwgt,**k)
	return wgt

def QComponent(qwgt,**k):
	@QCreate
	def qcomponent(wgt,qwgt,**k):
		wgt['Wgt']	=	qwgt()
		return wgt
	wgt=qcomponent(qwgt,**k)
	wgt=wgt['Gen']['Configure'](wgt)
	return wgt


def QLayout(*a,**k):
	@QCreate
	def qlayout(lay,*a,**k):
		wgt			=	k.pop('widget')
		layout		=	QtLibs.QLayouts[k['t']]
		lay['Wgt']	=	layout(wgt['Wgt'])
		return lay
	lay=qlayout(*a,**k)
	lay.pop('Elements')
	lay.pop('Con')
	return lay





def Assemble(wgt):
	for element in 	wgt['Elements']:
		wgt['Fnx']['Add'](wgt['Elements'][element]['Wgt'])
	return wgt

def Fnxs(wgt):
	wgt	=	Mtds(wgt)
	return wgt

def Configure(wgt):
	for prop in wgt['Cfg']:
		with contextlib.suppress(KeyError):
			wgt['Fnx']['Set'][prop](wgt['Cfg'][prop])
	return wgt


def ConnectElements(wgt):
	for element in wgt['Elements']:
		wgt['Con'][element]=wgt['Elements'][element]['Con']

	return wgt




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
		wgt['Con'][name][key]=wgt['Fnx']['Sig'][key].connect
		print('\t',key,' : ',wgt['Con'][name][key])

	return wgt
