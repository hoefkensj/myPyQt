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

		'MaximumSize'           :		'''make.Size(k.get('wh'))''',
		'SizePolicy'            :		'''make.SizePolicy(k.get('pol'))''',
		'ContentsMargins'       :		'''make.Margins(k.get('margin'))''',
		'IconSize'              :		'''make.Size(k['isize'])''',
		'ToolButtonStyle'       :		'''make.ToolButtonStyle(k.get('btn')])''',

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



	return l

def mapMake(**k)

mappings={
	'n': {






		'widget'  :			'Widget',


	},
	'v': {
		'Widget'                :		'''k['widget'].get('Name')''',

		'Icon'                  :		'''gnr.Icon(k['ico'])''',


	}
	return n,v

def make(**k):
	c={}
	for kwarg in k:
		if kwarg in nmapping:
			c[nmapping[kwarg]]=vmapping[nmapping[kwarg]]
		else:
			c[kwarg]=k[kwarg]
	return c