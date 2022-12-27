#!/usr/bin/env python
# Auth
import contextlib,inspect,functools
import Configs.Config
from Fnx import isTest
from QLib.QStatic import QtLibs,PyQtX,skel
import assets.ico
import sys
from QLib.QBases import QLayout
import PyQt6.QtCore
from  PyQt6.QtWidgets import QSizePolicy
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

def Assemble(wgt):
	def assemble():
		for element in 	wgt['Mod']:
			wgt['Fnx']['Add'](wgt['Mod'][element])
		return wgt
	return assemble

def Config(w,**k):
	l= Configs.Config.mapAlias(**k)
	m= Configs.Config.mapFnAlias(**k,**l)
	for setting in m:
		k[setting]=eval(m[setting])
	w['Cfg']={setting: k[setting] for setting in k}
	w['Cfg']['Configure']=Configure
	return w

def Configure(wgt):
	for prop in wgt['Cfg']:
		with contextlib.suppress(KeyError) as key:
			print(key)
			wgt['Qt']['Set'][prop](wgt['Cfg'][prop])
			wgt['Qt']['Mtd'][prop](wgt['Cfg'][prop])
			wgt['Fnx'][prop](wgt['Cfg'][prop])
	return wgt

def Connects(wgt):
	wgt['Con']={}
	wgt['Con']['Wgt']=wgt['Qtm'].get('Sig')
	if isinstance(wgt.get('Mod'), dict) and len(wgt.get('Mod')) > 0:
		for element in wgt['Mod']:
			wgt['Con'][element]=wgt['Mod'][element]['Con']['Wgt']
	return wgt

def Entry(fn,wgt):
	return {(getattr(fn, '__name__')): fn(wgt)}

def Element(component):
	name=component.get('QID')
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



def Qid(w,**k):	
	w['Qid']= k["Name"]
	return w
def Wgt(w,**k):
	w['Wgt']=eval('Q')
	return w
def Cfg(w,**k):
	w=Config(w,**k)
	return  w
def Lay(w,**k):
	w['Lay']=QLayout.make(w, **k)
	return w
def Qtm(w,**k):
	w['Qtm']=Qt(w)
	return w
def Fnx(w,**k):
	w['Fnx']={}
	w['Fnx']['Gen']=functions
	return w
def Con(w,**k):
	w=Connect(w)
	return 	w
def Mod(w,**k):
	w['Mod']={}
	return 	w
def Asm(w,**k):
	w=Assemble(w)
	return w


def Construct(wgttype):

	def Qid(Qt,**k):return {'Qid': k["Name"],'Wgt': Qt,}
	def Cfg(w,**k):	return Config(w,**k)
	def Lay(w,**k):	return {**w,'Lay':QLayout.make(w, **k)}
	def Qtm(w,**k):	return Qt(w)
	def Fnx(w,**k):	return Functions(w)
	def Con(w,**k):	return Connects(w)
	def Mod(w,**k): return Modules(w)
	def Asm(w,**k):	return Assemble(w)
	pyQt={
		'QApp'			:	[Qid,Cfg,Qtm,Con,],
		'QBse'			:	[Qid,Cfg,Lay,Qtm,Fnx,Con,Asm,Mod,],
		'QMdl'			:	[Qid,Cfg,Lay,Qtm,Fnx,Con,Mod,Asm,],
		'QLay'			:	[Qid,Cfg,Qtm,Fnx,],
		'QElm'			:	[Qid,Cfg,Qtm,Fnx,Con,],
	}

	return pyQt.get(wgttype)

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