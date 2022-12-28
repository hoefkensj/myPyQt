#!/usr/bin/env python
# Auth
from QLib.QElements import  QApplication,QTree
from QLib.QBases import QWidget
from Fnx import QMake
from QLib.QStatic import QtLibs
from Fnx.debug import DebDec


def lFn(w,construct,**k):
	fns=k.get('fn')
	fnn={fn.__name__:fn for fn in fns}
	n=construct.__name__
	if n in fnn:
		w=construct(w,fn=fnn[n])


def QElements(**k):
	def Mod():
		# GUI['Elements']|=gnr.Element(component)
		mod={}
		mod	|= QMake.Element(QTree.make('Tree',cols=7,HideCols=[2,4,5,6]))
		return mod
	app=	QApplication.make('QElements',**k)
	breakpoint()
	wgt= QWidget.make('Main',**k)

	wgt['Mod']=Mod()
	wgt=wgt['Fnx']['Asm'](wgt)
	breakpoint()



	wgt['Qtm']['Mtd']['show']()
	app['Fnx']['Run']()


def make(**k):
	return QElements(**k)

if __name__ == '__main__':
		Q=make(t='V')

