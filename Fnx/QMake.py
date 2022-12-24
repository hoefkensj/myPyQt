#!/usr/bin/env python
# Auth
import contextlib
import Configs.Config
from Fnx import isTest
from QLib.QStatic import QtLibs,PyQtX
import assets.ico

def Size(wh):
	return QtLibs.QCores['Size'](wh[0], wh[1])

def SizePolicy(pol):
	h,v = pol.split('.')
	return QtLibs.QSizePolicies['Pol'](QtLibs.QSizePolicies[h], QtLibs.QSizePolicies[v])

def Margins(margins):
	return QtLibs.QCores['Margins'](*margins)

def ToolButtonStyle(style):
		return QtLibs.QToolButtons.get(style)

def Icon(svg):
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
		return icon

def IconSet(i):
	return assets.ico.get(i) if i in  assets.ico.names() else None

def Assemble(wgt):
	def assemble():
		for element in 	wgt['Mod']:
			wgt['Fnx']['Add'](wgt['Mod'][element])
		return wgt
	return assemble

def Config(**k):
	def config(**k):
		j= Configs.Config.mapMakeAlias(**k)
		for setting in j:
			k[setting]=eval(j[setting])
		k= Configs.Config.mapAlias(**k)
		return {setting: k[setting] for setting in k}

	def Configure(wgt):
		wgt['Cfg']=config(**k)
		for prop in wgt['Cfg']:
			with contextlib.suppress(KeyError):
				wgt['Qt']['Set'][prop](wgt['Cfg'][prop])
		return wgt
	return Configure


def Connect(wgt):
	def connect(wgt):
		wgt['Con']={}
		wgt['Con']['Wgt']=wgt['Qt']['Sig']
		if isinstance(wgt.get('Mod'), dict) and len(wgt.get('Mod')) > 0:
			for element in wgt['Mod']:
				wgt['Con'][element]=wgt['Mod'][element]['Con']['Wgt']
		return wgt
	return connect




def Entry(fn,wgt):
	return {(getattr(fn, '__name__')): fn(wgt)}
def Element(component):
	name=component.get('QID')
	return {name : component}




def Qt(w):
	# fnx_Qt=importlib.import_module('.skell')
	wgt=w['Wgt']
	QtMtd={'Mtd':{},'Get':{},'Set':{},'Sig':{}}
	DirWgt=dir(wgt)
	mtdMap={item: val for item in DirWgt if callable(val:=getattr(wgt,item))}
	clsMap={item: getattr(getattr(getattr(wgt,item),'__class__'),'__name__') for item in DirWgt}
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
	return QtMtd
