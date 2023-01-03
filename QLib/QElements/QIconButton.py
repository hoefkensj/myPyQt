#!/usr/bin/env python
from Configs import QDefaults
from Fnx import QMake

def QIconButton(**k):
	def Fnx(w):
		w['Fnx']={}
		return w
	if not k.get('ico'):
		k|={'ico': k.get('Name')}

	return QMake.QBuild('QElm','iBtn',Fnx,**k)

def make(name, **k):
	return QIconButton(**(QDefaults.QIconButton|k|{'Name':name}))