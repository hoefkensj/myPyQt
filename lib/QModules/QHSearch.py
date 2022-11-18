#!/usr/bin/env python
# Auth
from . import QHSearchCtl
from .. import QtWgt, gnr, QWgt


def QSearch(**k):
	def defaults():return {
		'pfx'   :	'shw'				,
		'm'    :	[0,0,0,0]			,
		'hPol'  :	'F'						,
		'vPol'  :	'F'						,
		'w'    :	20						,
		'h'    :	20						,
		'lbl'   :	None					,
		}
	def Elements():
		parent=k.get('name')
		e		= {}
		e|= QtWgt.make(f'chk_RegEx_{parent}')
		e|= QtWgt.make(f'txt_Field_{parent}',vPol='F')
		e|= gnr.sPack(QHSearchCtl.make(f'Ctl_{parent}', bi=False))
		return e
	def ShortMtds():
		parent=k.get('name')
		rex=w['Elements'][f'chk_RegEx_{parent}']['Mtd']
		txt=w['Elements'][f'txt_Field_{parent}']['Mtd']
		ctl=w['Elements'][f'wgt_Ctl_{parent}']['Con']
		return rex,txt,ctl
	def Fnx():
		rex,txt,ctl=ShortMtds()

		# def dispPN(wgt):
		# 	def dispPN(show):
		# 		wgt.btnPrev.setHidden(not show)
		# 		wgt.btnNext.setHidden(not show)
		# 	return dispPN
		# def selNext(Tree):
		# 	def sel():
		# 		item=wgt.Found.pop(0)
		# 		Tree.setCurrentItem(wgt.Found[0])
		# 		wgt.Found.append(item)
		# 	return sel
		# def selPrev(Tree):
		# 	def sel():
		# 		item=wgt.Found.pop(-1)
		# 		Tree.setCurrentItem(item)
		# 		wgt.Found=[item,*wgt.Found]
		# 	return sel
		# wgt.showPN 	= dispPN(wgt)
		# wgt.selNext		=	selNext
		# wgt.selPrev		=	selPrev
		# return wgt
		def Show():
			def show(state):
				w['Wgt']['Mtd']['setVisible'](state)
			return show
		f = {}
		f['Search'] =	Show()
		return f
	def Con():
		rex,txt,ctl=ShortMtds()
		c = {}
		# c['chk_RegEx']=	rex['checkStateChecked'].connect
		# wgt.Find		=	wgt.btnSearch.clicked.conne
		# wgt.Next		= wgt.btnNext.clicked.connect
		# wgt.Prev		=	wgt.btnPrev.clicked.connect
		# c['iBtn_Search']=ctl['iBtn_Search']
		# c['iBtn_Prev']=ctl['iBtn_Prev']
		# c['iBtn_Next']=ctl['iBtn_Next']
		return c
	def Init(w):
		rex,txt,ctl=ShortMtds()
		for element in w['Elements']:
			w['Fnx']['Add'](w['Elements'][element])
		return w
	k = gnr.ArgKwargs(defaults,**k)
	w=	QWgt.make(k.get('name'),t='h',vPol='P',hPol='E')
	w['Name']			=	k.get('pfx_name')
	w['Elements'] = Elements()
	# w['Cfg']			= Cfg()
	w['Fnx'] 			|= Fnx()
	w['Con'] |=	Con()
	return Init(w)

def make(name,**k):
	Names=gnr.makeNames(name=name,pfx='wgt')
	kwargs={
	'pfx_name'  :	Names['pfx_name'],
	'pfx'       :	Names['pfx'],
	'name'      :	Names['name'],
	'qt'        : gnr.PfxMap('wgt'),}
	return QSearch(**kwargs,**k)

