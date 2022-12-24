#!/usr/bin/env python
# Auth
import re

def Rex(regex):
	return re.compile(regex,re.X)

def RE_QTMTD(pfx):
	def re_Mtd(n, e):	return r'(?P<{NAME}>{EX})'.format(NAME=n,EX=e)
	RE_IS=re_Mtd('IS', 'is')
	RE_SET=re_Mtd('SET', 'set')
	RE_MTD=re_Mtd('MTD', '[A-Za-z]*')
	REX={
	'IS': Rex(re_Mtd('ISMTD',f'^{RE_IS}?{RE_MTD}$')),
	'SET':Rex(re_Mtd('ISMTD',f'^{RE_SET}?{RE_MTD}$'))}

	return REX.get(pfx)

def Name(wgt,**k):
	name											=	k['Name']
	wgt['Name']									=	name
	return wgt

# re.compile(r'^(?P<ALLWORDS>(?P<CAPWORD>(?P<CAP>[A-Z])(?P<WORD>[a-z]*))*)$')