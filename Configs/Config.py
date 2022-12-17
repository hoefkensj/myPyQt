#!/usr/bin/env python
import Fnx
from Fnx import make
from QLib import gnr
from QStatic import QtLibs
from QStatic.QtLibs import QToolButtons
from Configs import QDefaults



	def config(wgt,**k):
		c=make(**k)
		for setting in c:
			print(setting,c[setting])
			if setting not in vmapping:
				wgt['Cfg'][setting]=c[setting]
				continue
			wgt['Cfg'][setting]=eval(c[setting])

		return wgt

	return config




def names(*a):
	names={
			'pfx'    :	f'{a[0]}'								,
			'name'   :	f'{a[1]}{"_" if len(a)>2 else ""}{a[-1]if len(a)>2 else ""}',
	}
	return names

def preset(naming,preconf,**k):
	k= preconf |	k |names(*naming)
	return k


