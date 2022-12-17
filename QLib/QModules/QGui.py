#!/usr/bin/env python
from QLib.QModules import QMain
from QLib.QElements import QtApplication
from Configs import Config

def QGui(*a,**k):
	def Run(wgt):
		def run(wgt):
			def Execute():
				wgt['App']['Fnx']['Run']()
			return Execute
		return run

	def Fnx(wgt):
		wgt['Fnx']							=		{}
		wgt['Fnx']['Configure']	=		wgt['Main']['Gen']['Config']
		wgt['Fnx']['Add']				=		wgt['Main']['Fnx']['Add']
		wgt['Fnx']['Main']			=		wgt['Main']['Fnx']['Run']
		return wgt['Fnx']

	def Init(wgt):
		wgt['Main']=wgt['Fnx']['Configure'](wgt['Main'],**k)
		return wgt

	w								=		{}
	pfx							=		'gui'
	name						=		k['name']
	w['Name']				=		f'{pfx}_{name}'
	w['name']				=		name
	w['type']				= 	'QGui'
	w['App'] 				= 	QtApplication.make(w['name'], **k)
	w['Main'] 			=	 	QMain.make(w['name'],**k)
	w['Fnx']				= 	Fnx(w)
	w['Run']				=		Run(w)
	return Init(w)

def make(namestr,**k):
	preset={}
	k=Config.preset(['gui',namestr],preset,**k)
	return QGui(**k)
