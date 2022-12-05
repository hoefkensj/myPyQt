#!/usr/bin/env python
Properties={
	'margin'    						:	[0,0,0,0]						,
	'LayoutSpacing'					:	0										,
	'Spacing'								:	0										,
	'pol'										:'E.E'								,
	}

TreeWidget={
	'AlternatingRowColors'	:	True,
	'Animated'							:	True,
	'MinimumHeight'					:	10,
	'AllColumnsShowFocus'		:	True,
	'HeaderHidden'					:	False,
}

QModule={
	'ed'        :	True						,
	't'         :	'H'							,
	'pol'       :	'E.F'						,
}
QEditProp				=	QModule	|	{}
QHSearch				=	QModule	|	{}
QHArrowsLR			=	QModule	|	{'pol' :	'F.F',}

QButton={
	'pol'       :	'P.P'									,
	'bi'        :	False									,
}
QIconButton	=	QButton	| {
	'wh'        :	[20,20]								,
	'bi'        :	False									,
	'isize'     :	[32,32]								,
	'btn'       :	'I'										,
}
QTextButton	=	QButton	| {
	'btn'       :	'T',
	'txt'				:	1,
}

QLineEdit={
	'ro'				:	False,
	'Height'		: 20,
	}