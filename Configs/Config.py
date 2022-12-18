#!/usr/bin/env python
from Configs import mappings

def Alias(keymap,k,l):
	l={ keymap[key] : k.pop(key) for key in keymap if key in k}
	return k,l

def mapMakeAlias(**k):
	mapa=mappings.MakeAliases
	l={}
	for item in mapa:
		if item in k:
			VAL=k.pop(item)
			l[mapa[item][0]]=mapa[item][1].format(VAL=VAL)
	return l

def mapAlias(**k):
	mapb=mappings.Aliasses
	for item in mapb:
		if item in k:
			VAL=k.pop(item)
			k[mapb[item]]=VAL
	return k

def Config(wgt,**k):
	from Fnx import make
	j=mapMakeAlias(**k)
	for setting in j:
		k[setting]=eval(j[setting])
	k=mapAlias(**k)
	for setting in k:
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


