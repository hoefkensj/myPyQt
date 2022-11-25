#!/usr/bin/env python
import lib.Create
import lib.QWgt
import lib.gnr
import lib.PyQtX

def QMain(**k):

	def Cfg():
		c={
			'ObjectName'			:	w['Name'],
			'ContentsMargins'	: k['margin'],
			'SizePolicy'			:	lib.gnr.makeSizePolicy(k['pol'])
			}
		return c
	def Init(wgt):
		wgt=wgt['Fnx']['Configure']()

	w=lib.QWgt.make(k['name'],**k)
	w['Cfg'] 			= Cfg()
	w['Add']			=	w['Fnx']['Add']
	return w


def make(namestr,**k):
	k={
		'margin'    :	[0,0,0,0]					,
		'pol'       :	'E.E'							,
		't'         :	'V'								,
	}	|	k	|	{
		'pfx'       :	'wgt'							,
		'name'      :	namestr							,
	}
	return QMain(**k)
