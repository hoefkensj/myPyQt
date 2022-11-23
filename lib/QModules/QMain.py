#!/usr/bin/env python
import lib.Create
import lib.QWgt
import lib.gnr
import lib.PyQtX

def QMain(**k):
	def Create():
		w=lib.QWgt.make(k['pfx_name'],**k)
		return w
	def Cfg():
		c={
			'ObjectName'			:	k['pfx_name'],
			'ContentsMargins'	: k['margin'],
			}
		return c
	w=Create()
	w['Cfg'] 			= Cfg()
	w['Add']			=	w['Fnx']['Add']
	return w


def make(namestr,**k):
	name=lib.gnr.makeName(namestr)
	k={
		'margin'    :	[0,0,0,0]					,
		'pol'       :	'EE'							,
		't'         :	'v'								,
		}|k|{
		'pfx'       :	'wgt'							,
		'name'      :	name							,
		'pfx_name'  :	f'wgt_{name}'			,
		}
	return QMain(**k)