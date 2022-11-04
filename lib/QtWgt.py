#!/usr/bin/env python
from  PyQt5 import QtWidgets
from myPyQt.lib import gnr
def QtWgt(**k):

	def Wgt():
		wgt=gnr.qwMtd(m=Arg('qt'))
		return wgt()

	def Arg(a):
		arg={}
		arg['qt']			= k.get('qt')
		arg['n']			= k.get('n')
		arg['m']			= k.get('m') or [0,0,0,0]
		arg['pfx']		= k.get('pfx') or k.get('qt')
		r = arg.get(a)
		return r

	def Props():
		p={
			'Name' 		: Arg('n'),
			}
		return p

	def Mtd():
		wgt = w['Wgt']
		mtd=gnr.Mtds(wgt)
		return mtd

	def Atr():
		wgt = w['Wgt']
		atr=gnr.Atrs(wgt)
		return atr
	def Conn():
		c={}
		return c
	def Fnx():
		f={}
		return f

	def Init():
		def init():
			w['Mtd']['setObjectName'](f'{Arg("pfx")}_{Arg("n")}')
			w['Mtd']['setContentsMargins'](*Arg('m'))
		init()
		return {'Init' : Init}

	w= {}
	w['Wgt']			=	Wgt()
	w['Prp']			= Props()
	w['Mtd']			=	Mtd()
	w['Atr']			= Atr()
	w['con']			= Conn()
	w['Fnx']			=	Fnx()
	w['Init']			=	Init()
	return w

def QtPfx(**k):
	pfx=k.get('pfx')
	qt=k.get('qt')

	dct_Pfx={
	'lbl' :	'QLabel',
	'trw'  :	'QTreeWidget',
	'txt' :	'QLineEdit',
	'pBtn'  :	'QPushButton',
	'frm' :	'QFrame',
	'grp' :	'QGroupBox',
	'dSpn'  :	'QDoubleSpinBox',
	'cmb' :	'QComboBox',
	'chk' :	'QCheckBox',
	'mbar'  :	'QMenuBar',
	'mnu' :	'QMenu',
	'pBtn'  :	'QPushButton',
	'tBtn'  :	'QToolButton',
	'rdo' :	'QRadioButton',
	}
	return dct_Pfx.get(pfx)

def make(**k):
	n=k.get('n')
	pfx_name= n.split('_') #should be replaced with regex
	name=pfx_name[-1]
	pfx=k.get('t') or pfx_name[0]
	qt=QtPfx(pfx=pfx)
	wgt=QtWgt(qt=qt,n=name,pfx=pfx)
	return {n:wgt}














