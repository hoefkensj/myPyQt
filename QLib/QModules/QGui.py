#!/usr/bin/env python
from QLib import QModules
from QLib.QModules import QtApplication,QMain
from Configs import Config

def QGui(*a,**k):
	def Run(wgt):
		def run(wgt):
			def Execute():
				wgt['App']['Fnx']['Run']()
			return Execute
		return run
	def Fnx(wgt):
		wgt['Fnx']={}
		wgt['Fnx']['Configure']	=		wgt[w['name']]['Fnx']['Configure']
		wgt['Fnx']['Add']				=		wgt[w['name']]['Fnx']['Add']
		wgt['Fnx']['Main']	=				wgt[w['name']]['Fnx']['Run']
		return wgt['Fnx']
	def Init(wgt):
		wgt=wgt['Fnx']['Configure'](wgt)
		return wgt

	w								=		{}
	pfx							=		'gui'
	name						=		k['name']
	w['Name']				=		f'{pfx}_{name}'
	w['name']				=		name
	w['type']				= 	'QGui'
	w['App'] 				= 	QModules.QtApplication.make(w['name'], **k)
	w['Main'] 			=	 	QModules.QMain.make(w['name'],**k)
	w 							= 	Config.make(w, **k)
	w['Fnx']				= 	Fnx(w)
	w['Run']				=		Run(w)
	return Init(w)

def make(namestr,**k):
	preset={}
	k=Config.preset(['gui',namestr],preset,**k)
	return QGui(**k)
