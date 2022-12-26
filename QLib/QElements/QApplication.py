#!/usr/bin/env python
from Configs import Config
from QLib.QStatic import QtLibs
from QLib.QStatic import skel
from Fnx import QMake
from Configs import QDefaults
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

	w={}
	for fn in QMake.Construct('QApp',**k):
		breakpoint()
		w=fn(w)
	w=QMake.Configure(w)
	return  w

def make(namestr,**k):
	return QtApplication(**(QDefaults.QApplication|k|{'Name':namestr}))




def main():

    p = multiprocessing.Process(target=fun, args=('Peter',))
    p.start()