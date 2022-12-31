#!/usr/bin/env python
###############################################################################
# # 	Path: /myPyQt/Qlib/QFrames			#	#		License: MIT										#	#
# # 	File: QElements.py							#	#		Created: 2022.05.01-173015.265	#	#
# # 	Author: Hoefkens Jeroen 				#	#		Updated: 2022.05.01-173015.265	# #
#	#		Git:	https://github.com/hoefkensj/myPyQt.git													#	#
###############################################################################
from QLib.QElements import  QApplication,QTree,QIconButton
from QLib.QBases import QWidget
from Fnx import QMake
from QLib.QStatic import QtLibs
from Fnx.debug import DebDec

def QElements(**k):
	def Mod():
		# GUI['Elements']|=gnr.Element(component)
		mod={}
		mod	|= QMake.Element(QTree.make('Tree',cols=7,HideCols=[2,4,5,6]))
		mod	|= QMake.Element(QIconButton.make(f'Search', wh=[15,15], bi=False))
		breakpoint()
		return mod


	app=	QApplication.make('QElements',**k)
	wgt= QWidget.make('Main',**k)

	wgt=wgt['Fnx']['Asm'](wgt,Mod,**k)
	wgt['Qtm']['Mtd']['show']()
	app['Fnx']['Run']()

def make(**k):
	return QElements(**k)

if __name__ == '__main__':
		Q=make(t='V')

