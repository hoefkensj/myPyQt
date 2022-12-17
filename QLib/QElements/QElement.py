#!/usr/bin/env python
def QElement(**k):
	w												=	dict()
	w['Name']								=	''
	w['name']								=	''
	w['type'] 							=	''
	w['Wgt']								=	()
	w['Gen']								=	{}
	w['Cfg']								= {}
	w['Fnx']								=	{}

	w['Fnx']['Set']					=	{}
	w['Fnx']['Get']					=	{}
	w['Fnx']['Sig']					=	{}
	w['Fnx']['Mtd']					=	{}
	w['Fnx']['Atr']					=	{}
	w['Con']								=	{}
	w['Elements']						=	{}
	return w