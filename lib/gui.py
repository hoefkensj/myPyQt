#!/usr/bin/env python
import sys
from  PyQt5.QtWidgets import QWidget,QApplication
from wgt import  Wgt
from tree import Tree
from pyDictatorQt import browse

def App():
	from sys import argv
	
	a = {}
	a['QtApp'] = QApplication(argv)
	a['Clip'] = a['QtApp'].clipboard()
	return a
	


def pTree(*a, **k):
	d = k.get('d')
	indent = k.get('indent') or 0
	for key in d:
		if isinstance(d[key], dict):
			sys.stdout.write('  ┃  ' * (indent) + '  ┣━━ ' + '\x1b[1;32m' + str(key) + ':' + '\x1b[0m\n')
			if len(d[key]) > 10:
				sys.stdout.write('  ┃  ' * (indent) + '  ┣━━ ' + '(+ ' + str(len(d[key])) + ' items)' + '\n')
			else:
				Tree(d=d[key], indent=indent + 1)
		else:
			sys.stdout.write('  ┃  ' * (indent) + '  ┣━━ ' + str(key) + '\t:\t' + str(d[key]) + '\n')



def GUI():
	def elements():
		wgtTree = Tree(n='Tree')
		e = {}
		e['wgtTree'] = wgtTree
		return e
	def place():
		GUI['Main']['Fnx']['Add'](GUI['Elements']['wgtTree'])


	GUI = {}
	GUI['App'] = App()
	GUI['Main'] = Wgt(n='Qt5', t='V')
	GUI['Elements']=elements()
	place()
	pTree(d=GUI)
	
	return GUI





browse(myPyQt=GUI())