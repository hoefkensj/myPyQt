#!/usr/bin/env python
###############################################################################
# # 	Path: /myPyQt/Qlib/QFrames			#	#		License: MIT										#	#
# # 	File: QElements.py							#	#		Created: 2022.05.01-173015.265	#	#
# # 	Author: Hoefkens Jeroen 				#	#		Updated: 2022.05.01-173015.265	# #
#	#		Git:	https://github.com/hoefkensj/myPyQt.git													#	#
###############################################################################
from QLib.QElements import  QApplication,QTree,QIconButton,QTextButton
from QLib.QBases import QWidget
from Fnx import QMake
from QLib.QStatic import QtLibs
from Fnx.debug import DebDec


def QElements(**k):
	def Mod():
		# GUI['Elements']|=gnr.Element(component)
		def trw():
			mod={}
			mod	|= QMake.Element(QTree.make('Tree',cols=7,hidecols=[2,4,5,6]))
			return mod
		def btn():
			mod={}
			mod	|= QMake.Element(QIconButton.make(f'Search',wh=[15,15], bi=True))
			mod	|= QMake.Element(QIconButton.make(f'Dec', wh=[15,15], bi=True))
			mod	|= QMake.Element(QIconButton.make(f'>', wh=[15,15], bi=True))
			mod	|= QMake.Element(QIconButton.make(f'<', wh=[15,15], bi=True))
			mod	|= QMake.Element(QIconButton.make(f'Inc', wh=[15,15], bi=True))
			mod	|= QMake.Element(QIconButton.make(f'Cpy', wh=[15,15], bi=True))
			mod	|= QMake.Element(QIconButton.make(f'Reg', wh=[15,15], bi=True))
			mod	|= QMake.Element(QTextButton.make(f'ikkel','ikkel', bi=True))
			mod	|= QMake.Element(QTextButton.make(f'test',pol='E.F', bi=True))
			return mod
		return trw()|btn()


	wgt= QWidget.make('Main',**k)
	wgt=wgt['Fnx']['Asm'](wgt,Mod,**k)
	return wgt['Qtm']['Mtd']['show']
def make(**k):
	app=	QApplication.make('QElements',**k)
	H=	QElements(t='V')()

	return 	app['Fnx']['Run']

if __name__ == '__main__':
		Qt=make()
		Qt()
