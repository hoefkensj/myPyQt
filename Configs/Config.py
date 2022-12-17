#!/usr/bin/env python

from Fnx import make

from Configs import QDefaults,mappings

def isMake(setval):
	return setval.startswith('make.')


def Config(wgt,**k):
	k=mappings.mapAlias(**k)
	m=mappings.mapMakes(**k)
	for setting in m:
		k[setting]=eval(m[setting])

	for setting in k:
		print(setting,k[setting])
		wgt['Cfg'][setting]=k[setting]
	return wgt



def names(*a):
	names={
			'pfx'    :	f'{a[0]}'								,
			'name'   :	f'{a[1]}{"_" if len(a)>2 else ""}{a[-1]if len(a)>2 else ""}',
	}
	return names

def preset(naming,preconf,**k):
	k= preconf |	k |names(*naming)
	return k


