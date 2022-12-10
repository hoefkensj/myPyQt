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
	return w


def ADD(MAIN):
		MAIN['Elements']['trw_Tree']['Fnx']['Add'](GUI=GUI)
def Allign(MAIN):
	s=gnr.Short(MAIN,'Fnx')
	wMax = max(s['Key']['wLbl'](), s['Val']['wLbl']())+10

	s['Key']['Allign'](wMax)
	s['Val']['Allign'](wMax)
GUI=gui.make('Main')
MAIN=GUI['Main']
# GUI['Elements']|=gnr.Element(component)
MAIN['Elements']|= gnr.Element(QTree.make('Tree',cols=7,hidecols=[2,3,4,5,6]))
MAIN['Elements']|= gnr.Element(mod_TreeCtl('TreeCtl'))
MAIN['Elements']|= gnr.Element(QEditProp.make('Key',))
MAIN['Elements']|= gnr.Element(QEditProp.make('Val',))
MAIN['Elements']|= gnr.Element(mod_AppCtl('AppCtl'))

sCon=gnr.Short(MAIN,'Con')
sFnx=gnr.Short(MAIN,'Fnx')
sCon['TreeCtl']['+'](sFnx['Tree']['Mtd']['expandAll'])
sCon['TreeCtl']['-'](sFnx['Tree']['Mtd']['collapseAll'])

# sCon['AppCtl']['Update']()
ADD(MAIN)
sCon['AppCtl']['Print'](MAIN['Elements']['trw_Tree']['Fnx']['PrintTree'])
sCon['AppCtl']['Update'](MAIN['Elements']['trw_Tree']['Fnx']['Update'])
# GUI['Main']=GUI['Main']['Fnx']['Run'](GUI['Main'])
GUI['Fnx']['Main']()
Allign(MAIN)
GUI['Run'](GUI)

print('After')

