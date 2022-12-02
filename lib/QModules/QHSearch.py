#!/usr/bin/env python
# Auth
from lib import gnr
from lib.QElements import QtWgt
from Configs import QDefaults,Config
from lib.QElements import QIconButton
from lib.QBases import QWidget
from lib.QModules	import QHSearchCtl
def QHSearch(**k):
	def Elements(wgt):
		if 'Elements' not in wgt:wgt['Elements'] = {}
		parent=wgt['name']
		wgt['Elements'] |= gnr.Element(QtWgt.make(f'Field_{parent}', pfx='txtE', pol='E.F'))
		wgt['Elements'] |= gnr.Element(QIconButton.make(f'Reg_{parent}',AutoRaise=True, bi=True))
		wgt['Elements'] |= gnr.Element(QHSearchCtl.make(f'ctl_{parent}', bi=False))
		# e|= gnr.Element(QtWgt.make(f'ctl_{parent}',pfx='txtE',pol='E.F'))
		return wgt

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
		def Visible(wgt):
			def visible(state):
				w['Wgt']['Set']['Visible'](state)
			return visible
		def Init(wgt):
			def init():
				pass
			return init
		wgt=gnr.Fnx(wgt)
		wgt['Fnx']['Init']		=	Init(wgt)
		wgt['Fnx']['Visible'] =	Visible(wgt)
		return wgt
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
	w						=	QWidget.make(k['name'], **k)
	w						=	Config.make(w,**k)
	w						= Elements(w)
	w						=	Fnx(w)
	w['Con']			=	Con(w)
	return gnr.minInit(w)


def make(namestr,**k):
	k	= {
		**QDefaults.Properties						,
		'ed'        :	True								,
		'pol'       :	'E.F'								,
		't'         :	'H'									,
	} |	k	|	{
		'pfx'       :	'wgt'								,
		'name'      :	f'{namestr}_Search'	,
	}
	return  QHSearch(**k)

