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
		w['Fnx']['Wgt']['Add'](w['Mod'][element])
	w=w['Fnx']['Mod'](w)
	w=w['Con']['Mod'](w)
	w=w['Cfg']['Configure'](w)
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


def Entry(fn,wgt):
	return {(getattr(fn, '__name__')): fn(wgt)}

def Element(component):
	name=component.get('Qid')
	return {name : component}

def Qt(wgt):
	# fnx_Qt=importlib.import_module('.skell')
	widget=wgt['Wgt']
	QtMtd={'Wrp':{},'Mtd':{},'Get':{},'Set':{},'Sig':{}}
	DirWgt=dir(widget)
	mtdMap={item: val for item in DirWgt if callable(val:=getattr(widget,item))}
	clsMap={item: getattr(getattr(getattr(widget,item),'__class__'),'__name__') for item in DirWgt}
	pool=[*DirWgt]
	pool=[item for item in pool if item in mtdMap]
	for item in pool:
		setmtdname=isTest.isSetMtd(item)
		ismtdname=isTest.isIsMtd(item)
		if isTest.isMethodWrapper(clsMap[item]):
			QtMtd['Wrp']|={item:mtdMap[item]}
		elif isTest.isQtSignal(clsMap[item]):
			QtMtd['Sig']|={item:mtdMap[item]}
		elif setmtdname:
			QtMtd['Set']|={setmtdname:mtdMap[item]}
		elif ismtdname:
			QtMtd['Get']|={ismtdname:mtdMap[item]}
		else:
			QtMtd['Mtd']|={item:mtdMap[item]}
	wgt['Qtm']=QtMtd
	return wgt
def Modules(*a,**k):
	mod=a[2]
	w=mod(a[0])
	return w

def FunctionsMod(w,fnx,**k):
	def FnxMod():
		def fnxmod(w):
			w['Fnx']|={w['Mod'][mod]['Qid']:w['Mod'][mod]['Fnx'] for mod in w['Mod']}
			return w
		return fnxmod
	Fnx={'Wgt': fnx(w)}
	Fnx['Mod']=FnxMod()
	Fnx['Asm']=Assemble
	w['Fnx']=Fnx
	return w
def ConnectMod(w,con,**k):
	def ConMod():
		def conmod(w):
			w['Con']|={w['Mod'][mod]['Qid']:w['Mod'][mod]['Con'] for mod in w['Mod']}
			return w
		return conmod
	Con={}
	Con['Wgt']=w['Qtm'].get('Sig')
	Con['Mod']=ConMod()
	w['Con']=Con
	return w
def ConnectElm(*a,**k):
	return {**a[0],'Con': a[0]['Qtm'].get('Sig')}

def Construct():
	def construct(type):
		def Qid(*a,**k):	return {'Qid': k["Name"],'Wgt': a[0],}
		def Mod(*a,**k):	return Modules(*a,**k)
		def Cfg(*a,**k):	return Config(*a,**k)
		def Lay(*a,**k):	return QLayout.make(a[0], **k)
		def Qtm(*a,**k):	return Qt(a[0])
		def FEl(*a,**k):	return a[1](a[0])
		def FMd(*a,**k):	return FunctionsMod(a[0],a[1],**k)
		def CMd(*a,**k):	return ConnectMod(a[0],a[2],**k)
		def CEl(*a,**k):	return ConnectElm(*a,**k)
		def Asm(*a,**k):	return Assemble(*a)
		pyQt={
			'QApp'			:	[Qid,Cfg,Qtm,FEl,CEl,],
			'QBse'			:	[Qid,Cfg,Lay,Qtm,FMd,CMd,Mod],
			'QMdl'			:	[Qid,Mod,Cfg,Lay,Qtm,FMd,CMd,Asm,],
			'QLay'			:	[Qid,Cfg,Qtm,FEl,],
			'QElm'			:	[Qid,Cfg,Qtm,FEl,CEl,],
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