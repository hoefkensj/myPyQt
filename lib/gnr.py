#!/usr/bin/env python
# Auth
from inspect import ismethod
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QGridLayout,QFormLayout
from PyQt5.QtWidgets  import  QSizePolicy as QSP
def Layouts(t):

	l				=		{
		'H'   :	QHBoxLayout,
		'V'   : QVBoxLayout,
		'G'   :	QGridLayout,
		'F'   :	QFormLayout,
						}
	return l[t]
def SizePols():

	p={
			'P'   : QSP.Preferred,
			'M'   : QSP.Maximum,
			'm'   : QSP.Minimum,
			'E'   :	QSP.Expanding,
			'mE'  :	QSP.MinimumExpanding,
			'F'   :	QSP.Fixed,
		}
	return p


def Mtds(o):
	f={}
	for n in dir(o):
		m=getattr(o, n)
		if callable(m) and '__' not in n:
			f[n]=m
	return f

def Attr(o):
	v={}
	for n in dir(o):
		a=getattr(o, n)
		if not ismethod(a) and '__' not in n:
			v[n]=a
	return v

def Mtd():
	def mtd(w):
		m=Mtds(w)
		return m
	return mtd
def Atr():
	def atr(w):
		a=Attr(w)
		return a
	return atr
