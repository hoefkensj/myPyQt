#!/usr/bin/env python
# Auth
from sys import argv,exit
from lib import Create
from static.QtLibs import QElements
from Configs import Config
import asyncio
import sys

def QtApplication(**k):
	def Fnx(wgt):
		def Run(wgt):
			async def app():
				wgt['Fnx']['Mtd']['exec']()
			def run():
				asyncio.run(app())
			return run
		wgt['Fnx']['Run'] = Run(wgt)
		return wgt

	w					=			Create.QApplication(**k)
	w					= 		Fnx(w)
	w['Clip'] =			w['Fnx']['Mtd']['clipboard']()
	return w

def make(namestr,**k):
	preset={}
	k=Config.preset(['app',namestr],preset,**k)
	return QtApplication(**k)