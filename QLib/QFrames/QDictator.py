#!/usr/bin/env python
# Auth
import sys
from QLib import gnr
from QLib.QModules import QGui
from QLib.QModules import QHIncDec,QHSearch, QEditProp
from QLib.QElements import QTree,QTextButton
from QLib.QBases import QModule


def module(name,*elements):
	def Elements(wgt):
		for element in elements:
			wgt['Elements']|=element
		return wgt

	def Connect(wgt):
#SHORT
		#SHORT
		for element in s:
			if element.get('Con'):
				for con in sCon[element]:
					wgt['Con'][element][con]=sCon[element][con]
		return wgt

	def Connect2(wgt):
		#SHORT
		#SHORT
		for element in s:
			if not element.get('Con'):
				continue
			for con in sCon[element]:
				wgt['Con'][element][con]=sCon[element][con]
		return wgt

	w=QModule.make(name)
	w=Elements(w)
	w=w['Fnx']['Run'](w)
	w=Connect(w)
	return w

def mod_TreeCtl(name):
	w=QModule.make(name)
	w['Elements']|=gnr.Element(QHIncDec.make('ColEx',wh=[20,20]))
	w['Elements']|=gnr.Element(QHSearch.make('TreeSearch',))
	w=w['Fnx']['Run'](w)
	#SHORT
	w['Con']['+']=sfn['ColEx']['Inc']
	w['Con']['-']=sfn['ColEx']['Dec']
	w['Con']['search']=sfn['TreeSearch']['Search']
	return w

def mod_AppCtl(name):
	w=QModule.make(name)
	w['Elements']|= gnr.Element(QTextButton.make('Update',pol='E.P',))
	w['Elements']|= gnr.Element(QTextButton.make('Print',pol='E.P',))
	w['Elements']|= gnr.Element(QTextButton.make('Exit',pol='E.P',))
	w=w['Fnx']['Run'](w)
#SHORT
	w['Con']['Update']=sfn['Update']
	w['Con']['Print']=sfn['Print']
	w['Con']['Exit']=sfn['Exit']
	w['Con']['Exit'](sys.exit)
	return w



def QDictator(**k):

	def Elements(m):
		# GUI['Elements']|=gnr.Element(component)
		m['Elements']	|= gnr.Element(QTree.make('Tree',cols=7,hidecols=[2,3,4,5,6]))
		m['Elements']	|= gnr.Module('TreeCtl',[
                      QHIncDec.make('ColEx',wh=[20,20]),
                      QHSearch.make('TreeSearch',)])
		# m['Elements']	|= gnr.Element(QEditProp.make('Key',))
		# m['Elements']	|= gnr.Element(QEditProp.make('Val',))
		m['Elements']	|= gnr.Module('AppCtl',[
                      QTextButton.make('Update',pol='E.P',),
                      QTextButton.make('Print',pol='E.P',),
                      QTextButton.make('Exit',pol='E.P',),])
		return m
	def Fnx(m):
		def Select(*a,**k):
#SHORT
			txtBox = [sFnx['Key']['txtText'], sFnx['Val']['txtText']]
			def select(data):
				for idx, txtbox in zip([0, 1, 2], txtBox):
					txtbox(data.text(idx))
			return select
		def AddDict(m):
			def adddict(**k):
				#use adddict(NAME=DICT)
				m['Elements']['Tree']['Fnx']['Add'](**k)
			return adddict
		def Allign(m):
#SHORT
			wMax = max(s['Key']['wLbl'](), s['Val']['wLbl']())+10
			s['Key']['Allign'](wMax)
			s['Val']['Allign'](wMax)
		m['Fnx']['Select']=Select
		m['Fnx']['AddDict']=AddDict(m)
		m['Fnx']['Allign']=Allign
		return m
	# def Connect(wgt):
	# 	s=gnr.ShortEl(wgt);sCon=gnr.ShortEl(wgt,'Con')
	# 	for element in s:
	# 		if not s[element].get('Con'):
	# 			continue
	# 		wgt['Con'][element]={con:sCon[element][con] for con in sCon[element]}
	# 	return wgt
	def Con(m):
		select=m['Fnx']['Select'](m)
#SHORT
		sACc=gnr.sCon(m,'itemSelected')
		for key in sClk:
			print(key)
		# ['Inc'](sFnx['Tree']['Mtd']['expandAll'])
		# sCon['TreeCtl']['+'](sFnx['Tree']['Mtd']['expandAll'])
		# sCon['TreeCtl']['-'](sFnx['Tree']['Mtd']['collapseAll'])
		# sClk['Print'](m['Elements']['trw_Tree']['Fnx']['PrintTree'])
		m['Con']['AppCtl']['Update'](m['Elements']['trw_Tree']['Fnx']['Update'])
		# sCon['Tree']['Item'](select)
		return m
	def Init(g):
		# g['Main']['Fnx']['Allign'](g['Main'])
		return GUI['Run'](GUI)

	GUI= QGui.make('Main')
	MAIN=GUI['Wgt']
	MAIN=Elements(MAIN)
	MAIN=Fnx(MAIN)



	# MAIN=Connect(MAIN)
	# MAIN=Con(MAIN)
	# GUI['Add']=MAIN['Fnx']['AddDict']
	# GUI['Fnx']['Main']()
	return Init(GUI),GUI

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

RUN,GUI=QDictator()
# ADD(GUI=GUI)
STDTree=pTree(d={**GUI},max=5)
print('################### DONE')
RUN()





