#!/usr/bin/env python
import QLib.Create
<<<<<<< HEAD
<<<<<<< HEAD
from QLib import gnr,Create
=======
>>>>>>> parent of 5545eeb... Update workspace.xml, QDefaults.py, and 27 more files...
from QLib.QBases import QWidget
from QLib import gnr,Create
from Configs import Config,QDefaults
def QModule(**k):
	def Elements(wgt):
<<<<<<< HEAD
		if a:
			wgt['Elements']=a[0]
		else:
			wgt['Elements']={}
=======
from QLib.QElements import QTextButton,QIconButton,QLineEdit,QLabel
from QLib.QBases import QWidget
from QLib import gnr
from QLib.QElements import QtWgt
from Configs import Config,QDefaults
def QEditProp(**k):


	def Elements(wgt):
		es=[
		QLabel.make('Name',**k|{'pol':'P.P'}),
		# QtWgt.make('Name', pfx='lbl', pol='F.F', k=k),
		QLineEdit.make('Field',ro=1, **k|{'pol':'E.F'}),
		QLineEdit.make('Dupl', **k),
		QTextButton.make('Set', **k|{'pol':'P.P'}),
		QIconButton.make('Edit', bi=1,**k)]
		for e in es:
			wgt['Elements'] |= gnr.Element(e)
>>>>>>> parent of 8640264... Update workspace.xml, QDefaults.py, and 47 more files...
=======
		wgt['Elements']={}
>>>>>>> parent of 5545eeb... Update workspace.xml, QDefaults.py, and 27 more files...
		return wgt

	def Fnx(wgt):
<<<<<<< HEAD
<<<<<<< HEAD
		def Init(wgt):
			wgt=wgt['Fnx']['Generate'](wgt)
			wgt=wgt['Fnx']['Configure'](wgt)
			return wgt



		wgt['Fnx']['Init']	= Init
=======
		# sfn_mdt=gnr.Short(wgt,'Fnx','Mdt')
		sfn_set=gnr.Short(wgt,'Fnx','Set')
		sfn_get=gnr.Short(wgt,'Fnx','Get')
		def TxtText():
			def txtText(text):
				sfn_set['Field']['Text'](text)
				sfn_set['Dupl']['Text'](text)
			return txtText
		def SetText():
			def setText():
				nText= 	sfn_get['Field']['Text']()
				sfn_set['Dupl']['Text'](nText)
				sfn_set['Edit']['Checked'](False)
				sfn_set['Set']['Hidden'](True)
			return setText
		def Edit():
			def edit(state):
				sfn_set['Edit']['Checked'](state)
				sfn_set['Field']['ReadOnly'](not state)
				sfn_set['Set']['Hidden'](not state)
				if not state:
					sfn_set['Field']['Text'](str(sfn_get['Dupl']['Text']()))
			return edit
		def Editable():
			def editable(state):
				sfn_set['Edit']['Hidden'](state)
			return editable
		def Allign(max):
			sfn_set['Name']['Width'](max)
		# def WLbl():
			# return sfn_mdt['Name']['Width']()
		def Init(wgt):
			def init():
				sfn_set['Name']['Text'](sfn_get['Name']['Text']())
				sfn_set['Set']['Hidden'](True)
				sfn_set['Field']['ReadOnly'](True)
				sfn_set['Dupl']['Hidden'](True)
				wgt['Fnx']['Editable'](not k['ed'])
				return Internals(wgt)
			return init
		wgt= QLib.Create.Fnx(wgt)
		wgt['Fnx']['Edit'] 			=	Edit()
		wgt['Fnx']['txtText'] 	=	TxtText()
		wgt['Fnx']['setText']		=	SetText()
		wgt['Fnx']['Editable'] 	=	Editable()
		# wgt['Fnx']['WLbl']			= WLbl
		wgt['Fnx']['Allign']		= Allign
		wgt['Fnx']['Init']			=	Init(wgt)
		return wgt
	def Internals(wgt):
		wgt['Con']['Edit'](wgt['Fnx']['Edit'])
		wgt['Con']['Set'](wgt['Fnx']['setText'])
		wgt['Con']['Field']['returnPressed'](wgt['Fnx']['setText'])
		return wgt
	def Con(wgt):
		sCon=gnr.Short(wgt,'Con')
		sSig=gnr.Short(wgt,'Fnx','Sig')
		wgt['Con'] = wgt.get('Con') or {}
		wgt['Con']['Edit']= sCon['Edit']['clicked']
		wgt['Con']['Set']=	sCon['Set']['clicked']
		wgt['Con']['Field']	= {}
		wgt['Con']['Field']['returnPressed']= sSig['Field']['returnPressed'].connect
>>>>>>> parent of 8640264... Update workspace.xml, QDefaults.py, and 47 more files...
=======
		def Run(wgt):
			wgt['Fnx']['Generate'](wgt)
			return wgt
		wgt= QLib.Create.Fnx(wgt)
		wgt['Fnx']['Run']	=	Run
>>>>>>> parent of 5545eeb... Update workspace.xml, QDefaults.py, and 27 more files...
		return wgt
	def Init(wgt):
<<<<<<< HEAD
<<<<<<< HEAD
		wgt=wgt['Fnx']['Init'](wgt)
=======
		wgt=gnr.QWgtInit(wgt)
>>>>>>> parent of 8640264... Update workspace.xml, QDefaults.py, and 47 more files...
		return wgt
=======
		wgt=wgt['Fnx']['Configure'](wgt)
		wgt=gnr.QWgtInit(wgt)
		return Create.Mtds(wgt)
>>>>>>> parent of 5545eeb... Update workspace.xml, QDefaults.py, and 27 more files...
	w	= QWidget.make(k['name'], **k)
	w	=	Elements(w)
	w	=	Fnx(w)
	w	=	Con(w)
	return 	Init(w)


def make(namestr,**k):
	preset=	QDefaults.QEditProp
	k=Config.preset(['wgt',namestr],preset,**k)
<<<<<<< HEAD
<<<<<<< HEAD
	return QModule(Elements,**k)
=======
	return QEditProp(**k)
>>>>>>> parent of 8640264... Update workspace.xml, QDefaults.py, and 47 more files...
=======
	return QModule(**k)
>>>>>>> parent of 5545eeb... Update workspace.xml, QDefaults.py, and 27 more files...
