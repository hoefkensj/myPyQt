#!/usr/bin/env python
# Auth
import sys
def setQtVersion(QtVersion):
	if QtVersion==6:
		from PyQt6 import QtCore,QtWidgets,QtGui
	elif  QtVersion==5:
		from PyQt5 import QtCore,QtWidgets,QtGui
	else:
		sys.exit('no Qt version set')

	QtCore=QtCore
	QtWidgets=QtWidgets
	QtGui=QtGui

	return QtVersion,QtCore,QtWidgets,QtGui,

QtVersion,QtCore,QtWidgets,QtGui=setQtVersion(6)
Qt=QtCore.Qt







