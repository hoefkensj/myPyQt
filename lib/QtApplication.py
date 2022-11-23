#!/usr/bin/env python
# Auth
from sys import argv
from .PyQtX import QApplication

def QtApplication():

	a = {}
	a['QtApp'] = QApplication(argv)
	a['Clip'] = a['QtApp'].clipboard()
	return a