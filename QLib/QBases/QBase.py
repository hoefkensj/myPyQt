#!/usr/bin/env python
from QLib import Create
from Configs import QDefaults
from Configs import Config
from QLib.QStatic import skel

# from QLib.QBases import QLayout


def Lay(wgt,**k):
	if k.get('t'):
		wgt['Lay']=QLayout.make(wgt, **k)
	return wgt

def Add(wgt):
	def add(component):
		cmpWgt=component['Wgt']
		wgt['Lay']['Fnx']['Add'](cmpWgt)
		return wgt
	return add



def QBase(**k):
	def Fnx(wgt):
		wgt['Fnx']['Wgt']['Local']['Add']		= Add(wgt)

		return wgt

	w 			= skel.QBase
	w= Name(w, **k)
	w				=	Create.QBase('wgt', **k)





	w['Wgt']= QtLibs.QElements[qwgt]()
	w['Gen']= Generate.make(w)
	w['Cfg']|=w['Gen']['Config'](**k)
	w=w['Gen']['Fnx']['Qt']()
	return w
	return  w

def make(namestr,**k):
	preset=QDefaults.QWidget
	k= Config.preset(preset, **k)
	return QWidge