#!/usr/bin/env python
# Auth
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



# def Size(wh):	return QCores['Size'](wh[0], wh[1])
# def SizePolicy(pol):
# 	h,v = pol.split('.')
# 	return QSizePolicies['Pol'](QSizePolicies[h],QSizePolicies[v])
# def Margins(margins):
# 	return QCores['Margins'](*margins)
#
# def make(component,*a):
#
# 	comps={
# 		'size'    : Size(*a)
# 		'sizpol'  : SizePolicy(*a)
# 		'margins' : Margins(*a)
# 	}


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
		if isinstance(wgt[section],dict) and len(wgt[section])==0:
			toclean+=[section]
	for section in toclean:
		wgt.pop(section)
	return wgt

def minInit(wgt):
	wgt=Clean(wgt)
	wgt['Fnx']['Configure'](wgt)
	if isinstance(wgt.get('Elements'),dict):
		wgt['Fnx']['Generate'](wgt)
	if callable(wgt['Fnx'].get('Init')):
		wgt['Fnx']['Init']()
	return wgt

