#!/usr/bin/env python


from QLib.QBases import QModule

def Element(component):
	name=component.get('name')
	return {name : component}

def Module(name,elements,**k):
	def Elements(wgt):
		for element in elements:
			wgt['Elements']|= Element(element)
		return wgt

	def Connect(wgt):
		s=ShortEl(wgt);sCon=ShortEl(wgt, 'Con')
		for element in s:
			if not s[element].get('Con'):
				continue
			wgt['Con'][element]={con:sCon[element][con] for con in sCon[element]}
		return wgt

	w=QModule.make(name)
	w=Elements(w)
	w=w['Compile'](w)
	w=Connect(w)
	return Element(w)

def ShortEl(wgt, *a):
	s={}
	for name in wgt['Elements']:
		sub =wgt['Elements'][name]
		for item in a:
			sub=sub[item]
		s[name]=sub
	return s

def sCon(wgt, *conn):
	def addcon(name,s):
		s[name]=wgt['Con'][name].get(conn)
		return s

	s = {}
	for name in wgt['Con']:
		if conn :
			if conn[0] in wgt['Con']:
				s=addcon(name,s)
	return s
def ModCon(wgt):
	s=ShortEl(wgt)
	for element in s:
		wgt['Con'][element]=s[element]['Con']
	return wgt


def Clean(wgt):
	toclean=[]
	for section in wgt:
		if not wgt[section]:
			toclean+=[section]
	for section in toclean:
		wgt.pop(section)
	return wgt


def QWgtInit(wgt):
	wgt['Gen']['Config'](wgt)
	return wgt


def QElementInit(wgt):
	wgt['Gen']['Configure'](wgt)
	return wgt



