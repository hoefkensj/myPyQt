#!/usr/bin/env python
from Configs import QDefaults
from Configs import Config
from QLib.QStatic import QtLibs,skel
from Fnx import QMake
import contextlib
def QLayout(**k):

	def Fnx(wgt):
		wgt['Fnx']={}
		wgt['Fnx']['Add']	= wgt['Qt']['Mtd']['addWidget']
		return wgt['Fnx']

	# Name  = k.get('Name')
	Widget=k.pop('widget')
	Layout=	QtLibs.QLayouts[k['t']]

	# Con		= {'Wgt' : {sig:Qt['Sig'][sig].connect for sig in Qt['Sig']}}

	w=QMake.Construct(**k)
	w=QMake.Configure(w)


def make(widget,**k):
	for key in k :
		print(key)
	return QLayout(**(QDefaults.QLayout|k|{'Name':k['Name'],'widget':widget}))
