#!/usr/bin/env python
from QLib import Create
from Configs import QDefaults
from Configs import Config
from Fnx import QMake
from assets import ico

def QIconButton(**k):
	def Fnx(w):
		w['Fnx']={}
		return w
	return QMake.QBuild('QElm','iBtn',Fnx,**k)

def make(name, **k):
	icons={'ico': QMake.IconSet(name)}
	return QIconButton(**(QDefaults.QIconButton|k|{**icons}|{'Name':name}))