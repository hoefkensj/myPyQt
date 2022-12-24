#!/usr/bin/env python
PKGPATH={
	'QWGT'	: {'GROUP' : 'Elements',	'TYPE'	: 'wgt',		'ARGS'	: '' ,	},
	'QLAY'	:	{'GROUP' : 'Elements',	'TYPE'	: 'lay',		'ARGS'	: '' ,	},
	'QTRW'	:	{'GROUP' : 'Elements',	'TYPE'	: 'TrW',		'ARGS'	: '' ,	},
	'QAPP'	: {'GROUP' : 'Elements',	'TYPE'	: 'app',		'ARGS'	: 'sys.argv' ,}
}

ZeroSpc = {
	'Spacing'				:		0 ,
	'LayoutSpacing'	:		0	,
	}
Properties	=	{
	'margin'				:		[0,0,0,0]				,
	'pol'						:		'E.E'						,
	**ZeroSpc
}
QApplication	=	{**Properties}|{'WGT':PKGPATH['QAPP']}|{'SKL' : 'QApplication'}
QWidget				= {**Properties}|{'WGT':PKGPATH['QWGT']}|{'SKL' : 'QBase'}
QLayout				=	{**Properties}|{'WGT':PKGPATH['QLAY']}|{'SKL' : 'QLayout'}
TreeWidget 		= {**Properties}|{'WGT':PKGPATH['QTRW']}|{'SKL' : 'QElement'}| {
	'AlternatingRowColors'    : True,
	'Animated'                : True,
	'MinimumHeight'           :	10,
	'AllColumnsShowFocus'     :	True,
	'HeaderHidden'            :	False,
	'SKL'											: 'QElement',
}

QModule				=	{**Properties}|{
	't'         :	'H'				,
	'pol'       :	'E.F'			,
}
QEditProp			= {**QModule}	|	{	'ed'  :	True			,}
QHSearch			= {**QModule}	|	{}
QHArrowsLR		= {**QModule}	|	{'pol' :	'F.F',}
QHIncDec			= {**QModule}	|	{'pol' :	'P.P',}

QButton={
	'pol'                   :	'P.P'					,
	'bi'                    :	False					,
}
QIconButton	= QButton	| {
	'wh'                    :	[20,20]					,
	'isize'                 :	[32,32]					,
	'btn'                   :	'I'						,
}
QTextButton	= QButton	| {
	'btn'                   :	'T',
	'txt'                   :	1,
	'Height'                :	20,
}
QLabel={
	'pol'       :'P.F'					,
	'Height'      : 20,
}
QLineEdit={
	'ro'        :	False,
	'pol'       :	'E.P',
	'height'      : 	200,
}
QCheckBox				=	{
	'pol'					:	'P.P'					,
}
QIconCheckBox			=	{
	'wh'           :	[20,20]					,
	'isize'       :	[32,32]					,
}