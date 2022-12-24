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

	w = {**skel.QLayout}
	for key in w:
		w[key]=eval(w[key].format(**k['QLAY']))
	w['Fnx']=	Fnx(w)
	w=w['Cfg'](w)
	return  w


def make(widget,**k):
	preset=QDefaults.QLayout|{
		'widget'    :	widget	,	}
	k= Config.preset(preset, **k)
	return QLayout(**k)