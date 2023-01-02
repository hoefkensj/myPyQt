#!/usr/bin/env python
from QLib import Create
from Configs import QDefaults
from Configs import Config
from Fnx import QMake
from assets import ico
from QLib.QStatic.PyQtX import QtGui


def QIconButton(**k):
	def Fnx(w):
		w['Fnx']={}
		return w
	if not k.get('ico'):
		k|={'ico': k.get('Name')}

	return QMake.QBuild('QElm','iBtn',Fnx,**k)

def make(name, **k):
	return QIconButton(**(QDefaults.QIconButton|k|{'Name':name}))