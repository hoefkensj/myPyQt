#!/usr/bin/env python
# Auth
from QLib.QElements import  QApplication,QTree
from QLib.QBases import QWidget
from Fnx import QMake

def QElements(**k):
	def Mod(m):
		# GUI['Elements']|=gnr.Element(component)
		m['Mod']	|= QMake.Element(QTree.make('Tree',cols=7,hidecols=[2,3,4,5,6]))
		return m['Mod']
	app=	QApplication.make('QElements',**k)
	wgt= QWidget.make('Main',**k)

	wgt['Mod']=Mod(wgt)
	wgt['Asm']()
	wgt['Qt']['Mtd']['show']()
	app['Fnx']['Run']()


def make(**k):
	return QElements(**k)

if __name__ == '__main__':
		make(t='V')