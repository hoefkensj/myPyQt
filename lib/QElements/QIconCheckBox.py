#!/usr/bin/env python
# Auth
from lib import gnr,Create
from static.QtLibs import QElements

from Configs import QDefaults,Config
def QIconCheckBox(**k):
	def Fnx(wgt):
		def toggle():
			state=w['Mtd']['isChecked']
			wgt['Fnx']['Mtd']['setChecked'](not state)
		f 					= {}
		f['Configure']	=gnr.makeConfigure(wgt)
		f['Toggle']	= toggle
		return f
	def Con():
		c={}
		c['clicked'] = w['Wgt'].clicked.connect
		c['clicked'](w['Mtd']['toggle'])
		return c
	def Init(wgt)     :
		wgt=wgt['Fnx']['Configure']()
		return wgt
	w						=			Create.QCreate(QElements['chkB'], **k)
	w						=			Config.make(w,**k)
	w['Fnx']		=			Fnx(w)
	w['Con']		=			Con()
	return Init(w)

def make(namestr, **k):
	iconame=namestr.split('_')[0]
	k	= {
		**QDefaults.Properties							,
		'pol'       :	'P.P'									,
		'wh'        :	[20,20]								,
		'ico'       :	gnr.IconSet(iconame)	,
		'isize'     :	[32,32]								,
		'lbl'       :	None									,
	} |	k	|	{
		'name'      :	namestr								,
		'pfx'       :	'chkB'								,
	}
	return QIconCheckBox(**k)