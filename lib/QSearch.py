#!/usr/bin/env python
# Auth
from . import QtWgt,gnr
from . import elements

from . import QWgt

def QPrevNext(**k):
	def defaults():return {
		'pfx'		:	'idw'				,
		'm'			:	[0,0,0,0]			,
		'hPol'	:	'F'						,
		'vPol'	:	'F'						,
		}
	def Elements():
		parent=k.get('name')
		e		= {}
		e|= elements.make_iBtn(f'Prev_{parent}', bi=False)
		e|= elements.make_iBtn(f'Next_{parent}', bi=False)
		return e
	def ShortMtds():
		parent=k.get('name')
		Prev=w['Elements'][f'iBtn_Prev_{parent}']['Mtd']
		Next=w['Elements'][f'iBtn_Next_{parent}']['Mtd']
		return Prev,Next
	def Fnx(): return {}
	def Con():
		inc,dec=ShortMtds()
		c = {}
		c['iBtn_Prev']=	inc['clicked'].connect
		c['iBtn_Next']=	dec['clicked'].connect
		return c
	def Init(w):
		for element in w['Elements']:
			w['Fnx']['Add'](w['Elements'][element])
		return w

	k,Arg = gnr.ArgKwargs(defaults,**k)
	w ={}
	w	=	QWgt.make(k.get('name'),t='h',vPol='P',hPol='P')
	w['Name']			=	k.get('pfx_name')
	w['Elements'] = Elements()
	w['Fnx'] 			|= 	Fnx()
	w['Con']			|=	Con()
	return Init(w)
def QSearchCtl(**k):
	def defaults():return {
		'pfx'		:	'idw'				,
		'm'			:	[0,0,0,0]			,
		'hPol'	:	'F'						,
		'vPol'	:	'F'						,
		}
	def Elements():
		parent=k.get('name')
		e		= {}
		e|= gnr.sPack(make_QPN(f'PrevNext_{parent}', bi=False))
		e|= elements.make_iBtn(f'Search_{parent}', bi=False)
		return e
	def ShortMtds():
		parent=k.get('name')
		search=w['Elements'][f'iBtn_Search_{parent}']['Mtd']
		prvnxt=w['Elements'][f'wgt_PrevNext_{parent}']['Con']
		return search,prvnxt
	def Fnx(): return {}
	def Con():
		search,pn=ShortMtds()
		c = {}
		c['iBtn_Search']=	search['clicked'].connect
		c['iBtn_Prev']=pn['iBtn_Prev']
		c['iBtn_Next']=pn['iBtn_Next']
		return c
	def Init(w):
		for element in w['Elements']:
			w['Fnx']['Add'](w['Elements'][element])
		return w

	k,Arg = gnr.ArgKwargs(defaults,**k)
	w ={}
	w	=	QWgt.make(k.get('name'),t='h',vPol='P',hPol='P')
	w['Name']			=	k.get('pfx_name')
	w['Elements'] = Elements()
	w['Fnx'] 			|= 	Fnx()
	w['Con']			|=	Con()
	return Init(w)
def QSearch(**k):
	def defaults():return {
		'pfx'		:	'shw'				,
		'm'			:	[0,0,0,0]			,
		'hPol'	:	'F'						,
		'vPol'	:	'F'						,
		'w'			:	20						,
		'h'			:	20						,
		'lbl'		:	None					,
		}
	def Elements():
		parent=k.get('name')
		e		= {}
		e|= QtWgt.make(f'chk_RegEx_{parent}')
		e|= QtWgt.make(f'txt_Field_{parent}',vPol='F')
		e|= gnr.sPack(make_QSearchCtl(f'Ctl_{parent}', bi=False))
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

	k,Arg = gnr.ArgKwargs(defaults,**k)
	w=	QWgt.make(k.get('name'),t='h',vPol='P',hPol='E')
	w['Name']			=	k.get('pfx_name')
	w['Elements'] = Elements()
	# w['Cfg']			= Cfg()
	w['Fnx'] 			|= Fnx()
	w['Con']			|=	Con()
	return Init(w)

def make_QPN(name,pfx='wgt',**k):
	Names=gnr.makeNames(name=name,pfx=pfx)
	kwargs={
	'pfx_name'	:	Names['pfx_name'],
	'pfx'				:	Names['pfx'],
	'name'			:	Names['name'],
		'qt'        : gnr.PfxMap(pfx),}
	qtwgt 		=	QPrevNext(**kwargs,**k)
	return qtwgt
def make_QSearchCtl(name,pfx='wgt',**k):
	Names=gnr.makeNames(name=name,pfx=pfx)
	kwargs={
	'pfx_name'	:	Names['pfx_name'],
	'pfx'				:	Names['pfx'],
	'name'			:	Names['name'],
		'qt'        : gnr.PfxMap(pfx),}
	qtwgt 		=	QSearchCtl(**kwargs,**k)
	return qtwgt
def make_QSearch(name,pfx='wgt',**k):
	Names=gnr.makeNames(name=name,pfx=pfx)
	kwargs={
	'pfx_name'	:	Names['pfx_name'],
	'pfx'				:	Names['pfx'],
	'name'			:	Names['name'],
		'qt'        : gnr.PfxMap(pfx),}
	qtwgt 		=	QSearch(**kwargs,**k)
	return qtwgt

def make(name,**k):
	wgt= make_QSearch(name,**k)
	return wgt