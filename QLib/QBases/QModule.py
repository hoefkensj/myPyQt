#!/usr/bin/env python
from QLib.QBases import QWidget
from Configs import QDefaults
from Configs import Config

def QModule(**k):

	w	= QWidget.QMake(k['name'], **k)

	return w


def make(namestr,**k):
	preset=	QDefaults.QEditProp
	k= Config.preset(['mod', namestr], preset, **k)
	return QModule(**k)