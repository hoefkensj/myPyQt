#!/usr/bin/env python
# Auth
import re
import assets.ico
from .PyQtX import QtWidgets,QtGui,QtCore


def Layouts(t):
	from .PyQtX import QHBoxLayout,QVBoxLayout,QGridLayout,QFormLayout
	if t is not None:
		l				=		{
			'h'   :	QHBoxLayout,
			'v'   : QVBoxLayout,
			'g'   :	QGridLayout,
			'f'   :	QFormLayout,
							}
		r=l[t.casefold()];n=r.__name__
	else:
		r=None;n='None'
	return {'name': n , 'layout': r}

def Mtds(w):
	f = {}
	for n in dir(w):
		m1 = getattr(w, n)
		if callable(m1):
			f[n] = m1
	return f

def Atrs(w):
	v = {}
	for n in dir(w):
		a1 = getattr(w, n)
		if not callable(a1):
			v[n] = a1
	return v

def SetMtd(wgt):
	sets=wgt['Set']
	reads=wgt['Read']
	def setmtd(setm, *setv):
		Set=sets[setm]
		Set(*setv)
		Val=reads[setm]
		r={setm : Val()}
		return r
	return setmtd

def SetMtds(wgt):
	mtds=wgt['Mtd']
	sets={};reads={}
	nocase=[]
	for mtd in mtds:
		if mtd.startswith('set'):
			short=mtd[3:]
			nocase+=[short.casefold()]
			sets[short]=mtds[mtd]
	for mtd in mtds:
		if mtd.startswith('is'):
			fix=mtd[2:]
		else:
			fix=f'{mtd[0].upper()}{mtd[1:]}'
		if mtd.casefold() in nocase:
			reads[fix]=mtds[mtd]
	SetMtds={'Set': sets,'Read': reads}
	return SetMtds

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

def makeNames(*a,**k):
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
	n= [a][0] or k.get('n')
	if n:
		print(n)
		grps= pfxRex(n)
		pfx = grps.group('PFX')
		name = grps.group('NME')
	else:
		pfx = k.get('pfx')
		name = k.get('name')
	
	pfx_name	=	'{PFX}_{NAME}'.format(PFX=pfx,NAME=name)
	return {'pfx_name':pfx_name,'pfx':pfx,'name':name}

def PfxMap(pfx):
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
	return Map[pfx]

def ArgKwargs(defaults,**k):
	return defaults()|k


def SubQWgt(pfx):
	qwgt= getattr(QtWidgets,PfxMap(pfx))
	return qwgt()

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

def QtCreate(QtFn,**k):
	w=dict()
	w['Name']			=	k['pfx_name']
	w['name']			=	k.pop('name')
	w							|=	QtFn(w['name'],**k)
	w['Mtd']			=	Mtds(w['Wgt'])
	w['Atr']			= Atrs(w['Wgt'])
	w							|= SetMtds(w)
	return w
def QCreate(QtFn,defaults,**k):
	k|=defaults()
	w=dict()
	w['Name']			=	k['pfx_name']
	w['name']			=	k.pop('name')
	w['Wgt']			=	QtFn()
	w['Mtd']			=	Mtds(w['Wgt'])
	w['Atr']			= Atrs(w['Wgt'])
	w							|= SetMtds(w)
	return w

def Element(component):
	name=component['Name']
	return {name : component}

def Short(w):
	return {[e.split('_')[0]]: w['Elements'][e]for e in w['Elements']}

def IconSet(i):
	name=assets.ico.iconname(i)
	return assets.ico.get(name) if name in  assets.ico.names() else None