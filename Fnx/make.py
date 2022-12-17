#!/usr/bin/env python
# Auth
from QStatic.QtLibs import QCores
from QStatic.QtLibs import QSizePolicies

def Size(wh):
	return QCores['Size'](wh[0], wh[1])

def SizePolicy(pol):
	h,v = pol.split('.')
	return QSizePolicies['Pol'](QSizePolicies[h],QSizePolicies[v])

def Margins(margins):
	return QCores['Margins'](*margins)

def ToolButtonStyle()