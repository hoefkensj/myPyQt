#!/usr/bin/env python
###############################################################################
# # 	Path: /myPyQt/Qlib/QFrames			#	#		License: MIT										#	#
# # 	File: QElements.py							#	#		Created: 2022.05.01-173015.265	#	#
# # 	Author: Hoefkens Jeroen 				#	#		Updated: 2022.05.01-173015.265	# #
#	#		Git:	https://github.com/hoefkensj/myPyQt.git													#	#
###############################################################################
from QLib.QElements import  QApplication,QTree,QIconButton,QTextButton,QIconCheckBox
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
			# mod	|= QMake.Element(QIconCheckBox.make('Reg'))
			return mod
		def btn():
			mod={}
			mod	|= QMake.Element(QIconButton.make(f'Search', bi=True))
			mod	|= QMake.Element(QIconButton.make(f'Dec',))
			mod	|= QMake.Element(QIconButton.make(f'>', wh=[15,15], ))
			mod	|= QMake.Element(QIconButton.make(f'<', wh=[15,15], ))
			mod	|= QMake.Element(QIconButton.make(f'Inc', wh=[15,15], bi=True))
			mod	|= QMake.Element(QIconButton.make(f'Cpy', wh=[15,15], bi=True))
			mod	|= QMake.Element(QIconButton.make(f'Reg', wh=[15,15], bi=True))
			mod	|= QMake.Element(QTextButton.make(f'ikkel','ikkel', bi=True))
			mod	|= QMake.Element(QTextButton.make(f'test',pol='F.F', bi=True))
			return mod
		trwv=QWidget.make('BtnH',t='H',**k)
		trwv=trwv['Fnx']['Asm'](trwv, trw, **k)
		btnh=QWidget.make('TrWV',t='H',**k)
		btnh=btnh['Fnx']['Asm'](btnh, btn, **k)
		mod={}
		mod|=QMake.Element(trwv)
		mod|=QMake.Element(btnh)
		return mod


	wgt= QWidget.make('Main',t='V',**k)
	wgt=wgt['Fnx']['Asm'](wgt,Mod,**k)
	return wgt['Qtm']['Mtd']['show']
def make(**k):
	app=	QApplication.make('QElements',**k)
	H=	QElements()()

	return 	app['Fnx']['Run']

if __name__ == '__main__':
		Qt=make()
		Qt()
