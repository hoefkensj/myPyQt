#!/usr/bin/env python

import assets.ico
import QLib.PyQtX

def Icon(svg):
		import base64
		icon_states={
			0 : QLib.PyQtX.QtGui.QIcon.State.On,
			1 :	QLib.PyQtX.QtGui.QIcon.State.Off,	}
		icon = QLib.PyQtX.QtGui.QIcon()
		def  make_icon(icon,state):
			with open(f'icon{state}.svg','wb') as l:
				l.write(base64.b64decode(svg[state]))
			icon.addPixmap(
				QLib.PyQtX.QtGui.QPixmap(f'icon{state}.svg'),
				QLib.PyQtX.QtGui.QIcon.Mode.Normal,
				icon_states[state])
			return icon
		icon = make_icon(icon,0)
		icon = make_icon(icon,1)
		return icon

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

def IconSet(i):
	return assets.ico.get(i) if i in  assets.ico.names() else None

def Clean(wgt):
	toclean=[]
	for section in wgt:
		if isinstance(wgt[section],dict) and not section:
			toclean+=[section]
	for section in toclean:
		wgt.pop(section)
	return wgt

def Init(fn):
	def Pre(wgt,*a,**k):
		return wgt['Fnx']['Configure'](wgt)

	def init(wgt,*a,**k):
		wgt	=	Pre(wgt,*a,**k)
		wgt	=	fn(wgt,*a,**k)
		wgt	=	Post(wgt,*a,**k)
		return wgt

	def Post(wgt,*a,**k):
		# if callable(wgt['Fnx'].get('Init')):
		if 'Init' in wgt['Fnx']:
			wgt['Fnx']['Init']()
		return wgt

	return init
@Init
def QWgtInit(wgt):
	wgt['Fnx']['Generate'](wgt)
	return wgt
@Init
def QElementInit(wgt):
	wgt=Clean(wgt)
	return wgt



