#!/usr/bin/env python
# Auth
from . import QHSearchCtl
from .. import QtWgt, gnr, QWgt


def QSearch(**k):
	def defaults():return {
		'pfx'		:	'shw'					,
		'm'			:	[0,0,0,0]			,
		'pol'		:	'EF'					,
		'w' 		:	20						,
		'h'			:	20						,
		'lbl'		:	None					,
		}
	def Create(): return gnr.QtCreate(QWgt.make,defaults,**k)
	def Cfg():
		c= gnr.ArgKwargs(defaults, **k)
		c|={
			'sizepolicy'    :	gnr.sizePol(c.get('pol')),
			'margin'        :	c.get('m'),
		}
		return c
	def Elements():
		parent=w['name']
		n=[f'chk_RegEx_{parent}',f'txt_Field_{parent}',f'ctl_{parent}']
		e		= {}
		e[n[0]]= QtWgt.make(n[0],pol='PF')
		e[n[1]]= QtWgt.make(n[1],pol='EF')
		e[n[2]]= QHSearchCtl.make(n[2],pol='PF')
		return e
	def Short():
		parent=w['name']
		s={}
		s['rex']=w['Elements'][f'chk_RegEx_{parent}']
		s['txt']=w['Elements'][f'txt_Field_{parent}']
		s['ctl']=w['Elements'][f'wgt_Ctl_{parent}']
		return s
	def Fnx():
		s=Short()

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
				w['Wgt']['Set']['Visible'](state)
			return show
		f = {}
		f['Search'] =	Show()
		return f
	def Con():
		s=Short()
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
		s=Short()
		for element in w['Elements']:
			w['Fnx']['Add'](w['Elements'][element])
		return w

	w							=	Create()
	w['Cfg']			=	Cfg()
	w['Elements'] = Elements()
	w['Fnx'] 			|= Fnx()
	w['Con'] 			|=Con()
	return Init(w)

def make(name,**k):
	Names=gnr.makeNames(name=name,pfx='wgt')
	kwargs={
	'pfx_name'  :	Names['pfx_name'],
	'pfx'       :	Names['pfx'],
	'name'      :	Names['name'],
	'qt'        : gnr.PfxMap('wgt'),}
	return QSearch(**kwargs,**k)

