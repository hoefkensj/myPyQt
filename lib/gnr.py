#!/usr/bin/env python
# Auth
import re
import assets.ico
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

def SetMtd(wgt):
	sets = wgt['Set']
	reads=wgt['Read']
	def setmtd(setm, *setv):
		Set=sets[setm]
		Set(*setv)
		Val=reads[setm]
		r={setm : Val()}
		return r
	return setmtd

def Icon(svg,wh,):
	def icon(ico):
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
	size   =	makeSize( wh[0],wh[1])
	ico    =	icon(svg)
	return {'Icon':ico,'IconSize':size,'Svg':svg}


def sizePol(*a,**k):
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
	if len(a)==1:
		hp=a[0][0]
		vp=a[0][1]
	else:
		hp=k.get('h') or a[0]
		vp=k.get('v') or a[1]
	pol=QSP(SizePols(hp),SizePols(vp))
	return pol

def pfxRex():
	PFX=r'([^_]*)'
	SEP=r'([_]?)'
	NME=r'(.*)'
	gPFX=r'(?P<PFX>{RE})'.format(RE=PFX)
	gSEP=r'(?P<SEP>{RE})'.format(RE=SEP)
	gNME=r'(?P<NME>{RE})'.format(RE=NME)
	gCON=f'^{gPFX}{gSEP}{gNME}$'
	rex=re.compile(gCON ,re.VERBOSE)
	return rex

def splitName(name):
	nrex=pfxRex()
	rrex=nrex.search(name)
	res={'pfx': rrex.group('PFX'),'name' : rrex.group('NME'),}
	return res

def makeName(namestr):
	pfxx=PfxMap()
	rex=pfxRex()
	if '_' in namestr:
		rrex=rex.search(namestr)
		if rrex.group('PFX') in pfxx:
			name	=	rrex.group('NME')
		else:
			name	=	namestr
	else:
		name	=	namestr

	return name
def makePfx(namestr):
	pfxx=PfxMap()
	rex=pfxRex()
	if '_' in namestr:
		rrex=rex.search(namestr)
		if rrex.group('PFX') in pfxx:
			pfx	=	rrex.group('PFX')
	return pfx

def PfxMap():
	Map={
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
	return Map

def ArgKwargs(defaults,**k):
	return defaults()|k


def SubQWgt(pfx):
	pfxx=PfxMap()
	qwgt= getattr(QtWidgets,pfxx[pfx])
	return qwgt

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
		'i'   : ToolButtonIconOnly,
		't'   :	ToolButtonTextOnly,
		'f'   :	ToolButtonFollowStyle,
		'i|t' :	ToolButtonTextBesideIcon,
		'i/t' :	ToolButtonTextUnderIcon,
		}
	return s[t.casefold()]


def Element(component):
	name=component['Name']
	return {name : component}

def Short(w):
	return {e.split('_')[1]: w['Elements'][e]for e in w['Elements']}

def IconSet(i):
	return assets.ico.get(i) if i in  assets.ico.names() else None