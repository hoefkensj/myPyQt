#!/usr/bin/env python
# Auth
import re

from .PyQtX import QtWidgets,QtGui,QtCore


def Layouts(t):
	from .PyQtX import QHBoxLayout,QVBoxLayout,QGridLayout,QFormLayout

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
	from .PyQtX import QSizePolicy as QSP
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

def makeNames(**k):
	def pfxRex(s):
		PFX=r'([^_]*)'
		SEP=r'([_]?)'
		NME=r'(.*)'
		gPFX=r'(?P<PFX>{RE})'.format(RE=PFX)
		gSEP=r'(?P<SEP>{RE})'.format(RE=SEP)
		gNME=r'(?P<NME>{RE})'.format(RE=NME)
		gCON=f'^{gPFX}{gSEP}{gNME}$'
		rex=re.compile(gCON ,re.VERBOSE)
		return rex.search(s)
	if k.get('n'):
		grps= pfxRex(k.get('n'))
		pfx = grps.group('PFX')
		name = grps.group('NME')
	else:
		pfx = k.get('pfx')
		name = k.get('name')
	
	pfx_name	=	'{PFX}_{NAME}'.format(PFX=pfx,NAME=name)
	return {'pfx_name':pfx_name,'pfx':pfx,'name':name}

def Pfx2Qt(pfx):
	dct_Pfx={
	'lbl'   :	'QLabel',
	'trw'   :	'QTreeWidget',
	'txt'   :	'QLineEdit',
	'btn'   :	'QPushButton',
	'frm'   :	'QFrame',
	'grp'   :	'QGroupBox',
	'cmb'   :	'QComboBox',
	'chk'   :	'QCheckBox',
	'mnu'   :	'QMenu',
	'rdo'   :	'QRadioButton',
	'mbar'  :	'QMenuBar',
	'dSpn'  :	'QDoubleSpinBox',
	'pBtn'  :	'QPushButton',
	'tBtn'  :	'QToolButton',
	'iBtn'  :	'QToolButton',
	'wgt'   :	'QWidget',
	}
	qt=dct_Pfx.get(pfx)
	return qt

def ArgKwargs(**k):
	kwargs=k.pop('defaults') or {}
	kwargs|=k
	def argkwargs(a):
		arg={ar : kwargs.get(ar) for ar in kwargs.keys()}
		return arg[a]
	return argkwargs

def qwMtd(**k):
	m=k.get('m')
	mtds=Mtds(QtWidgets)
	return mtds[m]

def makeSize(*a,**k):
	if len(a) != 1 or len(k) !=1:
		w=k.get('w') or a[0]
		h=k.get('h') or a[1]
	else:
		w=k.get('wh')[0] or a[0][0]
		h=k.get('wh')[0] or a[0][1]

	return QtCore.QSize(w,h)

def tBtnStyles(t):
	from .PyQtX import ToolButtonIconOnly,ToolButtonTextOnly,ToolButtonFollowStyle
	from .PyQtX import ToolButtonTextUnderIcon,ToolButtonTextBesideIcon
	s={
		'i' 	: ToolButtonIconOnly,
		't'		:	ToolButtonTextOnly,
		'f'		:	ToolButtonFollowStyle,
		'i|t'	:	ToolButtonTextBesideIcon,
		'i/t'	:	ToolButtonTextUnderIcon,
		}
	return s[t.casefold()]
