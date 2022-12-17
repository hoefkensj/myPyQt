#!/usr/bin/env python

Aliasses={
		'Name'    	: 		'ObjectName',
		'bi'      	:			'Checkable',
		'lbl'     	:			'Text',
		'cols'    	:			'ColumnCount',
		'ro'      	:			'ReadOnly',
		'pol'     	:			'SizePolicy',
		'margins'  	:			'ContentsMargins',
		'btnstyle'  :			'ToolButtonStyle',
		'ico'     	:			'Icon',
		}

SizeAliasses={
		'mx':			'MaximumSize',
		'mn':			'MinimumSize',
		'ico':		'IconSize',
	}

Makes={
		'MaximumSize'           :		'''make.Size({MAKE})''',
		'MinimumSize'           :		'''make.Size({MAKE})''',
		'SizePolicy'            :		'''make.SizePolicy('{MAKE}')''',
		'ContentsMargins'       :		'''make.Margins({MAKE})''',
		'IconSize'              :		'''make.Size({MAKE})''',
		'ToolButtonStyle'       :		'''make.ToolButtonStyle({MAKE})''',
		'Icon'                  :		'''make.Icon({MAKE})'''
		}

def mapAlias(**k):
	l={}
	for key in Aliasses:
		if k.get(key):
			l[Aliasses[key]]=k.pop(key)

	if k.get('size'):
		m=k.pop('size')
		for key in SizeAliasses:
			if m.get(key):
				l[SizeAliasses[key]]=m.get(key)
	return l|k

def mapMakes(**k):
	l={}
	for key in Makes:
		if key in k:
			MAKE=k.get(key)
			print(key)
			l[key]=Makes[key].format(MAKE=MAKE)
			print(key,Makes[key].format(MAKE=MAKE))
	return l
def make(**k):
	k=mapAlias(**k)
	k=mapMakes(**k)
	return k