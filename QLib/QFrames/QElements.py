#!/usr/bin/env python
###############################################################################
# # 	Path: /myPyQt/Qlib/QFrames			#	#		License: MIT										#	#
# # 	File: QElements.py							#	#		Created: 2022.05.01-173015.265	#	#
# # 	Author: Hoefkens Jeroen 				#	#		Updated: 2022.05.01-173015.265	# #
#	#		Git:	https://github.com/hoefkensj/myPyQt.git													#	#
###############################################################################
from QLib.QElements import  QApplication,QTree,QIconButton,QTextButton,QIconCheckBox,QLabel,QLineEdit
from QLib.QBases import QWidget
from Fnx import QMake
from QLib.QStatic import QtLibs
from pTree import pTree
from Fnx.debug import DebDec
import contextlib
from QLib.QStatic.QtLibs import QCores


def QElements(**k):
	def Mod():
		# GUI['Elements']|=gnr.Element(component)
		def trw():
			mod={}
			mod	|= QMake.Component(QTree.make('Tree', cols=7, hidecols=[2, 4, 5, 6]))
			print(mod['Tree']['Qtm']['Mtd']['size']())
			mod	|= QMake.Component(QLabel.make('Label', lbl='test'))
			mod	|= QMake.Component(QLineEdit.make('LEdit'))
			return mod
		def btn():
			mod={}
			mod	|= QMake.Component(QIconButton.make(f'Search', bi=True))
			mod	|= QMake.Component(QIconButton.make(f'Dec', wh=[100, 200]))
			mod	|= QMake.Component(QIconButton.make(f'>', ))
			mod	|= QMake.Component(QIconButton.make(f'<', ))
			mod	|= QMake.Component(QIconButton.make(f'Inc', bi=True))
			mod	|= QMake.Component(QIconButton.make(f'Cpy', bi=True))
			mod	|= QMake.Component(QIconButton.make(f'Reg', bi=True))
			mod	|= QMake.Component(QTextButton.make(f'ikkel', 'ikkel', bi=True))
			mod	|= QMake.Component(QTextButton.make(f'test', bi=True))
			return mod
		trwv=QWidget.make('BtnH',t='V',**k)
		trwv=trwv['Fnx']['Asm'](trwv, trw, **k)
		btnh=QWidget.make('TrWV',t='H', **k)
		btnh=btnh['Fnx']['Asm'](btnh, btn, **k)
		mod={}
		mod|=QMake.Component(trwv)
		mod|=QMake.Component(btnh)
		return mod


	wgt= QWidget.make('Main',t='V',**k)
	wgt=wgt['Fnx']['Asm'](wgt,Mod,**k)
	pTree(d=wgt,max=5)
	return wgt['Qtm']['Mtd']['show']
def make(**k):
	app=	QApplication.make('QElements',**k)
	H=	QElements()()

	return 	app['Fnx']['Run']

if __name__ == '__main__':
		Qt=make()
		Qt()
