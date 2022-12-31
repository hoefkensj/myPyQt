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
				wgt['Fnx'][component['Qid']]=component['Fnx']
				wgt['Con'][component['Qid']]=component['Con']
				return wgt
			return add
		def Show(wgt):
			def show():
				if Qt['Get']['Hidden']():	Qt['Set']['Show'](True)
				elif Qt['Get']['Visible']():	Qt['Set']['Hidden'](True)
				return wgt
			return show
		fnx = {}
		fnx|= QMake.Entry(Add, wgt)
		fnx|= QMake.Entry(Show, wgt)
		return fnx
	def Mod(wgt):
		return wgt

	return QMake.QBuild('QBse','wgt',Fnx,Mod,**k)

def make(name,**k):
	return QWidget(**(QDefaults.QWidget|k|{'Name':name}))