#!/usr/bin/env python
import Fnx
from Fnx import make
from QLib import gnr

from static import QtLibs
from static.QtLibs import QToolButtons
from Configs import QDefaults
def make(wgt,**k):
	nmapping={
		'Name'    : 		'ObjectName',
		'pol'     :			'SizePolicy',
		'bi'      :			'Checkable',
		'wh'      :			'MaximumSize',
		'btn'     :			'ToolButtonStyle',
		'margin'  :			'ContentsMargins',
		'ico'     :			'Icon',
		'isize'   :			'IconSize',
		'txt'     :			'Text',
		'cols'    :			'ColumnCount',
		'widget'  :			'Widget',
		'lbl'     :			'Text',
		'ro'      :			'ReadOnly',
	}
	vmapping={
		'ObjectName'            :		'''wgt['Name']''',
		'SizePolicy'            :		'''Fnx.make.SizePolicy(k.get('pol'))''',
		'Checkable'             :		'''k.get('bi')''',
		'MaximumSize'           :		'''Fnx.make.Size(k.get('wh'))''',
		'ToolButtonStyle'       :		'''QtLibs.QToolButtons[k.get('btn')]''',
		'ContentsMargins'       :		'''Fnx.make.Margins(k.get('margin'))''',
		'Icon'                  :		'''gnr.Icon(k['ico'])''',
		'IconSize'              :		'''Fnx.make.Size(k['isize'])''',
		'Text'                  :		'''wgt['name'].split('_')[0]''',
		'ColumnCount'           :		'''k.get('cols')''',
		'Widget'                :		'''k.get('widget').get('Name')''',
		'ReadOnly'              :		'''k.get('ro')''',
	}

	c={}
	for kwarg in k:
		if kwarg in nmapping:
			c[nmapping[kwarg]]=eval(vmapping[nmapping[kwarg]])
		else:
			c[kwarg]=k[kwarg]
	wgt['Cfg']= wgt.get('Cfg') or {}
	if 'widget' in k:
		k.pop('widget')
	wgt['Cfg']|=c
	return wgt


def names(*a):
	names={
			'pfx'    :	f'{a[0]}'								,
			'name'   :	f'{a[1]}{"_" if len(a)>2 else ""}{a[-1]if len(a)>2 else ""}',
	}
	return names

def preset(naming,preconf,**k):
	k=QDefaults.Properties | preconf |	k |names(*naming)
	return k
