#!/usr/bin/env python

Qid =	{'QID'		:	'k["Name"]'}
Wgt	= {'Wgt' 		: 'wgt'}
Wly	=	{'Wgt'		:	'Layout(Widget)'}
Cfg = {'Cfg'		:	'Config(**k)'}
Lay	= {'Lay'		:	'QLayout.make(w[\'Wgt\'], **k)'}
Qtm	=	{'Qt'			:	'Qt(w)'}
Fnx	=	{'Fnx'		:	'Fnx(w)'}
Con	=	{'Con'		:	'Connect(w)'}
Asm	=	{'Asm'		:	'Assemble(w)'		}
Mod	=	{'Mod' 		: 'Mod()'}


pyQt={
	'QBase'					:	Qid|Wgt|Cfg|Lay|Qtm|Fnx|Con|Asm|Mod,
	'QApplication'	:	Qid|Wgt|Cfg|Qtm|Con,
	'QElement'			:	Qid|Wgt|Cfg|Qtm|Fnx|Con,
	'QModule'				:	Qid|Wgt|Cfg|Lay|Qtm|Fnx|Con|Asm|Mod,
	'QLayout'				:	Qid|Wly|Cfg|Qtm|Fnx,
}