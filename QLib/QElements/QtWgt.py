#!/usr/bin/env python
import QLib.Create
from QLib.QStatic import QElements
from QLib import gnr

from Configs import QDefaults
from Configs import Config

def QtWgt(**k):
	def Fnx(wgt):
		wgt= QLib.Create.Fnx(wgt)
		return wgt
	def Init(wgt)     :
		wgt=gnr.QElementInit(wgt)
		return wgt
	w							=	QLib.Create.QComponent(QElements[k['pfx']], **k)
	w							=	Config.make(w, **k)
	w['Con']			= {}
	w			= Fnx(w)
	return Init(w)

def make(namestr,**k):
	iconame=namestr.split('_')[0]
	k	= {
		**QDefaults.Properties							,
		'pol'       :	'P.P'									,
	} |	k	|	{
		'name'      :	namestr								,
	}
	return QtWgt(**k)
