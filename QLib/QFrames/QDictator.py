#!/usr/bin/env python
# Auth
import sys
from QLib import gui,gnr
from QLib.QModules import QHIncDec,QHSearch, QEditProp
from QLib.QElements import QTree,QTextButton
from QLib.QBases import QModule

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
	w['Con']['Update'](Update(GUI))
	return w


def Update(GUI):
	s=gnr.Short(GUI)
	sfn=gnr.Short(GUI,'Fnx')
	def update():
		GUI['Main']['Elements']['trw_Tree']['Fnx']['Add'](GUI=GUI)
	return update
def Allign(GUI):
	s=gnr.Short(GUI['Main'])
	wMax = max(s['Key']['Fnx']['wLbl'](), s['Val']['Fnx']['wLbl']()) + 10
	s['Key']['Fnx']['Allign'](wMax)
	s['Val']['Fnx']['Allign'](wMax)
GUI=gui.make('Main')
# GUI['Elements']|=gnr.Element(component)
GUI['Elements']|= gnr.Element(QTree.make('Tree',cols=5,hidecols=[2,3,4]))
GUI['Elements']|= gnr.Element(mod_TreeCtl('TreeCtl'))
GUI['Elements']|= gnr.Element(QEditProp.make('Key',))
GUI['Elements']|= gnr.Element(QEditProp.make('Val',))
GUI['Elements']|= gnr.Element(mod_AppCtl('AppCtl'))

s=gnr.Short(GUI)
sCon=gnr.Short(GUI,'Con')
sFnx=gnr.Short(GUI,'Fnx')
sCon['TreeCtl']['+'](sFnx['Tree']['Mtd']['expandAll'])
sCon['TreeCtl']['-'](sFnx['Tree']['Mtd']['collapseAll'])

GUI['Main']=GUI['Main']['Fnx']['Run'](GUI['Main'])

Allign(GUI)
GUI['Run'](GUI)

print('After')

