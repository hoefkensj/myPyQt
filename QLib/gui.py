#!/usr/bin/env python
from QLib import Create,QModules,gnr
from QLib.QModules import QtApplication,QMain
from Configs import Config

def QGui(*a,**k):
	def Run(wgt):
<<<<<<< HEAD
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
=======
		def run(wgt):
				# w.pop('Elements')
>>>>>>> parent of 5545eeb... Update workspace.xml, QDefaults.py, and 27 more files...

				wgt=gnr.Clean(wgt)
				wgt=wgt['App']['Fnx']['Run']()
				return wgt
		return run
	def Fnx(wgt):
		wgt['Fnx']={}
		wgt['Fnx']['Configure']	=		wgt[w['name']]['Fnx']['Configure']
		wgt['Fnx']['Add']				=		wgt[w['name']]['Fnx']['Add']
		return wgt
	def Init(wgt):
<<<<<<< HEAD
<<<<<<< HEAD
=======
		wgt=wgt['Fnx']['Configure'](wgt)
>>>>>>> parent of 5545eeb... Update workspace.xml, QDefaults.py, and 27 more files...
		wgt.pop('Wgt')
		wgt.pop('Con')
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
