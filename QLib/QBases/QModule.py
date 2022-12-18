#!/usr/bin/env python
import QLib.Create
from QLib.QBases import QWidget
from QLib import gnr,Create
from Configs import Config,QDefaults
def QModule(**k):

	w	= QWidget.make(k['name'], **k)

	return w


def make(namestr,**k):
	preset=	QDefaults.QEditProp
	k=Config.preset(['mod',namestr],preset,**k)
	return QModule(**k)