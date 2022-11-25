#!/usr/bin/env python
# Auth
from lib import gnr,QWgt
from lib.QElements import QIconButton

def QHSearch(**k):
	def Cfg():
		c={
			'ObjectName'        :		w['Name'],
			'SizePolicy'        :		gnr.makeSizePolicy(k['pol']),
			'ContentsMargins'   :		k['margin'],
			**k	}
		return c
	def Elements():
		parent=w['name']
		e		= {}
		e|= gnr.Element(QIconButton.make(f'<_{parent}', bi=False))
		e|= gnr.Element(QIconButton.make(f'>_{parent}', bi=False))
		return e
	def Con(wgt):
		s=gnr.ShortNames(wgt)
		c = {}
		c['<']=	s['<']['Mtd']['clicked'].connect
		c['>']=	s['>']['Mtd']['clicked'].connect
		return c
	w=QWgt.make(k['name'],**k)
	w['Elements'] = Elements()
	w['Fnx'] 			|=	gnr.Fnx(w)
	w['Con']			=	Con(w)
	return gnr.minInit(w)

def make(namestr,**k):
	k={
		'ed'        :	True								,
		'margin'    :	[0,0,0,0]						,
		'pol'       :	'E.F'								,
		't'         :	'H'									,
	} |	k	|	{
		'pfx'       :	'wgt'								,
		'name'      :	f'{namestr}_<>'			,
	}
	return QHSearch(**k)