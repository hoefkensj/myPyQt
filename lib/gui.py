#!/usr/bin/env python


import sys

import lib.Create
import lib.QModules.QMain
import lib.QtApplication
from Configs import QDefaults,Config
from lib import gnr






def QGui(*a,**k):
	def Fnx(wgt):
		def ReCfgElements(wgt):
			for element in wgt['Elements']:
				wgt['Elements'][element]['Fnx']['ReConfigure'](element)

		def Run():
			def run():
				for element in wgt['Main']['Elements']:
					wgt['Main']['Elements'][element]=wgt['Main']['Elements'][element]['Fnx']['Configure'](wgt['Main']['Elements'][element])
				sys.exit(wgt['App']['QtApp'].exec())
			return run
		wgt['Main']=gnr.Fnx(wgt['Main'])
		wgt['Fnx']=wgt['Main']['Fnx']
		wgt['Fnx']['ReCfgElements']=ReCfgElements
		wgt['Fnx']['Add']			=	wgt['Main']['Add']
		wgt['Fnx']['Run']			=	Run()
		return wgt

	def Init(wgt):
		wgt['Main']=gnr.minInit(GUI['Main'])
		wgt['Main']['Fnx']['Show'](True)
		return wgt

	GUI 							= lib.Create.QCreate(**k)
	GUI['App'] 				= 	lib.QtApplication.QtApplication()
	GUI['Main'] 			=	 	lib.QModules.QMain.make(GUI['name'],**k)
	GUI								= 	Fnx(GUI)
	GUI['Elements']		=		GUI['Main']['Elements']
	GUI['Fnx']				=		GUI['Main']['Fnx']
	# GUI['Show']				=		GUI['Fnx']['Show']
	GUI['Run']				=		GUI['Fnx']['Run']
	return Init(GUI)

def make(namestr,**k):
	k=QDefaults.Properties|k|Config.names('gui',namestr)
	return QGui(**k)

# pTree(d=GUI)

# pTree()
# browse(myPyQt=GUI())