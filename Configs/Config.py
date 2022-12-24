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


def preset(preconf,**k):
	k= preconf |	k
	return k


