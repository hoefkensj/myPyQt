#!/usr/bin/env python
from QLib import Create
from Configs import Config
import asyncio,multiprocessing

def QtApplication(**k):
	def Fnx(wgt):
		def Run(wgt):
			async def app():
				wgt['Fnx']['Qt']['Mtd']['exec']()
			def run():
				asyncio.run(app())
			return run
		wgt['Fnx']['Run'] = Run(wgt)
		return wgt
	w					=	Create.QApplication(**k)
	w					= 	Fnx(w)
	w['Clip'] =		w['Fnx']['Qt']['Mtd']['clipboard']()
	return w

def make(namestr,**k):
	preset={}
	k=Config.preset(['app',namestr],preset,**k)
	return QtApplication(**k)




def main():

    p = multiprocessing.Process(target=fun, args=('Peter',))
    p.start()