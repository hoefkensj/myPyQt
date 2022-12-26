#!/usr/bin/env python
from Configs import mappings

def Alias(keymap,k,l):
	l={ keymap[key] : k.pop(key) for key in keymap if key in k}
	return k,l

def mapFnAlias(**k):
	FnValMap={**mappings.FnAliasses}
	for item in k:
		l={item:(_:=FnValMap.get(item)).format(VAL) for item in FnValMap if (VAL:=k.get(item))}
	return l

def mapAlias(**k):
	AliasMap=mappings.Aliasses
	return {AliasMap[item] :k[item]for item in AliasMap if item in k}


def preset(preconf,name,**k):
	k= preconf|k|{'Name':name}
	return k


