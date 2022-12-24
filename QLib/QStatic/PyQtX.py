#!/usr/bin/env python
# Auth
from inspect import getmodulename
from importlib import import_module
from QLib.QStatic import QtModules

Available={
	'PyQt'	: {
		'v'     :	[],
		'mask'  :	'PyQt{version}',
		'smod'  :    [

    ],}}
compat={**Available}
compat['PyQt']|={'v': [5,6]}

def searchPyQt(compat,available):
	mask=compat['PyQt']['mask']
	v=compat['PyQt']['v']
	return [version for version in v if getmodulename(f'{mask.format(version=version)}.py')]


def importPyQt(**k):
	Available['PyQt']['v']=searchPyQt(compat,Available)
	version=k.get('v') or Available['PyQt']['v'][-1]
	mod=Available['PyQt']['mask'].format(version=version)
	smods=[k.get('module')]
	smods= k.get('modules') or QtModules.QModules
	PyQt= import_module(mod)
	QtCore,QtWidgets,QtGui=[import_module(f'{PyQt.__name__}.{smod}') for smod in smods]
	return PyQt,QtCore,QtWidgets,QtGui


PyQt,QtCore,QtWidgets,QtGui=importPyQt(modules=['QtCore','QtWidgets','QtGui'])





