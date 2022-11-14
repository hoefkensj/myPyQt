#!/usr/bin/env python
from . import QtWgt,gnr
from . import elements
import sys
from . import QWgt


def IncDec(**k):
	def defaults():
		d	=	{
		'pfx'		:	'idw'				,
		'm'			:	[0,0,0,0]			,
		'hPol'	:	'F'						,
		'vPol'	:	'F'						,
		'w'			:	20						,
		'h'			:	20						,
		'lbl'		:	None					,
		'ed'		:	True,
		}
		return d
	def create(wgt):
		wgt.btnExp 		= blk['Elements']['iBtn']('Inc',h=15,w=15,icons=ico)
		wgt.btnCol 		= blk['Elements']['iBtn']('Dec',h=15,w=15,icons=ico)
		return wgt
	def layout(wgt):
		wgt = blk['Base']['sPol'](wgt, h='P', v='P')
		wgt.setContentsMargins(*margin)
		return wgt
	def add(wgt,lay):
		lay.addWidget(wgt.btnExp)
		lay.addWidget(wgt.btnCol)
		return lay
	def conn(wgt):
		wgt.fnI=wgt.btnExp.clicked.connect
		wgt.fnD=wgt.btnCol.clicked.connect
		return wgt

	margin=k.get('margin') or [5,0,5,0]
	wgt =	 blk['Base']['Wgt'](n='wgtIncDec',t='h')
	wgt=create(wgt)
	wgt.lay=add(wgt,wgt.lay)
	wgt=layout(wgt)
	wgt=conn(wgt)
	wgt.setContentsMargins(*margin)
	return wgt