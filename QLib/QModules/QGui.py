#!/usr/bin/env python
from QLib.QElements import QApplication
from Fnx import QMake
from Configs import Config
from QLib.QStatic import QtLibs
from QLib.QStatic import skel
from Structures import Generate
from Fnx.tools import Name

def QGui(*a,**k):
	def Run(wgt):
		def run(wgt):
			def Execute():
				wgt['App']['Fnx']['Run']()
			return Execute
		return run

	def Fnx(wgt):
		return wgt



	w = skel.QBase
	w= Name(w, **k)
	w['App'] 				= 	QApplication.make(w['Name'], **k)
	w['Wgt']				= 	QtLibs.QElements['wgt']()
	w['Gen']				= 	Generate.make(w)
	w['Cfg']				= 	QMake.Config(**k)
	w['Run']				=		Run(w)
	return w

def make(namestr,**k):
	preset={}|{'Name' :namestr}
	k= Config.preset(preset, **k)
	return QGui(**k)
