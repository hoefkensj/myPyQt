#!/usr/bin/env python
from QLib import Create,QModules,gnr
from QLib.QModules import QtApplication,QMain
from Configs import Config

def QGui(*a,**k):
	def Run(wgt):
<<<<<<< HEAD
		def run():
			wgt['Fnx']['Run']()
			wgt['App']['Fnx']['Run']()
			return
=======
		def run(wgt):
				# w.pop('Elements')
				# w.pop('Wgt')
				# w.pop('Con')
				# w.pop('Lay')
				wgt=gnr.Clean(wgt)
				wgt=wgt['App']['Fnx']['Run']()
				return wgt
>>>>>>> parent of 8640264... Update workspace.xml, QDefaults.py, and 47 more files...
		return run

	def Fnx(wgt):
		wgt['Fnx']={}
		wgt['Fnx']['Configure']	=		wgt[w['name']]['Fnx']['Configure']
		wgt['Fnx']['Add']				=		wgt[w['name']]['Fnx']['Add']
		wgt['Fnx']['Show']			=		wgt[w['name']]['Fnx']['Show']
		wgt['Fnx']['Run']				=		wgt[w['name']]['Fnx']['Run']
		return wgt
	def Init(wgt):
<<<<<<< HEAD
		wgt.pop('Wgt')
		wgt.pop('Lay')
=======
		wgt=wgt['Fnx']['Configure'](wgt)
>>>>>>> parent of 8640264... Update workspace.xml, QDefaults.py, and 47 more files...
		return wgt
	w 							= 	Create.QEmpty(**k)
	w['App'] 				= 	QModules.QtApplication.make(w['name'], **k)
	w[w['name']] 		=	 	QModules.QMain.make(w['name'],**k)
	w								= 	Fnx(w)
	w['Elements']		=		w[w['name']]['Elements']
	w['Run']				=		Run(w)
	return Init(w)

def make(namestr,**k):
	preset={}
	k=Config.preset(['gui',namestr],preset,**k)
	return QGui(**k)
