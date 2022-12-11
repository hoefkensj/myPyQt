#!/usr/bin/env python
from QLib import Create,QModules,gnr
from QLib.QModules import QtApplication,QMain
from Configs import Config
from static import QtLibs

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
		return wgt
	def Init(wgt):
		wgt=wgt['Fnx']['Configure'](wgt)
		return wgt
	pfx			=	k['pfx']
	type		=	QtLibs.QElements.get(pfx).__name__ if QtLibs.QElements.get(pfx) else None
	name		=	k['name']
	w				=	{
			'Name'    :	f'{pfx}_{name}'			,
			'name'    :	name								,
			'type'    :	type								,}
	w['App'] 				= 	QModules.QtApplication.make(w['name'], **k)
	w[w['name']] 		=	 	QModules.QMain.make(w['name'],**k)
	w = Config.make(w, **k)
	w								= 	Fnx(w)
	w['Run']				=		Run(w)
	return Init(w)

def make(namestr,**k):
	preset={}
	k=Config.preset(['gui',namestr],preset,**k)
	return QGui(**k)
