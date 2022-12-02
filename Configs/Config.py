#!/usr/bin/env python
from lib import gnr
from static import QtLibs
from static.QtLibs import QToolButtons
from Configs import QDefaults
def make(wgt,**k):
	nmapping={
		'Name'		: 		'ObjectName',
		'pol'			:			'SizePolicy',
		'bi'			:			'Checkable',
		'wh'			:			'MaximumSize',
		'btn'			:			'ToolButtonStyle',
		'margin'	:			'ContentsMargins',
		'ico'			:			'Icon',
		'isize'		:			'IconSize',
		'txt'			:			'Text',
		'cols'		:			'ColumnCount',
	}
	vmapping={
		'ObjectName'						:		'''wgt['Name']''',
		'SizePolicy'						:		'''gnr.makeSizePolicy(k.get('pol'))''',
		'Checkable'							:		'''k.get('bi')''',
		'MaximumSize'						:		'''gnr.makeSize(k.get('wh'))''',
		'ToolButtonStyle'				:		'''QtLibs.QToolButtons[k.get('btn')]''',
		'ContentsMargins'				:		'''gnr.makeMargins(k.get('margin'))''',
		'Icon'									:		'''gnr.Icon(k['ico'])''',
		'IconSize'							:		'''gnr.makeSize(k['isize'])''',
		'Text'									:		'''wgt['name'].split('_')[0]''',
		'ColumnCount'						:		'''k.get('cols')''',

	}

	c={}
	for kwarg in k:
		if kwarg in nmapping:
			c[nmapping[kwarg]]=eval(vmapping[nmapping[kwarg]])
		else:
			c[kwarg]=k[kwarg]
	wgt['Cfg']= wgt.get('Cfg') or {}
	wgt['Cfg']|=c
	return wgt



def names(*a):
	names={
			'pfx'    :	f'{a[0]}'								,
			'name'   :	f'{a[1]}{"_" if len(a)>2 else ""}{a[-1]if len(a)>2 else ""}',
	}
	return names

def preset(preconf,**k):
	naming=preconf.pop('Names')
	k=QDefaults.Properties | preconf |	k	|	names(*naming)
	return k
