#!/usr/bin/env python
Properties	=	{
	'margin'    						:		[0,0,0,0]				,
	'LayoutSpacing'					:		0								,
	'Spacing'								:		0								,
	'pol'										:		'E.E'						,
}

QWidget=Properties|{}

TreeWidget=Properties|{
	'AlternatingRowColors'		:	True,
	'Animated'								:	True,
	'MinimumHeight'						:	10,
	'AllColumnsShowFocus'			:	True,
	'HeaderHidden'						:	False,
}
QLayout=Properties|{}

QModule=Properties|{
	'ed'        :	True			,
	't'         :	'H'				,
	'pol'       :	'E.F'			,
}


QEditProp			=	QModule	|	{}
QHSearch			=	QModule	|	{}
QHArrowsLR		=	QModule	|	{'pol' :	'F.F',}
QHIncDec			=	QModule	|	{'pol' :	'P.P',}

QButton={
	'pol'										:	'P.P'					,
	'bi'										:	False					,
}
QIconButton	=	QButton	| {
	'wh'										:	[20,20]					,
	'isize'									:	[32,32]					,
	'btn'										:	'I'						,
}
QTextButton	=	QButton	| {
	'btn'										:	'T',
	'txt'										:	1,
	'Height'								:	20,
}
QLabel=Properties|{
	'pol'				:'P.F'					,
	'Height'			: 20,
}
QLineEdit={
	'ro'				:	False,
	'pol'				:	'E.F',
	'Height'			: 	20,

}
QCheckBox				=	{
	'pol'					:	'P.P'					,
}
QIconCheckBox			=	{
	'wh'       		 :	[20,20]					,
	'isize'     	:	[32,32]					,
}