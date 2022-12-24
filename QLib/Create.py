#!/usr/bin/env python
# Auth
from Fnx.tools import Name

from QLib.QStatic import QtLibs
from QLib.QStatic import skel


# def Fnx_Qt(wgt):
#     def is_qt_signal(mtd):
#         cls = getattr(mtd, '__class__')
#         return cls.__name__ == 'pyqtBoundSignal'
#
#     def is_method_wrapper(mtd):
#         cls = getattr(mtd, '__class__')
#         return cls.__name__ == 'method-wrapper'
#
#     def is_set_get_pair(mtd, pool):
#         mtdcn = mtd[3:]
#         mtdsn = f'{mtdcn[0].casefold()}{mtdcn[1:]}'
#         mtdin = f'is{mtdcn}'
#         mtdsn = mtdsn if mtdsn in pool else ''
#         mtdin = mtdin if mtdin in pool else ''
#         getmtd = mtdsn or mtdin
#         return mtdcn, getmtd
#
#     wgt['Fnx'] = wgt.get('Fnx') or {}
#     wgt['Con'] = wgt.get('Con') or {}
#     wgt['Fnx']['Qt'] = {
#         'Mtd': {}, 'Wrp': {}, 'Atr': {},
#         'Set': {}, 'Get': {}, 'Sig': {},
#         'set': {},
#     }
#     Mtd = wgt['Fnx']['Qt']['Mtd']
#     atr = wgt['Fnx']['Qt']['Atr']
#     wrp = wgt['Fnx']['Qt']['Wrp']
#     Set = wgt['Fnx']['Qt']['Set']
#     Get = wgt['Fnx']['Qt']['Get']
#     Sig = wgt['Fnx']['Qt']['Sig']
#     sset = wgt['Fnx']['Qt']['set']
#     con = wgt['Con']
#     DirWgt = dir(wgt['Wgt'])
#
#     for mtdn in DirWgt:
#         mtd = getattr(wgt['Wgt'], mtdn)
#         if not callable(mtd):
#             atr[mtdn] = mtd
#             continue
#
#         if is_qt_signal(mtd):
#             Sig[mtdn] = mtd
#             con[mtdn] = mtd.connect
#             continue
#         elif is_method_wrapper(mtd):
#             wrp[mtdn] = mtd
#             continue
#         elif mtdn.startswith('set'):
#             shortmtd, getmtd = is_set_get_pair(mtdn, DirWgt)
#             if getmtd:
#                 Set[shortmtd] = mtd
#                 Get[shortmtd] = getattr(wgt['Wgt'], getmtd)
#             else:
#                 sset[shortmtd] = mtd
#         else:
#             Mtd[mtdn] = mtd



def QBase(qwgt,**k):
	w = skel.QBase
	w= Name(w, **k)
	w['Wgt']= QtLibs.QElements[qwgt]()
	w['Gen']= Generate.make(w)
	w['Cfg']|=w['Gen']['Config'](**k)
	w=w['Gen']['Fnx']['Qt']()
	return w

def QComponent(qwgt,**k):
	wgt['Wgt']= QtLibs.QElements[qwgt]()

	return wgt



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

