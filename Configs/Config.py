#!/usr/bin/env python
from Configs import mappings
import inspect

def Alias(keymap,k,l):
	l={ keymap[key] : k.pop(key) for key in keymap if key in k}
	return k,l

def mapFnAlias(**k):
	FnValMap={**mappings.FnAliasses}
	f={}
	for item in k:
		if item in FnValMap:
			val=k[item]
			nval=FnValMap.get(item).format(VAL=val)
			f[item]=nval

	# for item in k:
	# 	l={item:(_:=FnValMap.get(item)).format(VAL=VAL) for item in FnValMap if (VAL:=k.get(item))}
	return f,k

def mapAlias(**k):
	AliasMap=mappings.Aliasses
	return {AliasMap[item] :k[item]for item in AliasMap if item in k}


def preset(preconf,name,**k):
	# print(inspect.stack()[1][3])
	k= preconf|k|{'Name':name}
	return k


