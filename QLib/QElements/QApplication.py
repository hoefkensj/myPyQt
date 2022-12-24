#!/usr/bin/env python
from Configs import Config
from QLib.QStatic import QtLibs
from QLib.QStatic import skel
from Fnx import QMake

import asyncio,multiprocessing


import sys

def QtApplication(**k):
	def Fnx(wgt):
		def Run(wgt):
			async def app():
				wgt['Qt']['Mtd']['exec']()
			def run():
				asyncio.run(app())
			return run
		wgt['Fnx']={}
		wgt['Fnx']['Run'] = Run(wgt)
		wgt['Fnx']['Clip'] =		wgt['Qt']['Mtd']['clipboard']()
		return wgt['Fnx']

	QAPP={
		'GROUP' : 'Elements',
		'TYPE'	: 'app',
		'ARGS'	: 'sys.argv' ,
	}
	w={}
	skl = skel.QApplication
	for key in skl:
		val=skl[key].format(**QAPP)
		w[key]=eval(val)


	w=w['Cfg'](w)
	return w





def make(namestr,**k):
	preset={}|{'Name':namestr}
	k= Config.preset(preset, **k)
	return QtApplication(**k)




def main():

    p = multiprocessing.Process(target=fun, args=('Peter',))
    p.start()