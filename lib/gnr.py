#!/usr/bin/env python
# Auth
from .PyQtX import QHBoxLayout,QVBoxLayout,QGridLayout,QFormLayout
from .PyQtX import QSizePolicy as QSP
from . PyQtX import QtGui

def Layouts(t):

	l				=		{
		'h'   :	QHBoxLayout,
		'v'   : QVBoxLayout,
		'g'   :	QGridLayout,
		'f'   :	QFormLayout,
						}
	return l[t.casefold()]


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

def Icon(ico):
	import base64
	icon_states={
		0 : QtGui.QIcon.State.On,
		1 :	QtGui.QIcon.State.Off,	}
	icon = QtGui.QIcon()
	def  make_icon(icon,state):
		with open(f'icon{state}.svg','wb') as l:
			l.write(base64.b64decode(ico[state]))
		icon.addPixmap(QtGui.QPixmap(f'icon{state}.svg'), QtGui.QIcon.Mode.Normal, icon_states[state])
		return icon
	# with open('icond.svg','wb') as d:
	# 	d.write(base64.b64decode(ico[n][1]))
	icon = make_icon(icon,0)
	icon = make_icon(icon,1)
	return icon
	
def sizePol(**k):
	def SizePols(a):
		p={
				'P'   : QSP.Policy.Preferred,
				'M'   : QSP.Policy.Maximum,
				'm'   : QSP.Policy.Minimum,
				'E'   :	QSP.Policy.Expanding,
				'mE'  :	QSP.Policy.MinimumExpanding,
				'F'   :	QSP.Policy.Fixed,
			}
		return p.get(a)
	hp=k.get('h') or 'P'
	vp=k.get('v') or 'P'
	pol=QSP(SizePols(hp),SizePols(vp))
	return pol

def Names(**k):
	pfx_name	=k.get('n')
	name			=k.get('name')
	pfx				=k.get('pfx')
	if pfx_name:
		pfxname= pfx_name.split('_') #should be replaced with regex
		pfx=pfxname.pop(0)
		name='_'.join(pfxname)
	else:
		pfx_name='{PFX}_{NAME}'.format(PFX=pfx,NAME=name)
	return {'pfx_name':pfx_name,'pfx':pfx,'name':name}