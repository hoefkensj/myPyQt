#!/usr/bin/env python
# Auth
from inspect import ismethod
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QGridLayout,QFormLayout
from PyQt5.QtWidgets  import  QSizePolicy as QSP
from PyQt5 import QtGui
def Layouts(t):

	l				=		{
		'h'   :	QHBoxLayout,
		'v'   : QVBoxLayout,
		'g'   :	QGridLayout,
		'f'   :	QFormLayout,
						}
	return l[t.casefold()]
def SizePols():

	p={
			'P'   : QSP.Preferred,
			'M'   : QSP.Maximum,
			'm'   : QSP.Minimum,
			'E'   :	QSP.Expanding,
			'mE'  :	QSP.MinimumExpanding,
			'F'   :	QSP.Fixed,
		}
	return p

def Mtds(w):

	f = {}
	for n in dir(w):
		m1 = getattr(w, n)
		if callable(m1) and '__' not in n:
			f[n] = m1
	return f

def Atrs(w):
	v = {}
	for n in dir(w):
		a1 = getattr(w, n)
		if not callable(a1) and '__' not in n:
			v[n] = a1
	return v

def qwMtd(**k):
	m=k.get('m')
	mtds=Mtds(QtWidgets)

	return mtds[m]

def Icon(n=None,ico=None):
	import base64
	icon_states={
		0 : QtGui.QIcon.On,
		1 :	QtGui.QIcon.Off,	}
	icon = QtGui.QIcon()
	def  make_icon(icon,state):
		with open(f'icon{state}.svg','wb') as l:
			l.write(base64.b64decode(ico[n][state]))
		icon.addPixmap(QtGui.QPixmap(f'icon{state}.svg'), QtGui.QIcon.Normal, icon_states[state])
		return icon
	# with open('icond.svg','wb') as d:
	# 	d.write(base64.b64decode(ico[n][1]))
	icon = make_icon(icon,0)
	icon = make_icon(icon,1)
	return icon