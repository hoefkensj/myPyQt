#!/usr/bin/env python
# Auth
import lib.Create
import lib.gnr
import lib.QElements.QTextButton
import lib.QElements.QIconButton
import lib.QtWgt
import lib.QWgt

def QHSearch(**k):
	def Cfg():
		c={
			'ObjectName'				:		w['Name'],
			'SizePolicy'				:		lib.gnr.makeSizePolicy(k['pol']),
			'ContentsMargins'		:		k['margin'],
			**k
		}
		return c
	def Elements():
		parent=w['name']
		e		= {}
		e|= lib.gnr.Element(lib.QtWgt.make(f'RegEx_{parent}',pfx='chkB',pol='F.F'))
		e|= lib.gnr.Element(lib.QtWgt.make(f'Field_{parent}',pfx='txtE',pol='E.F'))
		e|= lib.gnr.Element(lib.QElements.QIconButton.make(f'<_{parent}', bi=False))
		e|= lib.gnr.Element(lib.QElements.QIconButton.make(f'>_{parent}', bi=False))
		e|= lib.gnr.Element(lib.QElements.QIconButton.make(f'Search_{parent}', bi=False))

		# e|= gnr.Element(QtWgt.make(f'ctl_{parent}',pfx='txtE',pol='E.F'))
		return e

	def Fnx(wgt):
		s={name.split('_')[1]:wgt['Elements'][name] for name in wgt['Elements']}

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
		def Init(wgt):
			def init():
				s={name.split('_')[1]:wgt['Elements'][name]for name in wgt['Elements']}
				s['RegEx']['Set']['Text']('RE')
				s['Field']['Set']['ReadOnly'](False)
			return init
		f = {}
		f['Search'] =	Show()
		f['Configure']	=	lib.gnr.Configure(wgt)
		f['Generate'] 	= lib.gnr.Generate(wgt)
		f['Init']				=	Init(wgt)
		return f
	def Con(w):
		s={name.split('_')[1]:w['Elements'][name]for name in w['Elements']}
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
		wgt['Fnx']['Configure']()
		wgt['Fnx']['Generate']()
		wgt['Fnx']['Init']()
		return wgt


	w=lib.QWgt.make(k['name'],**k)
	w['Elements'] = Elements()
	w['Fnx'] 			|=	Fnx(w)
	w['Con']			=	Con(w)
	return Init(w)


def make(namestr,**k):
	k={
		'ed'        :	True								,
		'margin'    :	[0,0,0,0]						,
		'pol'       :	'E.F'								,
		't'         :	'H'									,
	} |	k	|	{
		'pfx'       :	'wgt'								,
		'name'      :	f'{namestr}_Search'	,
	}
	return  QHSearch(**k)

