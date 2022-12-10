#!/usr/bin/env python
from QLib import gnr,Create
from static.QtLibs import QElements
from Configs import Config,QDefaults
import sys

def Make_Tree(wgt):
	def make_tree(limit,branches=[], **k):
		keylist=[]
		l=0
		i=0
		def make_branch(root, dct, path ,keylist=keylist,limit=limit, l=l):
			nonlocal i
			l=l+1
			i=i+1
			for key in dct:
				data = dct[key]
				keylist+=[key]
				dictpath = f"{path}['{key}']"
				branch = QElements['TrItem']()
				branch.setText(0, str(key))
				branch.setText(3, dictpath)
				keystr=''.join([f"['{key}']" for key in keylist])
				branch.setText(4,keystr)
				branch.setText(5, str(l))
				branch.setText(6, str(i))
				if isinstance(data, dict):
					if l != limit:
						make_branch(branch, data, dictpath,keylist=keylist,limit=limit,l=l)
					else:
						branch.setText(1, f'+{len(data)} Items')
				else:
					i=i+1
					data = str(data)
					w =wgt['Fnx']['Get']['ColumnWidth'](1)
					data = repr(data) if callable(data) else data
					dispdata = f'{data[:w - 4]}...' if len(data) > w - 4 else data
					branch.setText(1, dispdata)
					branch.setText(2, data)
					branch.setText(5, str(l))
					branch.setText(6, str(i))
				print(l)
				keylist.pop(-1)

				root.addChild(branch)
		name = k['name']
		data = k['data']
		root = QElements['TrItem']()
		root.setText(0, name)
		root.setText(1, name)
		make_branch(root, data, name,limit=limit,l=l)
		return root
	return make_tree
def Print_Tree(wgt):
	def pTree(*a, **k):
		d = k.get('d')
		indent = k.get('indent') or 0
		keys=len(d.keys())
		for key in d:
			dkey=f'\x1b[32m{d[key]}()\x1b[0m' if callable(d[key]) else str(d[key])
			keys-=1
			if isinstance(d[key], dict):
				sys.stdout.write('  ┃  ' * (indent))
				sys.stdout.write('  ┗━━ ' if keys == 0 else '  ┣━━ ')
				sys.stdout.write(f'\x1b[1;34m{str(key)}:\x1b[0m\t')
				if len(d[key]) > 1000:
					sys.stdout.write(f'\x1b[1;31m(+ {len(d[key])} items)' + '\x1b[0m\n')
				else:
					sys.stdout.write('\n')
					if indent <= k.get('max'):

						pTree(d=d[key], indent=indent + 1,max=k.get('max'))
			else:
				sys.stdout.write('  ┃  ' * (indent))
				sys.stdout.write('  ┗━━ ' if keys == 0 else '  ┣━━ ')
				sys.stdout.write(f'{str(key)}\t:\t{dkey}\n')
	def print_tree():
		for element in wgt['Data']:
			pTree(d=element['data'],max=10)
	return print_tree
def QTree(**k):
	def Fnx(wgt):
		def Add(wgt):
			def add(**k):
				kv = k.popitem()
				wgt['Data']= wgt.get('Data') or []
				wgt['Data']+=[{'name':kv[0],'data': kv[1]}]
			return add
		def ResizeCols(wgt):
			def resizecols():
				wgt['Fnx']['Mtd']['expandAll']()
				for col in range(wgt['Fnx']['Get']['ColumnCount']()):
					wgt['Fnx']['Mtd']['resizeColumnToContents'](col)
				wgt['Fnx']['Mtd']['collapseAll']()
			return resizecols
		def ReadColWidth(wgt):
			def readcolwidth():
				w=[]
				for col in range(wgt['Fnx']['Get']['ColumnCount']()):
					w+=[wgt['Fnx']['Get']['ColumnWidth'](col)]
				return w
			return readcolwidth
		def SetColWidth(wgt):
			def setcolwidth(col, rel=None, tot=None):
				if rel:
					w =wgt['Fnx']['Set']['ColumnWidth'](col)
					w = w + rel
				else:
					w = tot
				wgt['Fnx']['Set']['ColumnWidth'](col, w)
			return setcolwidth
		def Update(wgt):
			addTLI=wgt['Fnx']['Mtd']['addTopLevelItem']
			def update():
				for element in wgt['Data']:
					trunk=wgt['Fnx']['MakeTree'](25,name=element['name'], data=element['data'])
					addTLI(trunk)
			return update
		wgt['Fnx']['ResizeCols']			= ResizeCols(wgt)
		wgt['Fnx']['ReadColWidth']		= ReadColWidth(wgt)
		wgt['Fnx']['SetColWidth']			= SetColWidth(wgt)
		wgt['Fnx']['MakeTree']				= Make_Tree(wgt)
		wgt['Fnx']['PrintTree']				= Print_Tree(wgt)
		wgt['Fnx']['Add']							=	Add(wgt)
		wgt['Fnx']['Update']					=	Update(wgt)
		return wgt

	def Con(wgt):
		wgt['Con']['clicked'] = wgt['Fnx']['Sig']['itemClicked'].connect
		return wgt

	def Init(wgt)     :
		wgt=gnr.QElementInit(wgt)
		return wgt

	w						=			Create.QComponent(QElements['trW'], **k)
	w						=			Fnx(w)
	w						=			Con(w)

	return Init(w)

def make(namestr, **k):
	preset	= QDefaults.TreeWidget
	k=Config.preset(['trw',namestr],preset,**k)
	return QTree(**k)


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