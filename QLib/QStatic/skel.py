#!/usr/bin/env python

Qid =	{'QID'		:	'k["Name"]'}
Wgt	= {'Wgt' 		: 'QtLibs.Q{GROUP}.get(\'{TYPE}\')({ARGS})'}
Wly	=	{'Wgt'		:	'Layout(Widget)'}
Cfg = {'Cfg'		:	'QMake.Config(**k)'}
Lay	= {'Lay'		:	'QLayout.make(w[\'Wgt\'], **k)'}
Qtm	=	{'Qt'			:	'QMake.Qt(w)'}
Fnx	=	{'Fnx'		:	'Fnx(w)'}
Con	=	{'Con'		:	'QMake.Connect(w)'}
Asm	=	{	'Asm'		:	'QMake.Assemble(w)'		}
Mod	=	{'Mod' 		: 'Mod()'}

QBase 				= Qid|Wgt|Cfg|Lay|Qtm|Fnx|Con|Asm|Mod
QApplication	= Qid|Wgt|Cfg|Qtm|Fnx|Con
QElement 			= Qid|Wgt|Cfg|Qtm|Fnx|Con
QModulee 			= Qid|Wgt|Cfg|Lay|Qtm|Fnx|Con|Asm|Mod
QLayout				= Qid|Wly|Cfg|Qtm|Fnx
