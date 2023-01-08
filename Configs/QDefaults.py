#!/usr/bin/env python
SPOLEE	=		{'pol':'E.E'}
SPOLPP	=		{'pol':'P.P'}
SPOLFF	=		{'pol':'F.F'}
SPOLEF	=		{'pol':'E.F'}
SPOLPF	=		{'pol':'P.F'}
SPOLFP	=		{'pol':'P.F'}
SPACING	=		{'Spacing':0,'LayoutSpacing':0,}
MARGIN	=		{'margins':[0,0,0,0]}



BUTTON		=		{**SPOLFP}|{**MARGIN}|{**SPACING}|{'bi':False,}
CHECKBOX	=		{**SPOLFF}|{**MARGIN}|{**SPACING}
WIDGET		=		{**SPOLEE}|{**MARGIN}|{**SPACING}


QApplication	=		{**WIDGET}
QWidget				=		{**WIDGET}
QLayout				=		{**WIDGET}
QTreeWidget		=		{**WIDGET}|{'AlternatingRowColors':True,'Animated':True,'MinimumHeight':10,'AllColumnsShowFocus':True,'HeaderHidden':False,}


# QButton	=		{**BUTTON}
QIconButton		=		{**BUTTON}|{'wh':[20,20],'isize':[52,52],'btnstyle':'I','ico':'name'}
QTextButton		=		{**BUTTON}|{'btnstyle':'T',}
QLabel				=		{**MARGIN}|{**SPACING}|{'pol':'P.F','Height':20,}
QLineEdit			=		{**MARGIN}|{**SPACING}|{'ro':False,'pol':'P.P'}
# QCheckBox	=		{'pol':'P.P',}
QIconCheckBox	=		{**CHECKBOX}|{'wh':[20,20],'isize':[32,32],}

# QModule	=		{**WIDGET}|{'t':'H',}
# QHIncDec	=		{**QModule}|{'pol':'P.P',}
# QHArrowsLR	=		{**QModule}|{'pol':'F.F',}
# QHSearch	=		{**QModule}|{}
# QEditProp	=		{**QModule}|{'ed':True,}

