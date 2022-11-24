#!/usr/bin/env python
# Auth


def Atrs(w):
	v = {}
	for n in dir(w):
		a1 = getattr(w, n)
		if not callable(a1):
			v[n] = a1
	return v

def Mtds(wgt):
	all={};sets={};reads={}

	for n in dir(wgt):
		m1 = getattr(wgt, n)
		if callable(m1):
			all[n] = m1

	for mtd in all:
		if mtd.startswith('set'):
			setmtd		=	mtd[3:]
			shortmtd	=	f'{setmtd[0].casefold()}{setmtd[1:]}'
			ismtd			=	f'is{setmtd}'
			if ismtd in all:
				readmtd	=	all[ismtd]
			elif shortmtd in all:
				readmtd	=	all[shortmtd]
			sets[setmtd]	=	all.pop(mtd)
			reads[setmtd]	=	all.pop(readmtd)

	return {'Set': sets,'Read': reads, 'Mtd': all}

def preCreate(pfx,name):
	w		=		{
		'Name'    :	f'{pfx}_{name}'			,
		'name'		:	name								,
		'type'		:	pfx									,
	}
	return w

def postCreate(wgt):
	w		=		{
							**Mtds(wgt)						,
		'Atr'     : Atrs(wgt)						,
	}
	return w

def QCreate(wgt,**k):
	QWgt=wgt()
	w	=	{
		**preCreate(k['pfx'],k['name'])	,
		'Wgt'     :	QWgt								,
		**postCreate(QWgt)							,}
	return w
