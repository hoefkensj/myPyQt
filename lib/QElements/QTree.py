#!/usr/bin/env python
import lib.Create
from  PyQt5.QtWidgets import QTreeWidget
from myPyQt.lib import gnr

def Tree(**k):

	def Wgt():
		return QTreeWidget()

	def Arg(a):
		arg={}
		arg['n']			= k.get("n")
		arg['m']			= k.get("m") or [0,0,0,0]
		r = arg.get(a)
		return r

	def Props():
		name 		= Arg('n')
		return locals()

	def Mtd():
		wgt = w['Wgt']
		mtd= lib.Create.Mtds(wgt)
		return mtd

	def Atr():
		wgt = w['Wgt']
		atr= lib.Create.Atrs(wgt)
		return atr

	def Fnx():
		f={}
		return f
	def Init():
		def init():
			w['Mtd']['setObjectName'](f'tree_{Arg("n")}')
			w['Mtd']['setContentsMargins'](*Arg('m'))

		init()
		return init

	w= {}
	w['Wgt']			=	Wgt()
	w['Prp']			= Props()
	w['Mtd']			=	Mtd()
	w['Atr']			= Atr()
	w['Fnx']			=	Fnx()
	w['Init']			=	Init()
	return w
	
def Tree(**k):
	def Wgt():
		wgt = make(n=c.get('n'), t=c.get('qt'))
		return wgt[c.get('n')]

	def c.get():
		arg={}
		arg['n']				= k.get('n') or 'Tree'
		arg['m']				= k.get('m') or [0,0,0,0]
		r = arg.get(a)
		return r
	def Fnx():
		f 					= {}
		f['setHeader']				= t['Mtd']['setHeader']
		f['addTopLevelItem']	=	t['Mtd']['addTopLevelItem']
		f['setColumnWidth']		=	t['Mtd']['setColumnWidth']
		f['setCurrentItem']		=	t['Mtd']['setCurrentItem']
		f['expandAll']				= t['Mtd']['expandAll']
		f['collapseAll']			= t['Mtd']['collapseAll']
		return f
	def Init():
		t['Wgt'] 	=	sPol(t['Wgt'], h='E', v='mE')
		def Init():
			t['Mtd']['setObjectName'](f'tree{n}')
			t['Mtd']['setAlternatingRowColors'](True)
			t['Mtd']['setAnimated'](True)
			t['Mtd']['setHeaderHidden'](True)
			t['Mtd']['setColumnCount'](5)
			t['Mtd']['hideColumn'](2)
			t['Mtd']['hideColumn'](3)
			t['Mtd']['hideColumn'](4)
			t['Mtd']['setMinimumHeight'](10)
			t['Mtd']['setAllColumnsShowFocus'](True)
			t['Mtd']['setMinimumHeight'](50)
			t['Mtd']['setContentsMargins'](*m)
			Init()
		return Init
	def Conn():
		c={}
		c['itemClicked']=t['Mtd']['itemClicked'].connect
		return c

	w={}
	w['Wgt'] 		= Wgt()
	w['Arg']		=	c.get()
	w['Mtd']		= Mtd(t)
	w['Data']		=	Data(t)
	w['Fnx']		= Fnx()
	w['Conn']		=	Conn()
	w['Init']		= Init()
	return t

# def __Tree(**k):
# 	def create():
# 		wgt = QtWidgets.QTreeWidget()
# 		wgt.setObjectName(name)
# 		return wgt
# 	def Init(wgt):
# 		wgt = sPol(wgt, h='E', v='mE')
# 		# wgt.setFrameShape(QtWidgets.QFrame.NoFrame)
# 		wgt.setAlternatingRowColors(True)
# 		wgt.setAnimated(True)
# 		wgt.setHeaderHidden(True)
# 		wgt.setColumnCount(5)
# 		wgt.hideColumn(2)
# 		wgt.hideColumn(3)
# 		wgt.hideColumn(4)
# 		wgt.setMinimumHeight(10)
# 		wgt.setAllColumnsShowFocus(True)
# 		wgt.setMinimumHeight(50)
# 		wgt.setContentsMargins(*margins)
# 		return wgt
# 	name = k.get('n') or 'Tree'
# 	margins = k.get('margin') or [0, 0, 0, 0]
# 	wgt = create()
# 	wgt = Init(wgt)
# 	return wgt
#
#
# def ___Tree(*a, **k):
#
#
# 	def create(wgt):
# 		wgt.Tree = w['Elements']['Tree']
# 		return wgt
# 	def init(wgt):
# 		wgt.Tree.setContentsMargins(*w['Data']['Margins'])
# 		wgt.setContentsMargins(*w['Data']['Margins'])
# 		return wgt
# 	def add(wgt, lay):
# 		lay.addWidget(wgt.Tree)
# 		return lay
# 	def fnx(wgt):
# 		def resizeCols(wgt):
# 			def resizeCols():
# 				wgt.Tree.expandAll()
# 				wgt.Tree.resizeColumnToContents(0)
# 				wgt.Tree.resizeColumnToContents(1)
# 				wgt.Tree.collapseAll()
# 			return resizeCols
# 		def colWidth(wgt):
# 			def colWidth():
# 				w1 = wgt.Tree.columnWidth(0)
# 				w2 = wgt.Tree.columnWidth(1)
# 				return [w1, w2]
# 			return colWidth
# 		def setColWidth(wgt):
# 			def setColWidth(col, rel=None, tot=None):
# 				if rel:
# 					w = wgt.Tree.columnWidth(col)
# 					w = w + rel
# 				else:
# 					w = tot
# 				wgt.Tree.setColumnWidth(col, w)
# 			return setColWidth
# 		f = {}
# 		f['fittCols'] = resizeCols(wgt)
# 		f['colWidth'] = colWidth(wgt)
# 		f['setColWidth'] = setColWidth(wgt)
# 		return f
# 	def conn(wgt):
# 		wgt.Selected = wgt.Tree.itemClicked.connect
# 		wgt.FoundSel = wgt.Tree.itemSelectionChanged.connect
# 		return wgt
# 	w = {}
# 	w['Data'] = data()
# 	w['Wgt'] = blk['Base']['wgt'](n=w['Data']['Name'], t='h')
# 	w['Wgt'] = blk['Base']['sPol'](w['Wgt'], h='E', v='mE')
# 	w['Elements'] = elements()
# 	w['Wgt'] = create(w['Wgt'])
# 	w['layout'] = w['Wgt'].lay
# 	w['layout'] = add(w['Wgt'], w['layout'])
# 	w['Fnx'] = fnx(w['Wgt'])
# 	w['Conn'] = conn(w['Wgt'])
# 	w['Wgt'] = init(w['Wgt'])
# 	return w