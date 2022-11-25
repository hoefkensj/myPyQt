#!/usr/bin/env python
# Auth
import lib.Create
import lib.gnr
import lib.QElements.QTextButton
import lib.QElements.QIconButton
import lib.QtWgt


def QHSearch(**k):

	def Cfg():
		c={
			'ObjectName'				:		w['Name'],
			'SizePolicy'				:		lib.gnr.makeSizePolicy(k['pol']),
			'ContentsMargins'		:		k['margin'],
		}
		return c
	def Elements():
		parent=w['name']
		e		= {}
		e|= gnr.Element(lib.QtWgt.make(f'chk_RegEx_{parent}',pfx='lbl',pol='F.F'))
		e|= gnr.Element(lib.QtWgt.make(f'txt_Field_{parent}',pfx='txtE',pol='E.F'))
		# e|= gnr.Element(QtWgt.make(f'ctl_{parent}',pfx='txtE',pol='E.F'))
		return e

	def Fnx():


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
	def Init(wgt):
		s={name.split('_')[1]:w['Elements'][name]for name in w['Elements']}
		s['Name']['Set']['Text'](w['name'])
		s['Set']['Set']['Hidden'](True)
		# s['Set']['Set']['Text']('Set')
		s['Field']['Set']['ReadOnly'](True)
		s['Dupl']['Set']['Hidden'](True)
		wgt['Fnx']['Editable'](not k['ed'])
		wgt['Fnx']['Generate']()
		return wgt


	w=lib.QWgt.make(k['name'],**k)
	w['Elements'] = Elements()
	w['Fnx'] 			|=	Fnx(w)
	w['Con']			=	Con(w)
	return Init(w)


def make(namestr,**k):
	k={
		'ed'        :	True							,
		'margin'    :	[0,0,0,0]					,
		'pol'       :	'E.F'							,
		't'         :	'H'								,
	} |	k	|	{
		'pfx'       :	'wgt'							,
		'name'      :	namestr							,
	}
	return  QHSearch(**k)

