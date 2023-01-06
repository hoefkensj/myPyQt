#!/usr/bin/env python
SPOLEE	=		{'pol':'E.E'}
SPOLPP	=		{'pol':'P.P'}
SPOLFF	=		{'pol':'F.F'}
SPOLEF	=		{'pol':'E.F'}
SPOLPF	=		{'pol':'P.F'}
SPOLFP	=		{'pol':'P.F'}
SPACING	=		{'Spacing':0,'LayoutSpacing':0,}
MARGIN	=		{'margin':[0,0,0,0]}



BUTTON		=		{**MARGIN}|{**SPACING}|{**SPOLFP}|{'bi':False,}
CHECKBOX	=		{**MARGIN}|{**SPACING}|{**SPOLFF}
WIDGET		=		{**MARGIN}|{**SPACING}|{**SPOLEE}


QApplication	=		{**WIDGET}
QWidget				=		{**WIDGET}
QLayout				=		{**WIDGET}
QTreeWidget		=		{**WIDGET}|{'AlternatingRowColors':True,'Animated':True,'MinimumHeight':10,'AllColumnsShowFocus':True,'HeaderHidden':False,}


# QButton	=		{**BUTTON}
QIconButton		=		{**BUTTON}|{'wh':[20,20],'isize':[52,52],'btnstyle':'I','ico':'name'}
QTextButton		=		{**BUTTON}|{'Height':50,'btnstyle':'T',}
# QLabel	=		{'pol':'P.F','Height':20,}
# QLineEdit	=		{'ro':False,'pol':'E.P','height':200,}
# QCheckBox	=		{'pol':'P.P',}
QIconCheckBox	=		{**CHECKBOX}|{'wh':[20,20],'isize':[32,32],}

# QModule	=		{**WIDGET}|{'t':'H',}
# QHIncDec	=		{**QModule}|{'pol':'P.P',}
# QHArrowsLR	=		{**QModule}|{'pol':'F.F',}
# QHSearch	=		{**QModule}|{}
# QEditProp	=		{**QModule}|{'ed':True,}

