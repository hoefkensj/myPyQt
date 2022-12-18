#!/usr/bin/env python

Aliasses={
		'Name'    	: 		'ObjectName',
		'bi'      	:			'Checkable',
		'lbl'     	:			'Text',
		'cols'    	:			'ColumnCount',
		'ro'      	:			'ReadOnly',
		}

MakeAliases={
	'ico'     	:	[	'Icon'						 , 	'''make.Icon({VAL})''' 							],
	'btnstyle' 	:	[	'ToolButtonStyle'	 , 	'''make.ToolButtonStyle({VAL})'''		],
	'margins'  	:	[	'ContentsMargins'	 , 	'''make.Margins({VAL})''' 					], 
	'pol'     	:	[	'SizePolicy'			 , 	'''make.SizePolicy('{VAL}')'''			], 	
	'sz_max'		:	[	'MaximumSize'			 , 	'''make.Size({VAL})'''							], 
	'sz_min'		:	[	'MinimumSize'			 , 	'''make.Size({VAL})'''							], 
	'sz_ico'		:	[	'IconSize'				 , 	'''make.Size({VAL})'''							], 	
}

