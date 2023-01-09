#!/usr/bin/env python
#!/usr/bin/env python
###############################################################################
# # 	Path: /myPyQt/Qlib/QFrames			#	#		License: MIT										#	#
# # 	File: QElements.py							#	#		Created: 2022.05.01-173015.265	#	#
# # 	Author: Hoefkens Jeroen 				#	#		Updated: 2022.05.01-173015.265	# #
#	#		Git:	https://github.com/hoefkensj/myPyQt.git													#	#
###############################################################################
from QLib.QModules import QEditProp
from QLib.QBases import QWidget
from Fnx import QMake
from QLib.QStatic import QtLibs
from pTree import pTree
from Fnx.debug import DebDec
import contextlib
from QLib.QStatic.QtLibs import QCores
from QLib.QElements import  QApplication,QTree,QIconButton,QTextButton,QIconCheckBox,QLabel,QLineEdit

def QModules(**k):
	def Mod():
		mod={}
		mod	|= QMake.Component(QEditProp.make('EditProp'))
		return mod

	# QMake.QBuild('QMdl', 'Wgt', Fnx, **k)
	wgt= QWidget.make('Main',t='V',**k)
	wgt=wgt['Fnx']['Asm'](wgt,Mod,**k)
	# pTree(d=wgt,max=5)
	return wgt['Qtm']['Mtd']['show']

def make(**k):
	app=	QApplication.make('QElements',**k)
	H=	QModules()()

	return 	app['Fnx']['Run']

if __name__ == '__main__':
		Qt=make()
		Qt()
