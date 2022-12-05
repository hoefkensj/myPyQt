#!/usr/bin/env python
# Auth
import re
import assets.ico
import contextlib
import lib.PyQtX
from static.QtLibs import QSizePolicies,QCores



# def SetMtd(wgt):
# 	sets = wgt['Fnx']['Set']
# 	reads=wgt['Read']
# 	def setmtd(setm, *setv):
# 		Set=sets[setm]
# 		Set(*setv)
# 		Val=reads[setm]
# 		r={setm : Val()}
# 		return r
# 	return setmtd

def Icon(svg):
		import base64
		icon_states={
			0 : lib.PyQtX.QtGui.QIcon.State.On,
			1 :	lib.PyQtX.QtGui.QIcon.State.Off,	}
		icon = lib.PyQtX.QtGui.QIcon()
		def  make_icon(icon,state):
			with open(f'icon{state}.svg','wb') as l:
				l.write(base64.b64decode(svg[state]))
			icon.addPixmap(
				lib.PyQtX.QtGui.QPixmap(f'icon{state}.svg'),
				lib.PyQtX.QtGui.QIcon.Mode.Normal,
				icon_states[state])
			return icon
		icon = make_icon(icon,0)
		icon = make_icon(icon,1)
		return icon



def Size(wh):	return QCores['Size'](wh[0], wh[1])
def SizePolicy(pol):
	h,v = pol.split('.')
	return QSizePolicies['Pol'](QSizePolicies[h],QSizePolicies[v])
def Margins(margins):
	return QCores['Margins'](*margins)

def make(component,*a):

	comps={
		'size' 		: Size(*a)
		'sizpol'	: SizePolicy(*a)
		'margins'	: Margins(*a)
	}


def makeSize(wh):
	return QCores['Size'](wh[0], wh[1])

def makeSizePolicy(pol):
	h,v = pol.split('.')
	return QSizePolicies['Pol'](QSizePolicies[h],QSizePolicies[v])

def makeMargins(margins):
	return QCores['Margins'](*margins)

def Element(component):
	name=component.get('Name')
	return {name : component}


def Short(wgt,*a):
	s={}
	for name in wgt['Elements']:
		sub =wgt['Elements'][name]
		for item in a:
			sub=sub[item]
		s[name.split('_')[1]]=sub
	return s

# def ShortFnx(wgt):
# 	return {name.split('_')[1]:wgt['Elements'][name]['Fnx']for name in wgt['Elements']}

# def Short(wgt):
# 	return {name.split('_')[1]:wgt['Elements'][name]for name in wgt['Elements']}

def IconSet(i):
	return assets.ico.get(i) if i in  assets.ico.names() else None


def makeConfigure(wgt):
	def SpecialCases(wgt):
		def HideCols(wgt):
			cols = wgt['Cfg']['hidecols']
			for col in cols:
				print('hidecol:' ,col)
				wgt['Fnx']['Set']['ColumnHidden'](col,True)
			return wgt
		Cases={
			'hidecols'        :	HideCols			,
		}
		for Case in Cases:
			if Case in  wgt['Cfg']:
				wgt=Cases[Case](wgt)
		return wgt
	def configure(wgt):
		for prop in wgt['Cfg']:
			with contextlib.suppress(KeyError):
				wgt['Fnx']['Set'][prop](wgt['Cfg'][prop])
		wgt=SpecialCases(wgt)
		return wgt
	wgt['Fnx']['Configure']	=	configure
	return wgt


def Generate(wgt):
	def generate():
		for element in 	wgt['Elements']:
			wgt['Fnx']['Add'](wgt['Elements'][element]['Wgt'])
	wgt['Fnx']['Generate'] 	= generate
	return wgt

def Show(wgt):
	mtd={}
	mtd[True]=wgt['Fnx']['Mtd']['show']
	mtd[False]=wgt['Fnx']['Mtd']['hide']
	mtd['exec']=True
	def show(*a):
		if a:
			mtd[a[0]]()
			mtd['exec']=not a[0]
		else:
			mtd[mtd['exec']]()
			mtd['exec']=not mtd['exec']
	wgt['Fnx']['Show']=show
	return wgt

def Fnx(wgt):
	wgt	=	Show(wgt)
	wgt = makeConfigure(wgt)
	if isinstance(wgt.get('Elements'),dict):
		wgt	=	Generate(wgt)
	return wgt

def Clean(wgt):
	toclean=[]
	for section in wgt:
		if isinstance(wgt[section],dict) and len(wgt[section])==0:
			toclean+=[section]
	for section in toclean:
		wgt.pop(section)
	return wgt

def minInit(wgt):
	wgt=Clean(wgt)
	wgt['Fnx']['Configure'](wgt)
	if isinstance(wgt.get('Elements'),dict):
		wgt['Fnx']['Generate']()
	if callable(wgt['Fnx'].get('Init')):
		wgt['Fnx']['Init']()
	return wgt

