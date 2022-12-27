#!/usr/bin/env python
# Auth
import contextlib
import Configs.Config
from Fnx import isTest
from QLib.QStatic import QtLibs,PyQtX
import assets.ico

from QLib.QBases import QLayout


from Fnx.debug import DebDec



def Size(wh):
	return QtLibs.QCores['Size'](wh[0], wh[1])

def SizePolicy(pol):
	QSPols=QtLibs.QSizePolicies
	QSPol=QSPols['Pol']
	h=(h:=QtLibs.QSizePolicies[ pol.split('.')[0]])
	v=(v:=QtLibs.QSizePolicies[ pol.split('.')[1]])

	return 	''

def Margins(margins):
	return QtLibs.QCores['Margins'](*margins)

def ToolButtonStyle(style):
		return QtLibs.QToolButtons.get(style)

def svgIcon(svg):
		import base64
		icon_states={
			0 : PyQtX.QtGui.QIcon.State.On,
			1 :	PyQtX.QtGui.QIcon.State.Off,	}
		icon = PyQtX.QtGui.QIcon()
		def  make_icon(icon,state):
			with open(f'icon{state}.svg','wb') as l:
				l.write(base64.b64decode(svg[state]))
			icon.addPixmap(
				PyQtX.QtGui.QPixmap(f'icon{state}.svg'),
				PyQtX.QtGui.QIcon.Mode.Normal,
				icon_states[state])
			return icon
		icon = make_icon(icon,0)
		icon = make_icon(icon,1)
		return iconQSizePolicies['Pol'](QtLibs.QSizePolicies[h], QtLibs.QSizePolicies[v])

def IconSet(i):
	return assets.ico.get(i) if i in  assets.ico.names() else None

def Assemble(w,*a,**k):
	for element in 	w['Mod']:
		w['Fnx']['Add'](w['Mod'][element])
	return w


def Config(w,*a,**k):
	l= Configs.Config.mapAlias(**k)
	m= Configs.Config.mapFnAlias(**k,**l)
	for setting in m:
		k[setting]=eval(m[setting])
	w['Cfg']={setting: k[setting] for setting in k}
	w['Cfg']['Configure']=Configure
	return w

def Configure(w):
	for prop in w['Cfg']:
		with contextlib.suppress(KeyError) as key:
			print(key)
			w['Qt']['Set'][prop](w['Cfg'][prop])
			w['Qt']['Mtd'][prop](w['Cfg'][prop])
			w['Fnx'][prop](w['Cfg'][prop])
	return w

def ConnectMod(w):
	w['Con']={}
	w['Con']['Wgt']=w['Qtm'].get('Sig')
	if isinstance(w.get('Mod'), dict) and len(w.get('Mod')) > 0:
		for element in w['Mod']:
			w['Con'][element]=w['Mod'][element]['Con']['Wgt']
	return w
def ConnectElm(w):	
	return {'Con': w['Qtm'].get('Sig')}

def Entry(fn,wgt):
	return {(getattr(fn, '__name__')): fn(wgt)}

def Element(component):
	name=component.get('Qid')
	return {name : component}

def Qt(wgt):
	# fnx_Qt=importlib.import_module('.skell')
	widget=wgt['Wgt']
	QtMtd={'Mtd':{},'Get':{},'Set':{},'Sig':{}}
	DirWgt=dir(widget)
	mtdMap={item: val for item in DirWgt if callable(val:=getattr(widget,item))}
	clsMap={item: getattr(getattr(getattr(widget,item),'__class__'),'__name__') for item in DirWgt}
	pool=[*DirWgt]
	pool=[item for item in pool if item in mtdMap]
	for item in pool:
		setmtdname=isTest.isSetMtd(item)
		ismtdname=isTest.isIsMtd(item)
		if  isTest.isMethodWrapper(item):
			QtMtd['Wrp']|={item:mtdMap[item]}
		elif isTest.isQtSignal(item):
			QtMtd['Sig']|={item:mtdMap[item]}
		elif setmtdname:
			QtMtd['Set']|={setmtdname:mtdMap[item]}
		elif ismtdname:
			QtMtd['Get']|={ismtdname:mtdMap[item]}
		else:
			QtMtd['Mtd']|={item:mtdMap[item]}
	wgt['Qtm']=QtMtd
	return wgt
def Modules(w,**k):
	mod=k.pop('mod')
	w=mod(w)
	return w
def Functions(w,**k):
	w['Fnx']={}
	fn=k.get('fn')
	w['Fnx']=fn(w,)
	w['Fnx']['Asm']=Assemble
	return w

def Construct():
	def construct(type):
		def Qid(*a,**k):	return {'Qid': k["Name"],'Wgt': Qt,}
		def Mod(*a,**k):	return Modules(*a,**k)
		def Cfg(*a,**k):	return Config(*a,**k)
		def Lay(*a,**k):	return QLayout.make(*a, **k)
		def Qtm(*a,**k):	return Qt(*a)
		def Fnx(*a,**k):	return Functions(*a,**k)
		def CMd(*a,**k):	return ConnectMod(*a,**k)
		def CEl(*a,**k):	return ConnectElm(*a,**k)
		def Asm(*a,**k):	return Assemble(*a)
		pyQt={
			'QApp'			:	[Qid,Cfg,Qtm,Fnx,CEl,],
			'QBse'			:	[Qid,Mod,Cfg,Lay,Qtm,Fnx,CMd],
			'QMdl'			:	[Qid,Mod,Cfg,Lay,Qtm,Fnx,CMd,Asm,],
			'QLay'			:	[Qid,Cfg,Qtm,Fnx,],
			'QElm'			:	[Qid,Cfg,Qtm,Fnx,CEl,],
		}
		return pyQt[type]
	return construct
#
# 	'ico'     	:			'{Icon:svgIcon({VAL})}'							,
# 	'btnstyle' 	:			'ToolButtonStyle'		,
# 	'margins'  	:			'ContentsMargins'		,
# 	'pol'     	:			'SizePolicy'				,
# 	'sz_max'		:			'MaximumSize'				,
# 	'sz_min'		:			'MinimumSize'				,
# 	'sz_ico'		:			'IconSize'					,
# }
# FnAliasses={
# 'Icon'						: '''Icon({VAL})'''                ,
# 'ToolButtonStyle'	: '''ToolButtonStyle({VAL})'''     ,
# 'ContentsMargins'	: '''Margins({VAL})'''             ,
# 'SizePolicy'			: '''SizePolicy('{VAL}')'''        ,
# 'MaximumSize'			: '''Size({VAL})'''                ,
# 'MinimumSize'			: '''Size({VAL})'''                ,
# 'IconSize'				: '''Size({VAL})'''           		 , }