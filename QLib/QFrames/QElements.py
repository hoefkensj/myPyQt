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
		mod={}
		# mod	|= QMake.Element(QTree.make('Tree',cols=7,HideCols=[2,4,5,6]))
		mod	|= QMake.Element(QIconButton.make(f'Search',wh=[15,15], bi=True))

		mod	|= QMake.Element(QIconButton.make(f'Dec', wh=[15,15], bi=True))

		mod	|= QMake.Element(QIconButton.make(f'>', wh=[15,15], bi=False))
		mod	|= QMake.Element(QIconButton.make(f'Inc', wh=[15,15], bi=True))
		mod	|= QMake.Element(QIconButton.make(f'Reg', wh=[15,15], bi=True))
		mod	|= QMake.Element(QIconButton.make(f'<', wh=[15,15], bi=False))
		mod	|= QMake.Element(QTextButton.make(f'ikkel','ikkel', bi=True))
		mod	|= QMake.Element(QTextButton.make(f'test',pol='E.F', bi=False))
		return mod

	def hv(**k):
		h=QWidget.make('H',t='H',**k)
		h=h['Fnx']['Asm'](h,Mod,**k)
		v=QWidget.make('V',t='V',**k)
		v=v['Fnx']['Asm'](v,Mod,**k)
		mod={}
		mod	|= QMake.Element(h)
		mod	|= QMake.Element(v)
		return mod

	wgt= QWidget.make('Main',**k)
	wgt=wgt['Fnx']['Asm'](wgt,hv,**k)
	return wgt['Qtm']['Mtd']['show']
def make(**k):
	app=	QApplication.make('QElements',**k)
	H=	QElements(t='H')()

	return 	app['Fnx']['Run']

if __name__ == '__main__':
		Qt=make()
		Qt()
