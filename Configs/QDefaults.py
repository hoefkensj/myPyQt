#!/usr/bin/env python
SPOLEE	=		{'pol':'E.E'}
SPOLEF	=		{'pol':'E.F'}
SPOLEP	=		{'pol':'E.P'}
SPOLPP	=		{'pol':'P.P'}
SPOLFF	=		{'pol':'F.F'}
SPOLPF	=		{'pol':'P.F'}
SPOLFP	=		{'pol':'P.F'}
SPACING	=		{'Spacing':0,'LayoutSpacing':0,}
MARGIN	=		{'margins':[0,0,0,0]}
ISIZE		=		{'sz_ico':[21,21]}


WIDGET		=		{**SPOLEE}|{**MARGIN}|{**SPACING}|{'t':'V'}
BUTTON		=		{**WIDGET}|{**SPOLEP}|{'bi':False,}
CHECKBOX	=		{**WIDGET}



QApplication	=		{**WIDGET}
QWidget				=		{**WIDGET}
QLayout				=		{**WIDGET}

QTreeWidget		=		{**WIDGET}|{	'AlternatingRowColors':True,
																'Animated':True,
																'MinimumHeight':10,
																'AllColumnsShowFocus':True,
																'HeaderHidden':False,}


QIconButton		=		{**BUTTON}|{**SPOLFF}|{**ISIZE}|{'btnstyle':'I','ico':'name'}
QTextButton		=		{**BUTTON}|{'btnstyle':'T',}
QLabel				=		{**WIDGET}
QLineEdit			=		{**WIDGET}|{'ro':False}
# QCheckBox	=		{'pol':'P.P',}
QIconCheckBox	=		{**CHECKBOX}|{**ISIZE}

# QModule	=		{**WIDGET}|{'t':'H',}
# QHIncDec	=		{**QModule}|{'pol':'P.P',}
# QHArrowsLR	=		{**QModule}|{'pol':'F.F',}
# QHSearch	=		{**QModule}|{}
# QEditProp	=		{**QModule}|{'ed':True,}

