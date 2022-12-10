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

QModule={
	'ed'        :	True			,
	't'         :	'H'				,
	'pol'       :	'E.F'			,
}
QLayout={}
QEditProp			=	QModule	|	{}
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
	'pol'       	:	'P.P'					,
}
QIconCheckBox			=	{
	'wh'       		 :	[20,20]					,
	'isize'     	:	[32,32]					,
}