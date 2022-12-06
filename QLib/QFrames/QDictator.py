#!/usr/bin/env python
# Auth
import sys
from QLib import gui,gnr
from static.QtLibs import QElements
from QLib.QModules import QHIncDec,QHSearch, QEditProp
from QLib.QElements import QTree,QTextButton
from time import sleep,perf_counter_ns

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

					pTree(d=d[key], indent=indent + 1,max=k.get('max'))
		else:
			sys.stdout.write('  ┃  ' * (indent))
			sys.stdout.write('  ┗━━ ' if keys == 0 else '  ┣━━ ')
			sys.stdout.write(f'{str(key)}\t:\t{dkey}\n')
def Update(GUI):
	s=gnr.Short(GUI)
	sfn=gnr.Short(GUI,'Fnx')
	sTS_sfn=gnr.Short(s['TreeSearch'],'Fnx')
	def update():
		GUI['Main']['Elements']['trw_Tree']['Fnx']['Add'](GUI=GUI)
		x=sfn['TreeSearch']['x']()
		y=sfn['TreeSearch']['y']()
		w=sfn['TreeSearch']['width']()
		w=sTS_sfn['Field']['Set']['MinimumWidth'](w+20)

	return update
def Allign(GUI):
	s=gnr.Short(GUI)
	wkey=s['Key']['Fnx']['wLbl']()
	wval=s['Val']['Fnx']['wLbl']()
	wMax=max(wkey,wval)+10
	s['Key']['Fnx']['Allign'](wMax)
	s['Val']['Fnx']['Allign'](wMax)



GUI=gui.make('Main')

# GUI['Elements']|=gnr.Element(component)
GUI['Elements']|= gnr.Element(QTree.make('Tree',cols=5,hidecols=[2,3,4]))
# GUI['Elements']|= gnr.Element(QHIncDec.make('ColEx',pol='P.P'))
GUI['Elements']|= gnr.Element(QHSearch.make('TreeSearch',))
GUI['Elements']|= gnr.Element(QEditProp.make('Key',))
GUI['Elements']|= gnr.Element(QEditProp.make('Val',))
GUI['Elements']|= gnr.Element(QTextButton.make('Update',pol='E.P',))


GUI['Main']=GUI['Main']['Fnx']['Run'](GUI['Main'])
# GUI['Fnx']['Configure'](GUI['Main'])
# pTree(d=GUI,max=5000)
Allign(GUI)
upd=Update(GUI)
GUI['Elements']['tBtn_Update']['Con']['clicked'](upd)
GUI['Run'](GUI)



# GUI['Elements'](QSearch.make_QSearch('SearchTree'))
# GUI['Elements'](QSearch.make_QSearchCtl('Search'))
# GUI['Elements'](QHSearch.make('TrSearch'))
# GUI['Fnx']['Add'](  QtWgt.make('trw_RegEx',))
# GUI['Elements'](elements.make_iBtn('Search'))
#

# GUI['Elements']['lbl_Tree']['Mtd']['setText']('Tree')