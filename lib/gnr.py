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
	def icon(ico):
		import base64
		icon_states={
			0 : lib.PyQtX.QtGui.QIcon.State.On,
			1 :	lib.PyQtX.QtGui.QIcon.State.Off,	}
		icon = lib.PyQtX.QtGui.QIcon()
		def  make_icon(icon,state):
			with open(f'icon{state}.svg','wb') as l:
				l.write(base64.b64decode(ico[state]))
			icon.addPixmap(lib.PyQtX.QtGui.QPixmap(f'icon{state}.svg'), lib.PyQtX.QtGui.QIcon.Mode.Normal, icon_states[state])
			return icon
		# with open('icond.svg','wb') as d:
		# 	d.write(base64.b64decode(ico[n][1]))
		icon = make_icon(icon,0)
		icon = make_icon(icon,1)
		return icon
	return icon(svg)




# def NameRE(**k):
# 	# pfx_NameParentnameParentmodule
# 	# ibtn_EditKeyEdit
# 	pfx=k.get('pfx') or '^_' #NOT _
# 	sep=k.get('sep') or '_'
# 	name=k.get('name') or '.*'
# 	parent=k.get('parent') or '.*'
# 	f'([{pfx}]*)'
# 	f'([{sep}]?)'
# 	f'({name})'
# 	f'({name})'
# 	gPFX=r'(?P<PFX>{RE})'.format(RE=PFX)
# 	gSEP=r'(?P<SEP>{RE})'.format(RE=SEP)
# 	gNME=r'(?P<NME>{RE})'.format(RE=NME)
# 	gCON=f'^{gPFX}{gSEP}{gNME}$'
# 	rex=re.compile(gCON ,re.VERBOSE)
# 	return rex


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



def ShortNames(wgt):
	return {name.split('_')[1]:wgt['Elements'][name]for name in wgt['Elements']}


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
			with contextlib.suppress(KeyError) as e:
				# print(e)
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
	wgt['Fnx'] = wgt.get('Fnx') or {}
	wgt	=	Show(wgt)
	wgt = makeConfigure(wgt)
	if isinstance(wgt.get('Elements'),dict):
		wgt	=	Generate(wgt)
	return wgt

def minInit(wgt):
	wgt['Fnx']['Configure'](wgt)
	if isinstance(wgt.get('Elements'),dict):
		wgt['Fnx']['Generate']()
	wgt['Fnx']['Init']()
	return wgt

