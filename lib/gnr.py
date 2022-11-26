#!/usr/bin/env python
# Auth
import re
import assets.ico
import contextlib
import lib.PyQtX
from static.QtLibs import QSizePolicies



# def SetMtd(wgt):
# 	sets = wgt['Set']
# 	reads=wgt['Read']
# 	def setmtd(setm, *setv):
# 		Set=sets[setm]
# 		Set(*setv)
# 		Val=reads[setm]
# 		r={setm : Val()}
# 		return r
# 	return setmtd

def Icon(svg,wh,):
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
	size   =	makeSize(wh)
	ico    =	icon(svg)
	return {'Icon':ico,'IconSize':size}




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
	return lib.PyQtX.QtCore.QSize(wh[0], wh[1])

def makeSizePolicy(pol):
	h,v = pol.split('.')
	return QSizePolicies['Pol'](QSizePolicies[h],QSizePolicies[v])


def Element(component):
	name=component['Name']
	return {name : component}

def Configure(wgt):
	def configure():
		if 'ContentsMargins' in wgt['Cfg']:
			wgt['Set']['ContentsMargins'](*wgt['Cfg'].pop('ContentsMargins'))

		for prop in wgt['Cfg']:
			with contextlib.suppress(KeyError):
				wgt['Set'][prop](wgt['Cfg'][prop])
		return wgt

	return configure



def ShortNames(wgt):
	return {name.split('_')[1]:wgt['Elements'][name]for name in wgt['Elements']}


def IconSet(i):
	return assets.ico.get(i) if i in  assets.ico.names() else None

def Generate(wgt):
	def generate():
		for element in 	wgt['Elements']:
			wgt['Fnx']['Add'](wgt['Elements'][element]['Wgt'])
	return generate

def Show(w):
	def show(state):
		w['Wgt']['Set']['Visible'](state)
	return show

def Fnx(wgt):
	f = {}
	f['Show'] 			=	Show(wgt)
	f['Configure']	=	Configure(wgt)
	f['Generate'] 	= Generate(wgt)
	return f

def minInit(wgt):
	wgt['Fnx']['Configure']()
	wgt['Fnx']['Generate']()
	wgt['Fnx']['Init']()
	return wgt