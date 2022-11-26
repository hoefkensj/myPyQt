#!/usr/bin/env python
# Auth
from lib import gnr,QWgt
from lib.QElements import QIconButton

def QHArrowsLR(**k):
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
		e|= gnr.Element(QIconButton.make(f'<_{parent}', wh=[15,20],bi=False))
		e|= gnr.Element(QIconButton.make(f'>_{parent}', wh=[15,20],bi=False))
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
		c['<']=	s['<']['Mtd']['clicked'].connect
		c['>']=	s['>']['Mtd']['clicked'].connect
		return c
	w=QWgt.make(k['name'],**k)
	w['Cfg']		=			Cfg()
	w['Elements'] = Elements()
	w['Fnx'] 			|= Fnx(w)
	w['Con']			=	Con(w)
	return gnr.minInit(w)

def make(namestr,**k):
	k={
		'ed'        :	True								,
		'margin'    :	[0,0,0,0]						,
		'pol'       :	'F.F'								,
		't'         :	'H'									,
	} |	k	|	{
		'pfx'       :	'wgt'								,
		'name'      :	f'{namestr}_<>'			,
	}
	return QHArrowsLR(**k)