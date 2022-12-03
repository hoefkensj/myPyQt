#!/usr/bin/env python
# Auth
from sys import argv,exit
from lib import Create
from static.QtLibs import QElements
from Configs import Config

def QtApplication(**k):
	def Fnx(wgt):
		def Run(wgt):
			def run():
				exit(wgt['Fnx']['Mtd']['exec']())
			return run
		wgt['Fnx']['Run'] = Run(wgt)
		return wgt

	w						=			Create.QCreate(QElements['app'], **k)
	w['Clip'] = w['Fnx']['Mtd']['clipboard']()
	return

def make(namestr,**k):
	preset={}
	k=Config.preset(['app',namestr],preset,**k)
	return QtApplication(**k)