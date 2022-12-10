#!/usr/bin/env python
# Auth
import sys
from QLib import gui,gnr
from static.QtLibs import QElements
from QLib.QModules import QHIncDec,QHSearch, QEditProp
from QLib.QElements import QTree,QTextButton
<<<<<<< HEAD
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
=======
from time import sleep,perf_counter_ns
>>>>>>> parent of 8640264... Update workspace.xml, QDefaults.py, and 47 more files...

def pTree(*a, **k):
	d = k.get('d')
	indent = k.get('indent') or 0
	keys=len(d.keys())
	for key in d:
		dkey=f'\x1b[32m{d[key]}()\x1b[0m' if callable(d[key]) else str(d[key])
		keys-=1
		if isinstance(d[key], dict):
			sys.stdout.write('  ┃  ' * (indent))
			sys.stdout.write('  ┗━━ ' if keys == 0 else '  ┣━━ ')
			sys.stdout.write(f'\x1b[1;34m{str(key)}:\x1b[0m\t')
			if len(d[key]) > 200:
				sys.stdout.write(f'\x1b[1;31m(+ {len(d[key])} items)' + '\x1b[0m\n')
			else:
				sys.stdout.write('\n')
				if indent <= k.get('max'):

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
>>>>>>> parent of 5545eeb... Update workspace.xml, QDefaults.py, and 27 more files...

# GUI['Elements'](QSearch.make_QSearch('SearchTree'))
# GUI['Elements'](QSearch.make_QSearchCtl('Search'))
# GUI['Elements'](QHSearch.make('TrSearch'))
# GUI['Fnx']['Add'](  QtWgt.make('trw_RegEx',))
# GUI['Elements'](elements.make_iBtn('Search'))
#

# GUI['Elements']['lbl_Tree']['Mtd']['setText']('Tree')