#!/usr/bin/env python

from lib import gnr,Create
from static.QtLibs import QElements

from Configs import QDefaults,Config
def Make_Tree():
	def make_tree(rwgt, branches=[], **k):
		keylist=[]
		def make_branch(root, dct, path ,keylist=keylist):
			for key in dct:
				data = dct[key]
				keylist+=[key]
				dictpath = f"{path}['{key}']"
				branch = QElements['TrItem']()
				branch.setText(0, str(key))
				branch.setText(3, dictpath)
				keystr=''.join([f"['{key}']" for key in keylist])
				branch.setText(4,keystr)
				if isinstance(data, dict):
					make_branch(branch, data, dictpath,keylist=keylist)
				else:
					data = str(data)
					w =rwgt['Read']['ColumnWidth'](1)
					data = repr(data) if callable(data) else data
					dispdata = f'{data[:w - 4]}...' if len(data) > w - 4 else data
					branch.setText(1, dispdata)
					branch.setText(2, data)
				keylist.pop(-1)

				root.addChild(branch)

		name = rwgt['name']
		data = k.get('data')
		data={**data}
		root = QElements['TrItem']()
		root.setText(0, name)
		root.setText(1, name)
		make_branch(root, data, name)
		return root
	return make_tree
def QTree(**k):
	def Fnx(wgt):
		def ResizeCols(wgt):
			def resizecols():
				wgt['Fnx']['expandAll']()
				wgt['Mtd']['resizeColumnToContents'](0)
				wgt['Mtd']['resizeColumnToContents'](1)
				wgt['Fnx']['collapseAll']()
			return resizecols
		def ReadColWidth(wgt):
			def readcolwidth():
				w1 = wgt['Mtd']['columnWidth'](0)
				w2 = wgt['Mtd']['columnWidth'](1)
				return [w1, w2]
			return readcolwidth
		def SetColWidth(wgt):
			def setcolwidth(col, rel=None, tot=None):
				if rel:
					w =wgt['Set']['ColumnWidth'](col)
					w = w + rel
				else:
					w = tot
				wgt['Set']['ColumnWidth'](col, w)
			return setcolwidth
		def Init(wgt):
			def init():

				wgt['Mtd']['show']()
			return init


		wgt=gnr.Fnx(wgt)
		wgt['Fnx']['Header']					= wgt['Set']['Header']

		wgt['Fnx']['CurrentItem']			=	wgt['Set']['CurrentItem']
		wgt['Fnx']['TopLevelItem']		=	wgt['Mtd']['addTopLevelItem']
		wgt['Fnx']['expandAll']				= wgt['Mtd']['expandAll']
		wgt['Fnx']['collapseAll']			= wgt['Mtd']['collapseAll']
		wgt['Fnx']['ResizeCols']			= ResizeCols(wgt)
		wgt['Fnx']['ReadColWidth']		= ReadColWidth(wgt)
		wgt['Fnx']['SetColWidth']			= SetColWidth(wgt)
		wgt['Fnx']['Init'] = Init(wgt)
		wgt['Fnx']['MakeTree']	= Make_Tree()
		return wgt

	def Con(wgt):
		wgt['Con'] = wgt.get('Con') or {}
		wgt['Con']['clicked'] = wgt['Sig']['itemClicked'].connect
		return wgt
	def Init(wgt):
		wgt=gnr.minInit(wgt)
		return wgt
	w						=			Create.QCreate(QElements['trW'], **k)
	w						=			Config.make(w,**k)
	w						=			Fnx(w)
	w						=			Con(w)
	return Init(w)

def make(namestr, **k):
	preset	=	QDefaults.TreeWidget |	{
		'Names'									:	['trw',namestr]			,
		'pol'										:	'E.E'									,
	}
	return QTree(**Config.preset(preset,**k))


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