#!/usr/bin/env python
# Auth
import lib.Create

from lib.QElements import QIconButton
from lib import gnr,QWgt
from lib.QModules import QHArrowsLR

def QHSearchCtl(**k):
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
		e|= gnr.Element(QHArrowsLR.make(f'<>_{parent}', bi=False))
		e|=	gnr.Element(QIconButton.make(f'Search_{parent}', bi=False))
		return e
	def Fnx(wgt):
		def Init(wgt):
			def init():
				pass
			return init
		f=gnr.Fnx(w)
		f['Init']=Init(wgt)
		return f
	def Con(wgt):
		s=gnr.ShortNames(wgt)
		c = {}
		c['Search']=	s['Search']['Mtd']['clicked'].connect
		return c
	w=QWgt.make(k['name'],**k)
	w['Cfg']		=			Cfg()
	w['Elements'] = Elements()
	w['Fnx'] 			|=	Fnx(w)
	w['Con']			=	Con(w)
	return gnr.minInit(w)

def make(namestr,**k):
	k={
		'ed'        :	True								,
		'margin'    :	[0,0,0,0]						,
		'pol'       :	'P.P'								,
		't'         :	'H'									,
	} |	k	|	{
		'pfx'       :	'wgt'								,
		'name'      :	f'{namestr}_SCtl'		,
	}
	return QHSearchCtl(**k)



