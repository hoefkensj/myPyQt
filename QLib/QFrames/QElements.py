#!/usr/bin/env python
# Auth
from QLib.QElements import  QApplication,QTree
from QLib.QBases import QWidget
from Fnx import QMake
from Fnx.debug import DebDec


def lFn(w,construct,**k):
	fns=k.get('fn')
	fnn={fn.__name__:fn for fn in fns}
	n=construct.__name__
	if n in fnn:
		w=construct(w,fn=fnn[n])


def QElements(**k):
	def Mod(m):
		# GUI['Elements']|=gnr.Element(component)
		m['Mod']	|= QMake.Element(QTree.make('Tree',cols=7,HideCols=[2,4,5,6]))
		return m
	app=	QApplication.make('QElements',**k)
	wgt= QWidget.make('Main',**k)
	wgt=Mod(wgt)

	w=QtLibs.QElements.get('wgt')()
	for construct in QMake.Construct('QBse'):
		w=lFn(w,construct,fn=[Mod,])

		if construct.__name__=='Mod':
			w=construct(w,fn=Mod)
			continue

	wgt['Qtm']['Mtd']['show']()
	breakpoint()
	app['Fnx']['Run']()


def make(**k):
	return QElements(**k)

if __name__ == '__main__':
		Q=make(t='V')

