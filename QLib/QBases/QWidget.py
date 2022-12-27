#!/usr/bin/env python
from Configs import QDefaults
from QLib.QBases import QLayout
from QLib.QStatic import QtLibs,skel
from Configs import Config
from Fnx import QMake
from Fnx.debug import DebDec


def QWidget(**k):
	def Fnx(wgt):
		def Add(wgt):
			def add(component):
				wgt['Lay']['Fnx']['Add'](component['Wgt'])
				wgt['Fnx'][component['QID']]=component['Fnx']
				# wgt['Con'][component['QID']]=component['Con']
				return wgt
			return add
		def Show(wgt):
			def show():
				if Qt['Get']['Hidden']():	Qt['Set']['Show'](True)
				elif Qt['Get']['Visible']():	Qt['Set']['Hidden'](True)
				return wgt
			return show
		fnx['Wgt'] = {}
		fnx['Wgt'] |= QMake.Entry(Add, wgt)
		fnx['Wgt'] |= QMake.Entry(Show, wgt)
		wgt['Fnx']=fnx
		return wgt
	def Mod(wgt):
		wgt['Mod']={}
		return wgt
	Constructs=QMake.Construct()
	w=QtLibs.QElements.get('wgt')()
	for construct in Constructs('QBse'):
		w=construct(w,Fnx,Mod,**k)
	return w

def make(name,**k):
	return QWidget(**(QDefaults.QWidget|k|{'Name':name}))