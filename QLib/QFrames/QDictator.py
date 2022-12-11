#!/usr/bin/env python
# Auth
import sys
from QLib import gnr
from QLib.QModules import QGui
from QLib.QModules import QHIncDec,QHSearch, QEditProp
from QLib.QElements import QTree,QTextButton
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
		m['Elements']	|= gnr.Element(QTree.make('Tree',cols=7,hidecols=[2,3,4,5,6]))
		m['Elements']	|= gnr.Element(mod_TreeCtl('TreeCtl'))
		m['Elements']	|= gnr.Element(QEditProp.make('Key',))
		m['Elements']	|= gnr.Element(QEditProp.make('Val',))
		m['Elements']	|= gnr.Element(mod_AppCtl('AppCtl'))
		return m
	def Fnx(m):
		def Select(*a,**k):
			sFnx=gnr.Short(m,'Fnx')
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
		m['Fnx']['Select']=Select
		m['Fnx']['AddDict']=AddDict(m)
		m['Fnx']['Allign']=Allign
		return m
	def Con(m):
		select=m['Fnx']['Select'](m)
		sCon=gnr.Short(m,'Con')
		sFnx=gnr.Short(m,'Fnx')

		sCon['TreeCtl']['+'](sFnx['Tree']['Mtd']['expandAll'])
		sCon['TreeCtl']['-'](sFnx['Tree']['Mtd']['collapseAll'])
		sCon['AppCtl']['Print'](m['Elements']['trw_Tree']['Fnx']['PrintTree'])
		sCon['AppCtl']['Update'](m['Elements']['trw_Tree']['Fnx']['Update'])
		sCon['Tree']['Item'](select)
		return m
	def Init(g):
		g['Main']['Fnx']['Allign'](g['Main'])
		return GUI['Run'](GUI)

	GUI= QGui.make('Main')
	MAIN=GUI['Main']
	MAIN=Elements(MAIN)
	MAIN=Fnx(MAIN)
	MAIN=Con(MAIN)
	GUI['Add']=MAIN['Fnx']['AddDict']
	GUI['Fnx']['Main']()
	return Init(GUI),GUI,GUI['Add']



RUN,GUI,ADD=QDictator()
ADD(GUI=GUI)
RUN()





