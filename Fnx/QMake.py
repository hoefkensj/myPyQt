#!/usr/bin/env python
# Auth
import contextlib
from .tools import lstDiff
import Configs.Config
from Fnx.isTest import isGetMtd,isIsMtd,isMethodWrapper,isQtSignal,isSetMtd
from QLib.QStatic import QtLibs,PyQtX
from assets import svg
from QLib.QBases import QLayout
def Size(a):
	return QtLibs.QCores['Size'](a[0], a[1])
def SizePolicy(pol):
	QSPols=QtLibs.QSizePolicies
	QSPol=QSPols['Pol']
	h=(h:=QtLibs.QSizePolicies[ pol.split('.')[0]])
	v=(v:=QtLibs.QSizePolicies[ pol.split('.')[1]])
	return 	QSPol(h,v)
def Margins(margins):
	return QtLibs.QCores['Margins'](*margins)
def ToolButtonStyle(style):
		return QtLibs.QToolButtons.get(style)
def svgIcon(name):
	icon_states={
		0 : PyQtX.QtGui.QIcon.State.On,
		1 :	PyQtX.QtGui.QIcon.State.Off,}
	icon_themes={
		0	: 'dark',
		1	:	'light',}
	icon = PyQtX.QtGui.QIcon()
	def  make_icon(ico_name,state):
		theme=icon_themes[state]
		svg.svgIcon(ico_name,theme)
		icon.addPixmap(
			PyQtX.QtGui.QPixmap(f'icon_{theme}.svg'),
			PyQtX.QtGui.QIcon.Mode.Normal,
			icon_states[state])
		return icon
	icon = make_icon(name,0)
	icon = make_icon(name,1)
	return icon
def Assemble(w,*a,**k):
	if a:
		w['Mod']=a[0]()
	for element in 	w['Mod']:
		w['Fnx']['Wgt']['Add'](w['Mod'][element])
	w=w['Fnx']['Mod'](w)
	w=w['Con']['Mod'](w)
	w=w['Cfg']['Configure'](w)
	return w
def Config(w,*a,**k):
	l= Configs.Config.mapAlias(**k)
	for setting in l:
		k[setting]=l[setting]
	m,k= Configs.Config.mapFnAlias(**k)
	for setting in m:
		k[setting]=eval(m[setting])
	w['Cfg']={setting: k[setting] for setting in k}
	w['Cfg']['Configure']=Configure
	return w
def Configure(w,*a,c=[]):
	for prop in w['Cfg']:
		with contextlib.suppress(KeyError):
			w['Qtm']['Set'][prop](w['Cfg'][prop])
			continue
		with contextlib.suppress(KeyError):
			w['Qtm']['Mtd'][prop](w['Cfg'][prop])
			continue
		with contextlib.suppress(KeyError):
			w['Fnx'][prop](w['Cfg'][prop])
			continue
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
	setPool=[isSetMtd(item) for item in DirWgt if isSetMtd(item)]
	Pool=[*DirWgt]
	Pool, mtdfilter=lstDiff(Pool,lstDiff(Pool,mtdMap)[0])
	Pool, setfilter=lstDiff(Pool, setPool)
	for item in Pool:
		print(item)
		getmtdname=isGetMtd(item)
		setmtdname=isSetMtd(item)
		ismtdname=isIsMtd(item)

		if isMethodWrapper(clsMap[item]):
			QtMtd['Wrp']|={item:mtdMap[item]}
		elif isQtSignal(clsMap[item]):
			QtMtd['Sig']|={item:mtdMap[item]}
		elif getmtdname:
			QtMtd['Get']|={ismtdname: mtdMap[item]}
		elif setmtdname:
			QtMtd['Set']|={setmtdname:mtdMap[item]}

		elif ismtdname:
			QtMtd['Get']|={ismtdname:mtdMap[item]}
		else :
			# tempPool+=[item.casefold()]
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

def QBuilders(type):
	def Qid(*a,**k):	return {	'Qid':k['Name']	,	'Wgt':a[0]	}
	def Mod(*a,**k):	return Modules(*a,**k)
	def Cfg(*a,**k):	return Config(*a,**k)
	def Lay(*a,**k):	return QLayout.make(a[0], **k)
	def Qtm(*a,**k):	return Qt(a[0])
	def FEl(*a,**k):	return a[1](a[0])
	def FMd(*a,**k):	return FunctionsMod(a[0],a[1],**k)
	def CMd(*a,**k):	return ConnectMod(a[0],a[2],**k)
	def CEl(*a,**k):	return ConnectElm(*a,**k)
	def Cnf(*a,**k):	return Configure(*a)
	def Asm(*a,**k):	return Assemble(*a)
	pyQt={
		'QApp'			:	[Qid,Cfg,Qtm,FEl,CEl,],
		'QBse'			:	[Qid,Cfg,Lay,Qtm,FMd,CMd,Mod],
		'QMdl'			:	[Qid,Mod,Cfg,Lay,Qtm,FMd,CMd,Cnf,Asm],
		'QLay'			:	[Qid,Cfg,Qtm,FEl,Cnf,],
		'QElm'			:	[Qid,Cfg,Qtm,FEl,CEl,Cnf,],
	}
	return pyQt[type]
def QBuild(*a,**k):
	w=QtLibs.QElements.get(a[1])()
	for build in QBuilders(a[0]):
		w=build(w, *a[2:], **k)
	return w

