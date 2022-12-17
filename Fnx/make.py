#!/usr/bin/env python
# Auth
from QStatic.QtLibs import QCores
from QStatic.QtLibs import QSizePolicies
from QStatic.QtLibs import QToolButtons
import assets.ico
import QStatic.PyQtX

def Size(wh):
	return QCores['Size'](wh[0], wh[1])

def SizePolicy(pol):
	h,v = pol.split('.')
	return QSizePolicies['Pol'](QSizePolicies[h],QSizePolicies[v])

def Margins(margins):
	return QCores['Margins'](*margins)

def ToolButtonStyle(style):
		return QToolButtons.get(style)

def Icon(svg):
		import base64
		icon_states={
			0 : QStatic.PyQtX.QtGui.QIcon.State.On,
			1 :	QStatic.PyQtX.QtGui.QIcon.State.Off,	}
		icon = QStatic.PyQtX.QtGui.QIcon()
		def  make_icon(icon,state):
			with open(f'icon{state}.svg','wb') as l:
				l.write(base64.b64decode(svg[state]))
			icon.addPixmap(
				QStatic.PyQtX.QtGui.QPixmap(f'icon{state}.svg'),
				QStatic.PyQtX.QtGui.QIcon.Mode.Normal,
				icon_states[state])
			return icon
		icon = make_icon(icon,0)
		icon = make_icon(icon,1)
		return icon

def IconSet(i):
	return assets.ico.get(i) if i in  assets.ico.names() else None
