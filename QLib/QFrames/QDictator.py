#!/usr/bin/env python
# Auth
import sys
from QLib import gui,gnr
from static.QtLibs import QElements
from QLib.QModules import QHIncDec,QHSearch, QEditProp
from QLib.QElements import QTree,QTextButton
<<<<<<< HEAD
from QLib.QBases import QModule


def QDictator(**k):
	def Elements(m):
		def mod_TreeCtl(name):
			w=QModule.make(name)
			w['Elements']|=gnr.Element(QHIncDec.make('ColEx',wh=[20,20]))
			w['Elements']|=gnr.Element(QHSearch.make('TreeSearch',))
			w=w['Fnx']['Run'](w)
			sfn=gnr.Short(w,'Con')
			w['Con']['+']=sfn['ColEx']['Inc']
			w['Con']['-']=sfn['ColEx']['Dec']
			return w
		def mod_AppCtl(name):

			w=QModule.make(name)
			w['Elements']|= gnr.Element(QTextButton.make('Update',pol='E.P',))
			w['Elements']|= gnr.Element(QTextButton.make('Print',pol='E.P',))
			w['Elements']|= gnr.Element(QTextButton.make('Exit',pol='E.P',))
			w=w['Fnx']['Run'](w)
			sfn=gnr.Short(w,'Con','clicked')
			w['Con']['Update']=sfn['Update']
			w['Con']['Print']=sfn['Print']
			w['Con']['Exit']=sfn['Exit']
			w['Con']['Exit'](sys.exit)
			return w
		# GUI['Elements']|=gnr.Element(component)
		m['Elements']	|= gnr.Element(QTree.make('Tree',cols=7,))##hidecols=[2,3,4,5,6]
		m['Elements']	|= gnr.Element(mod_TreeCtl('TreeCtl'))
		m['Elements']	|= gnr.Element(QEditProp.make('Key',))
		m['Elements']	|= gnr.Element(QEditProp.make('Val',))
		m['Elements']	|= gnr.Element(mod_AppCtl('AppCtl'))
	def Fnx(m):
		def Select(*a,**k):
			sFnx=gnr.Short(MAIN,'Fnx')
			txtBox = [sFnx['Key']['txtText'], sFnx['Val']['txtText']]
			def select(data):
				for idx, txtbox in zip([0, 1, 2], txtBox):
					txtbox(data.text(idx))
			return select
		def AddDict(m):
			def adddict(**k):
				#use adddict(NAME=DICT)
				m['Elements']['trw_Tree']['Fnx']['Add'](**k)
			return adddict
		def Allign(m):
			s=gnr.Short(m,'Fnx')
			wMax = max(s['Key']['wLbl'](), s['Val']['wLbl']())+10
			s['Key']['Allign'](wMax)
			s['Val']['Allign'](wMax)
		m['Fnx']={}
		m['Fnx']['Select']=Select
		m['Fnx']['AddDict']=AddDict(m)
		m['Fnx']['Allign']=Allign
		return m
	def Con(m):
		select=Select(m)
		sCon=gnr.Short(m,'Con')
		sFnx=gnr.Short(m,'Fnx')
		sCon['TreeCtl']['+'](sFnx['Tree']['Mtd']['expandAll'])
		sCon['TreeCtl']['-'](sFnx['Tree']['Mtd']['collapseAll'])
		sCon['AppCtl']['Print'](m['Elements']['trw_Tree']['Fnx']['PrintTree'])
		sCon['AppCtl']['Update'](m['Elements']['trw_Tree']['Fnx']['Update'])
		sCon['Tree']['Item'](select)
		return m


	GUI=gui.make('Main')
	MAIN=GUI['Main']
	MAIN=Fnx(MAIN)
	MAIN=Con(MAIN)
	GUI['Fnx']['Main']()


addDict(MAIN)
Allign(MAIN)
GUI['Run'](GUI)
>>>>>>> parent of 5545eeb... Update workspace.xml, QDefaults.py, and 27 more files...

# GUI['Elements'](QSearch.make_QSearch('SearchTree'))
# GUI['Elements'](QSearch.make_QSearchCtl('Search'))
# GUI['Elements'](QHSearch.make('TrSearch'))
# GUI['Fnx']['Add'](  QtWgt.make('trw_RegEx',))
# GUI['Elements'](elements.make_iBtn('Search'))
#

		# def saveDialog():
		# 	def saveDialog():
		# 		Path, Type =QtWidgets.QFileDialog.getSaveFileName(QtWidgets.QWidget(),"Save As","","All Files (*)")
		# 		return Path
		# 	return saveDialog()



