#!/usr/bin/env python
from Configs import QDefaults
from Fnx import QMake


def QTextButton(**k):
	def Fnx(w):
		w['Fnx']={}
		return w
	return QMake.QBuild('QElm','tBtn',Fnx,**k)

def make(name,*lbl, **k):
	lbl={'lbl':lbl[0]} if lbl else {'lbl': name}
	return QTextButton(**(QDefaults.QTextButton|k|{'Name':name}|{**lbl}))
