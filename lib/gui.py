#!/usr/bin/env python
from lib import Create,QModules,QtApplication
from Configs import Config

def QGui(*a,**k):
	def Fnx(wgt):
		def Run(wgt):
			def run(wgt):
				wgt=w['App']['Fnx']['Run']()
				return wgt
			return run
		wgt['Fnx']={}
		wgt['Fnx']['Configure']	=		wgt[w['name']]['Fnx']['Configure']
		wgt['Fnx']['Run']				=		Run(wgt)
		wgt['Fnx']['Add']				=		wgt[w['name']]['Fnx']['Add']
		return wgt

	def Init(wgt):
		wgt=wgt['Fnx']['Configure'](wgt)
		return wgt

	w 							= 	Create.Empty(**k)
	w								=		Config.make(w,**k)
	w['App'] 				= 	QtApplication.make(w['name'],**k)
	w[w['name']] 	=	 	QModules.QMain.make(w['name'],**k)
	w								= 	Fnx(w)
	w['Elements']		=		w[w['name']]['Elements']
	w['Run']				=		w['Fnx']['Run']
	return Init(w)

def make(namestr,**k):
	preset={}
	k=Config.preset(['gui',namestr],preset,**k)
	return QGui(**k)

# pTree(d=w)

# pTree()
# browse(myPyQt=w())