#!/usr/bin/env python
import lib.Create
from static.QtLibs import QElements
from lib import gnr

from Configs import QDefaults,Config
def QtWgt(**k):
	def Fnx(wgt):
		wgt=gnr.Fnx(wgt)
		return wgt
	def Init(wgt):
		wgt=wgt['Fnx']['Configure'](wgt)
		return wgt
	w							=	lib.Create.QCreate(QElements[k['pfx']], **k)
	w							=	Config.make(w,**k)
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
