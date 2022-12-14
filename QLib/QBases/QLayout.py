#!/usr/bin/env python
from Configs import QDefaults
from Configs import Config
from QLib.QStatic import QtLibs,skel
from Fnx import QMake
import contextlib
from Fnx.debug import DebDec


def QLayout(**k):
	def Fnx(wgt):
		wgt['Fnx']={}
		wgt['Fnx']['Add']	= wgt['Qtm']['Mtd']['addWidget']
		return wgt
	Widget=k.pop('widget')
	l=QtLibs.QLayouts[k['t']](Widget['Wgt'])


	for construct in QMake.QBuilders('QLay'):
		l=construct(l,Fnx,**k)


	Widget['Lay']=l
	return Widget


def make(widget,**k):
	return QLayout(**(QDefaults.QLayout|k|{'Name':k['Name'],'widget':widget}))
