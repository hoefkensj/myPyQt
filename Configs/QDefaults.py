#!/usr/bin/env python
import qdarkstyle
qdark=qdarkstyle.load_stylesheet()
Properties={
	'margin'    				:	[0,0,0,0]						,
	'LayoutSpacing'				:	0								,
	'Spacing'					:	0								,
	'pol'						:	'E.E'							,
	'StyleSheet'				: 	qdark
	}

QWidget=Properties|{}

TreeWidget={
	'AlternatingRowColors'	:	True,
	'Animated'				:	True,
	'MinimumHeight'			:	10,
	'AllColumnsShowFocus'	:	True,
	'HeaderHidden'			:	False,
}

QModule=Properties|{
	't'         :	'H'				,
	'pol'       :	'E.F'			,
}


QEditProp			=	QModule	|	{	'ed'        :	True			,}
QHSearch			=	QModule	|	{}
QHArrowsLR			=	QModule	|	{'pol' :	'F.F',}

QHIncDec={}

QButton={
	'pol'       :	'P.P'					,
	'bi'        :	False					,
}
QIconButton	=	QButton	| {
	'wh'        :	[20,20]					,
	'isize'     :	[32,32]					,
	'btn'       :	'I'						,
}
QTextButton	=	QButton	| {
	'btn'      			:	'T',
	'txt'				:	1,
	'Height'			:	 20,
}
QLabel={
	'pol'				:'P.F'					,
	'Height'			: 20,
}
QLineEdit={
	'ro'				:	False,
	'pol'				:	'E.P',
	'height'			: 	200,
}
QCheckBox				=	{
	'pol'       	:	'P.P'					,
}
QIconCheckBox			=	{
	'wh'       		 :	[20,20]					,
	'isize'     	:	[32,32]					,
}