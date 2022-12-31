#!/usr/bin/envpython

SPACING={'Spacing':0,'LayoutSpacing':0,}
MARGIN={'margin':[0,0,0,0]}
SIZEPOL={'pol':'E.E'}
BUTTON={**MARGIN}|{**SPACING}|{'pol':'P.F','bi':False,}
WIDGET={**MARGIN}|{**SPACING}|{**SIZEPOL}


QApplication={**WIDGET}
QWidget={**WIDGET}
QLayout={**WIDGET}
QTreeWidget={**WIDGET}|{'AlternatingRowColors':True,'Animated':True,'MinimumHeight':10,'AllColumnsShowFocus':True,'HeaderHidden':False,}


# QButton={**BUTTON}
QIconButton={**BUTTON}|{'wh':[20,20],'isize':[32,32],'btnstyle':'I',}
# QTextButton=QButton|{'btn':'T','txt':1,'Height':20,}
# QLabel={'pol':'P.F','Height':20,}
# QLineEdit={'ro':False,'pol':'E.P','height':200,}
# QCheckBox={'pol':'P.P',}
# QIconCheckBox={'wh':[20,20],'isize':[32,32],}

# QModule={**WIDGET}|{'t':'H',}
# QHIncDec={**QModule}|{'pol':'P.P',}
# QHArrowsLR={**QModule}|{'pol':'F.F',}
# QHSearch={**QModule}|{}
# QEditProp={**QModule}|{'ed':True,}

