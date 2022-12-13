#!/usr/bin/env python

import assets.ico
import Qt.PyQtX
from QLib.QBases import QModule
def Icon(svg):
		import base64
		icon_states={
			0 : Qt.PyQtX.QtGui.QIcon.State.On,
			1 :	Qt.PyQtX.QtGui.QIcon.State.Off,	}
		icon = Qt.PyQtX.QtGui.QIcon()
		def  make_icon(icon,state):
			with open(f'icon{state}.svg','wb') as l:
				l.write(base64.b64decode(svg[state]))
			icon.addPixmap(
				Qt.PyQtX.QtGui.QPixmap(f'icon{state}.svg'),
				Qt.PyQtX.QtGui.QIcon.Mode.Normal,
				icon_states[state])
			return icon
		icon = make_icon(icon,0)
		icon = make_icon(icon,1)
		return icon

def Element(component):
	name=component.get('Name')
	return {name : component}

def Module(name,*elements,**k):
	def Elements(wgt):
		for element in elements:
			wgt['Elements']|= Element(element)
		return wgt

	def Connect(wgt):
		s=ShortEl(wgt);sCon=ShortEl(wgt, 'Con')
		for element in s:
			if not s[element].get('Con'):
				continue
			wgt['Con'][element]={con:sCon[element][con] for con in sCon[element]}
		return wgt

	w=QModule.make(name)
	w=Elements(w)
	w=w['Compile'](w)
	w=Connect(w)
	return Element(w)

def ShortEl(wgt, *a):
	s={}
	for name in wgt['Elements']:
		sub =wgt['Elements'][name]
		for item in a:
			sub=sub[item]
		s[name.split('_')[1]]=sub
	return s
def ShortCon(wgt, *a):
	s={}
	for name in wgt['Con']:

		sub =wgt['Con'][name]
		for item in a:
			sub=sub[item]
		s[name.split('_')[1]]=sub
	return s

def IconSet(i):
	return assets.ico.get(i) if i in  assets.ico.names() else None

def Clean(wgt):
	toclean=[]
	for section in wgt:
		if not wgt[section]:
			toclean+=[section]
	for section in toclean:
		wgt.pop(section)
	return wgt


def QWgtInit(wgt):
	wgt['Fnx']['Generate'](wgt)
	wgt['Fnx']['Configure'](wgt)
	return wgt


def QElementInit(wgt):
	wgt['Fnx']['Configure'](wgt)
	return wgt



