#!/usr/bin/env python
# Auth
def Mtds(w):
	f = {}
	for n in dir(w):
		m1 = getattr(w, n)
		if callable(m1):
			f[n] = m1
	return f

def Atrs(w):
	v = {}
	for n in dir(w):
		a1 = getattr(w, n)
		if not callable(a1):
			v[n] = a1
	return v

def SetMtds(wgt):
	mtds=wgt['Mtd']
	sets={};reads={}
	nocase=[]
	for mtd in mtds:
		if mtd.startswith('set'):
			short=mtd[3:]
			nocase+=[short.casefold()]
			sets[short]=mtds[mtd]
	for mtd in mtds:
		if mtd.startswith('is'):
			fix=mtd[2:]
		else:
			fix=f'{mtd[0].upper()}{mtd[1:]}'
		if mtd.casefold() in nocase:
			reads[fix]=mtds[mtd]
	SetMtds={'Set': sets,'Read': reads}
	return SetMtds

def postCreate(wgt,type,**k):
	return {
	'Name'    :	k['pfx_name']	,
	'name'    :	k['name']			,
	type     	:	wgt						,
	'Mtd'     :	Mtds(wgt)			,
	'Atr'     : Atrs(wgt)			,
	**SetMtds(wgt)						,
	}

def QCreate(QtFn,**k):
	wgt=QtFn(k['pfx_name'],**k)
	return postCreate(wgt,'Wgt',**k)

def QtCreate(QtFn,**k):
	wgt=QtFn()
	return postCreate(wgt,'Wgt',**k)

def QlCreate(QlFn,**k):
	lay=QlFn(k['widget']['Wgt'])
	return postCreate(lay,'Lay',**k)
