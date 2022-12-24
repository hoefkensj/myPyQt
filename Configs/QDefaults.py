#!/usr/bin/env python
PKGPATH={
	'QWGT'	: {'GROUP' : 'Elements',		'TYPE'	: 'wgt',		'ARGS'	: '' ,	},
	'QLAY'	:	{'GROUP' : 'Elements',		'TYPE'	: 'lay',		'ARGS'	: '' ,	},
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




QWidget				= {**Properties}|{'QWGT':PKGPATH['QWGT']}
QLayout				=	{**Properties}|{'QLAY':PKGPATH['QLAY']}
TreeWidget 		= {**Properties}| {
	'AlternatingRowColors'    : True,
	'Animated'                : True,
	'MinimumHeight'           :	10,
	'AllColumnsShowFocus'     :	True,
	'HeaderHidden'            :	True,
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