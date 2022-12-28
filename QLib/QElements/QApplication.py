#!/usr/bin/env python
from Configs import Config,QDefaults
from QLib.QStatic import QtLibs
from Fnx import QMake
import asyncio,multiprocessing,sys
from Fnx.debug import DebDec

def QApplication(**k):
	def Fnx(wgt):
		def Run(wgt):
			async def app():
				wgt['Qtm']['Mtd']['exec']()
			def run():
				asyncio.run(app())
			return run
		wgt['Fnx']={}
		wgt['Fnx']['Run'] = Run(wgt)
		wgt['Fnx']['Clip'] =		wgt['Qtm']['Mtd']['clipboard']()
		return wgt


	Constructs=QMake.Construct()
	w=QtLibs.QElements.get('app')(sys.argv)
	for construct in Constructs('QApp'):
		w=construct(w,Fnx,**k)

	return  w

def make(name,**k):
	return QApplication(**(QDefaults.QApplication|k|{'Name':name}))

	# w=QMake.Configure(w)

#
# def main():
#
#     p = multiprocessing.Process(target=fun, args=('Peter',))
#     p.start()