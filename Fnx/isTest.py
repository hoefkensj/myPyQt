#!/usr/bin/env python
# Auth
from Fnx.tools import RE_QTMTD


def isQtSignal(mtd):
	pyqtsig='pyqtBoundSignal'
	cls=getattr(mtd,'__class__')
	return cls.__name__ == pyqtsig

def isMethodWrapper(mtd):
	mtdwrap='method-wrapper'
	cls=getattr(mtd,'__class__')
	return cls.__name__ == mtdwrap

def isIsMtd(mtd):
	isIsMtd=RE_QTMTD('IS')
	tested=isIsMtd.search(mtd)
	ret=False
	if tested:
		grp=tested.groupdict()
		if grp.get('IS'):
			ret=grp.get('MTD')
	return  ret

def isSetMtd(mtd):
	isIsMtd=RE_QTMTD('SET')
	tested=isIsMtd.search(mtd)
	ret=False
	if tested:
		grp=tested.groupdict()
		if grp.get('SET'):
			ret=grp.get('MTD')

	return  ret



	# if mtd[:3]=='set':
	# 	clitm		= mtd[3:]
	# 	isitm=	f'is{clitm}'
	# 	result= ['Set', (isitm in pool), (clitm in pool)]
	# elif mtd[:2]=='is':
	# 	clitm		= mtd[2:]
	# 	stitm=	f'set{clitm}'
	# 	if (stitm or clitm) in pool:
	# 		return ['is', (stitm in pool), (clitm in pool)]
	# else:
	# 	clitm		= mtd
	# 	isitm=	f'is{clitm}'
	# 	stitm=	f'set{clitm}'
	# 	if (stitm or isitm) in pool:
	# 		return ['cl', (stitm in pool), (isitm in pool)]
	# 	else:
	# 		return False
	#
	# 	mtdsn		=	f'{mtdcn[0].casefold()}{mtdcn[1:]}'
	# 	mtdin		=	f'is{mtdcn}'
	# 	mtdsn=mtdsn*(mtdsn in pool)
	# 	mtdin=mtdin*(mtdin in pool)
	# 	getmtd=(mtdsn and mtdin) or mtdsn or mtdin


	# if all([any([result[0],result[1]]), result[2]]):
	# 	ret=itm,result
	# else:
	# 	ret=False,result
	# return ret