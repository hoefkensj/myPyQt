#!/usr/bin/env python


import sys

import lib.Create
import lib.QModules.QMain
import lib.QtApplication
from Configs import QDefaults,Config
from lib import gnr






def QGui(*a,**k):
	def Fnx(wgt):


		wgt['Main']=gnr.Fnx(wgt['Main'])
		wgt['Fnx']=wgt['Main']['Fnx']
		wgt['Fnx']['CfgElements']=CfgElements
		wgt['Fnx']['Add']			=	wgt['Main']['Add']
		wgt['Fnx']['Run']			=	Run()
		return wgt

	def Init(wgt):
		wgt['Main']=gnr.minInit(GUI['Main'])
		return wgt

	GUI 							= lib.Create.QCreate(**k)
	GUI['App'] 				= 	lib.QtApplication.make(GUI['name'],**k)
	GUI['Main'] 			=	 	lib.QModules.QMain.make(GUI['name'],**k)
	GUI								= 	Fnx(GUI)
	GUI['Elements']		=		GUI['Main']['Elements']
	GUI['Fnx']				=		GUI['Main']['Fnx']

	return Init(GUI)

def make(namestr,**k):
	preset={}
	k=Config.preset(['gui',namestr],preset,**k)
	return QGui(**k)

# pTree(d=GUI)

# pTree()
# browse(myPyQt=GUI())