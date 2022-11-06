#!/usr/bin/env python
from .PyQtX import QtWidgets
from .gnr import Mtds,Atrs,Names,sizePol

def qwMtd(**k):
	m=k.get('m')
	mtds=Mtds(QtWidgets)
	return mtds[m]

def QtWgt(**k):
	def Wgt():
		wgt= qwMtd(m=Arg('qt'))
		return wgt()

	def Arg(a,Arg={}):
		def read():
			args={}
			args['qt']		= k.get('qt')
			args['n']			= k.get('n')
			args['name']	= k.get('name')
			args['m']			= k.get('m') or [0,0,0,0]
			args['pfx']		= k.get('pfx')
			args['vPol']	= k.get('vPol')
			args['hPol']	= k.get('hPol')
			return args
		if not Arg:	Arg= read()
		r = Arg.get(a)
		return r

	def Props():
		p={
			'Name' 					: Arg('n'),
			'SizePolicy'		:	sizePol(h=Arg('hPol'),v=Arg('vPol'))
			}
		return p

	def Mtd():
		wgt = w['Wgt']
		mtd=Mtds(wgt)
		return mtd

	def Atr():
		wgt = w['Wgt']
		atr=Atrs(wgt)
		return atr
	def Conn():
		c={}
		return c
	def Fnx():
		f={}
		return f
	def Init():
		P=w['Prp']
		def init():
			w['Mtd']['setObjectName'](P['Name'])
			w['Mtd']['setContentsMargins'](*Arg('m'))
			w['Mtd']['setSizePolicy'](P['SizePolicy'])
		init()
		return {'Init' : Init}

	w= {}
	w['Wgt']			=	Wgt()
	w['Prp']			= Props()
	w['Mtd']			=	Mtd()
	w['Atr']			= Atr()
	w['Con']			= Conn()
	w['Fnx']			=	Fnx()
	w['Init']			=	Init()
	return w

def Pfx2Qt(pfx):
	dct_Pfx={
	'lbl'		:	'QLabel',
	'trw'		:	'QTreeWidget',
	'txt'		:	'QLineEdit',
	'btn'		:	'QPushButton',
	'frm'		:	'QFrame',
	'grp'		:	'QGroupBox',
	'cmb'		:	'QComboBox',
	'chk'		:	'QCheckBox',
	'mnu'		:	'QMenu',
	'rdo'		:	'QRadioButton',
	'mbar'	:	'QMenuBar',
	'dSpn'	:	'QDoubleSpinBox',
	'pBtn'	:	'QPushButton',
	'tBtn'	:	'QToolButton',
	'iBtn'	:	'QToolButton',
	'wgt'		:	'QWidget',
	}
	qt=dct_Pfx.get(pfx)
	return qt

def make(**k):

	def n2names():
		makename	=	k.get('n')
		names			=	Names(n=makename)
		Pfx				=	names['pfx']
		Name			= names['name']
		Pfx_Name	=	names['pfx_name']
		return Pfx,Name,Pfx_Name
	def prepArgs():
		Pfx,Name,Pfx_Name=n2names()
		Qt=Pfx2Qt(Pfx)
		Args={}
		Args['Pfx']=Pfx
		Args['name']=Name
		Args['n']=Pfx_Name
		Args['qt']=Qt
		Args
		return Args
	Arg=prepArgs()

	return {Arg['n'] : QtWgt(**Arg)}

