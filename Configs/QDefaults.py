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

QIconButton={
		'pol'       :	'P.P'									,
		'wh'        :	[20,20]								,
		'bi'        :	False									,
		'isize'     :	[32,32]								,
		'lbl'       :	None									,
		'btn'       :	'I'										,
}