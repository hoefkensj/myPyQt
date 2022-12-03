#!/usr/bin/env python


import sys

import lib.Create
import lib.QModules.QMain
import lib.QtApplication
from Configs import QDefaults,Config
from lib import gnr,Create
from static import QtLibs






def QGui(*a,**k):
	def Fnx(wgt):
		def Run(wgt):
			def run(wgt):
				wgt=GUI['App']['Fnx']['Run']()
				return wgt
			return run
		wgt['Fnx']={}
		wgt['Fnx']['Configure']	=		wgt[GUI['name']]['Fnx']['Configure']
		wgt['Fnx']['Run']				=		Run(wgt)
		wgt['Fnx']['Add']				=		wgt[GUI['name']]['Fnx']['Add']
		return wgt

	def Init(wgt):
		wgt=wgt['Fnx']['Configure'](wgt)
		return wgt

	GUI 							= 	lib.Create.QCreate(**k)
	GUI								=		Config.make(GUI,**k)
	GUI['App'] 				= 	lib.QtApplication.make(GUI['name'],**k)
	GUI[GUI['name']] 	=	 	lib.QModules.QMain.make(GUI['name'],**k)
	GUI								= 	Fnx(GUI)
	GUI['Elements']		=		GUI[GUI['name']]['Elements']
	GUI['Run']				=		GUI['Fnx']['Run']
	return Init(GUI)

def make(namestr,**k):
	preset={}
	k=Config.preset(['gui',namestr],preset,**k)
	return QGui(**k)

# pTree(d=GUI)

# pTree()
# browse(myPyQt=GUI())