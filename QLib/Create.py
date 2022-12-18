#!/usr/bin/env python
# Auth
import contextlib
from QStatic import QtLibs
import sys
from Configs import Config
from time import sleep

def Entry(fn):
	name=getattr(fn,'__name__')
	return {name: fn}

def Generate(wgt):
	def Fnxs(wgt):
		wgt	=	Mtds(wgt)
		return wgt
	def Assemble(wgt):
		for element in 	wgt['Elements']:
			wgt['Fnx']['Add'](wgt['Elements'][element])
		return wgt
	def Configure(wgt):
		for prop in wgt['Cfg']:
			with contextlib.suppress(KeyError):
				wgt['Fnx']['Qt']['Set'][prop](wgt['Cfg'][prop])
		return wgt
	def ConnectElements(wgt):
		for element in wgt['Elements']:
			wgt['Con'][element]=wgt['Elements'][element]['Con']

		return wgt



	wgt['Fnx']['Gen']|=Entry(Config.Config)
	wgt['Fnx']['Gen']|=Entry(Fnxs)
	wgt['Fnx']['Gen']|=Entry(Assemble)
	wgt['Fnx']['Gen']|=Entry(Configure)
	wgt['Fnx']['Gen']|=Entry(ConnectElements)
	return wgt


def Mtds(wgt):
    def is_qt_signal(mtd):
        cls = getattr(mtd, '__class__')
        return cls.__name__ == 'pyqtBoundSignal'

    def is_method_wrapper(mtd):
        cls = getattr(mtd, '__class__')
        return cls.__name__ == 'method-wrapper'

    def is_set_get_pair(mtd, pool):
        mtdcn = mtd[3:]
        mtdsn = f'{mtdcn[0].casefold()}{mtdcn[1:]}'
        mtdin = f'is{mtdcn}'
        mtdsn = mtdsn if mtdsn in pool else ''
        mtdin = mtdin if mtdin in pool else ''
        getmtd = mtdsn or mtdin
        return mtdcn, getmtd

    wgt['Fnx'] = wgt.get('Fnx') or {}
    wgt['Con'] = wgt.get('Con') or {}
    wgt['Fnx']['Qt'] = {
        'Mtd': {}, 'Wrp': {}, 'Atr': {},
        'Set': {}, 'Get': {}, 'Sig': {},
        'set': {},
    }
    Mtd = wgt['Fnx']['Qt']['Mtd']
    atr = wgt['Fnx']['Qt']['Atr']
    wrp = wgt['Fnx']['Qt']['Wrp']
    Set = wgt['Fnx']['Qt']['Set']
    Get = wgt['Fnx']['Qt']['Get']
    Sig = wgt['Fnx']['Qt']['Sig']
    sset = wgt['Fnx']['Qt']['set']
    con = wgt['Con']
    DirWgt = dir(wgt['Wgt'])

    for mtdn in DirWgt:
        mtd = getattr(wgt['Wgt'], mtdn)
        if not callable(mtd):
            atr[mtdn] = mtd
            continue

        if is_qt_signal(mtd):
            Sig[mtdn] = mtd
            con[mtdn] = mtd.connect
            continue
        elif is_method_wrapper(mtd):
            wrp[mtdn] = mtd
            continue
        elif mtdn.startswith('set'):
            shortmtd, getmtd = is_set_get_pair(mtdn, DirWgt)
            if getmtd:
                Set[shortmtd] = mtd
                Get[shortmtd] = getattr(wgt['Wgt'], getmtd)
            else:
                sset[shortmtd] = mtd
        else:
            Mtd[mtdn] = mtd



# def Mtds(wgt):
# 	def isQtSignal(mtd):
# 		cls=getattr(mtd,'__class__')
# 		return cls.__name__ == 'pyqtBoundSignal'
# 	def isMethodWrapper(mtd):
# 		cls=getattr(mtd,'__class__')
# 		return cls.__name__ == 'method-wrapper'
# 	def isSetGetPair(mtd,pool):
# 			mtdcn		= mtd[3:]
# 			mtdsn		=	f'{mtdcn[0].casefold()}{mtdcn[1:]}'
# 			mtdin		=	f'is{mtdcn}'
# 			mtdsn=mtdsn*(mtdsn in pool)
# 			mtdin=mtdin*(mtdin in pool)
# 			getmtd=(mtdsn and mtdin) or mtdsn or mtdin
# 			return  (mtdcn,getmtd)
#
# 	wgt['Fnx'] = wgt.get('Fnx') or {}
# 	wgt['Con'] = wgt.get('Con') or {}
# 	wgt['Fnx']['Qt']={
# 		'Mtd' : {}	,	'Wrp':	{}	,	'Atr'	:	{}	,
# 		'Set'	:	{}	,	'Get'	:	{}	,	'Sig':	{}	,
# 		'set'	:	{}	,	}
# 	Mtd=wgt['Fnx']['Qt']['Mtd']
# 	atr=wgt['Fnx']['Qt']['Atr']
# 	wrp=wgt['Fnx']['Qt']['Wrp']
# 	Set=wgt['Fnx']['Qt']['Set']
# 	Get=wgt['Fnx']['Qt']['Get']
# 	Sig=wgt['Fnx']['Qt']['Sig']
# 	sset=wgt['Fnx']['Qt']['set']
# 	con=wgt['Con']
# 	DirWgt=dir(wgt['Wgt'])
# 	cpyDW=[*DirWgt]
# 	matchless=[]
# 	for mtdn in cpyDW:
# 		if mtdn not in DirWgt:
# 			continue
# 		mtd = getattr(wgt['Wgt'], mtdn)
# 		if not callable(mtd):
# 			atr[mtdn]=mtd
# 			DirWgt.remove(mtdn)
# 			continue
# 		cls=getattr(mtd,'__class__')
# 		if not mtdn.startswith('set') and \
# 				not isQtSignal(mtd) and \
# 					not isMethodWrapper(mtdn):
# 			DirWgt.remove(mtdn)
# 			matchless+=[mtdn]
# 			continue
#
# 		if isQtSignal(mtd):
# 				Sig[mtdn]=mtd
# 				con[mtdn]=mtd.connect
# 				DirWgt.remove(mtdn)
# 				continue
# 		elif isMethodWrapper(mtdn):
# 				wrp[mtdn]=mtd
# 				DirWgt.remove(mtdn)
# 				continue
# 		elif mtdn.startswith('set'):
# 			# print(isSetGetPair(mtdn,DirWgt))
#
# 			shortmtd,getmtd=isSetGetPair(mtdn,cpyDW)
# 			if getmtd:
# 				Set[shortmtd]	=	mtd
# 				Get[shortmtd]	= getattr(wgt['Wgt'], getmtd)
# 				DirWgt.remove(mtdn)
# 				if getmtd in DirWgt:
# 					DirWgt.remove(getmtd)
# 				elif getmtd in matchless:
# 					matchless.remove(getmtd)
#
#
#
# 			else:
# 				sset[shortmtd]	=	mtd
# 				DirWgt.remove(mtdn)
# 	for key in matchless:
# 		Mtd[key]=getattr(wgt['Wgt'], key)
# 	return wgt
def Naming(w,**k):
	pfx					=	k['pfx']
	name				=	k['name']
	w['Name']			=	f'{pfx}_{name}'
	w['name']			=	name
	return w

def QCreate(fn):


	def QCreatePost(wgt,**k):
		wgt = Generate(wgt)
		wgt=wgt['Fnx']['Gen']['Config'](wgt,**k)
		wgt['Fnx']['Gen']['Fnxs'](wgt)
		return wgt

	def create(w,**k):
		w =	Naming(w,**k)

		w	=	fn(w,*a,**k)
		w	=	QCreatePost(w,**k)
		return w
	return create



def QApplication(*a,**k):
	@QCreate
	def qapplication(wgt,*a,**k):
		wgt['Wgt']= QtLibs.QElements['app'](sys.argv)
		return wgt
	wgt=qapplication(*a,**k)
	wgt=wgt['Fnx']['Gen']['Configure'](wgt)
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
	wgt=wgt['Fnx']['Gen']['Configure'](wgt)
	return wgt

def QLayout(wgt,**k):
	@QCreate
	def qlayout(lay,*a,**k):


		lay['Wgt']	=	layout(wgt['Wgt'])
		return lay
	widget		=	k.pop('widget')
	layout		=	QtLibs.QLayouts[k['t']]
	w=qlayout(*a,**k)


	lay=lay['Fnx']['Gen']['Configure'](lay)
	return lay



def Show(wgt):
	def show(*a):
		if a:
			mtd[a[0]]()
		else:
			state=mtd['exec']()
			mtd[state]()
	if wgt['Fnx']['Qt']['Mtd'].get('show'):
		mtd={
				True    :	wgt['Fnx']['Qt']['Mtd']['show'],
				False   :	wgt['Fnx']['Qt']['Mtd']['hide'],
				'exec'  :	wgt['Fnx']['Qt']['Get']['Hidden']}
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
