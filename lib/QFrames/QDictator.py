#!/usr/bin/env python
# Auth
import sys
from lib import gui,gnr
from static.QtLibs import QElements
from lib.QModules import QHIncDec,QHSearch, QEditProp
from lib.QElements import QTree,QTextButton
from time import sleep

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
	s=gnr.ShortNames(GUI)
	def update():
		GUI['Main']['Elements']['trw_Tree']['Fnx']['Add'](GUI=GUI)
		x=s['TreeSearch']['Fnx']['x']()
		y=s['TreeSearch']['Fnx']['y']()
		w=s['TreeSearch']['Fnx']['width']()
		w=s['TreeSearch']['Els']['Field']['Fnx']['Set']['MinimumWidth'](w+20)

	return update


GUI=gui.make('Main')

# GUI['Elements']|=gnr.Element(component)

GUI['Elements']|= gnr.Element(QTree.make('Tree',cols=5,hidecols=[2,3,4]))
GUI['Elements']|= gnr.Element(QHSearch.make('Tree'))
GUI['Elements']|= gnr.Element(QEditProp.make('Key'))
GUI['Elements']|= gnr.Element(QEditProp.make('Val'))
GUI['Elements']|= gnr.Element(QTextButton.make('Update',pol='E.P'))

# GUI['Elements']|= gnr.Element(QHSearch.make('Search'))
# GUI['Main']['Elements'] |= gnr.Element(QtWgt.make('iBtn_Edit'))
# GUI['Main']['Lay']['Lay'].addWidget(GUI['Main']['Elements']['iBtn_Edit']['Wgt'])
# pTree(d=GUI)+

GUI['Main']=GUI['Main']['Fnx']['Run'](GUI['Main'])

# GUI['Fnx']['Configure'](GUI['Main'])
# pTree(d=GUI,max=5000)
upd=Update(GUI)
GUI['Elements']['tBtn_Update']['Con']['clicked'](upd)
GUI['Run'](GUI['Main'])





# GUI['Elements'](QSearch.make_QSearch('SearchTree'))
# GUI['Elements'](QSearch.make_QSearchCtl('Search'))
# GUI['Elements'](QHSearch.make('TrSearch'))
# GUI['Fnx']['Add'](  QtWgt.make('trw_RegEx',))
# GUI['Elements'](elements.make_iBtn('Search'))
#

# GUI['Elements']['lbl_Tree']['Mtd']['setText']('Tree')