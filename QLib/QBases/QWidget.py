#!/usr/bin/env python
from Configs import QDefaults
from QLib.QBases import QLayout
from QLib.QStatic import QtLibs,skel
from Configs import Config
from Fnx import QMake


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
		wgt['Fnx'] = {}
		wgt['Fnx'] |= QMake.Entry(Add, wgt)
		wgt['Fnx'] |= QMake.Entry(Show, wgt)
		return wgt['Fnx']
	def Mod():
		return {}
	w=QMake.Construct(**k)
	w=QMake.Configure(w)
	return  w

def make(namestr,**k):
	return QWidget(**(QDefaults.QWidget|k|{'Name':namestr}))