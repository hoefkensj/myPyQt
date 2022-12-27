#!/usr/bin/env python
from Configs import Config,QDefaults
from QLib.QStatic import QtLibs
from Fnx import QMake
import asyncio,multiprocessing,sys


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

	w=QtLibs.QElements.get('app')(sys.argv)
	w=(w:={construct(w,**k)	for construct in QMake.Construct('QApp')})


	return  w

def make(namestr,**k):
	return QtApplication(**(QDefaults.QApplication|k|{'Name':namestr}))

	# w=QMake.Configure(w)

#
# def main():
#
#     p = multiprocessing.Process(target=fun, args=('Peter',))
#     p.start()

def build_modifierset1(**k):
	w='modset1specific_startvalue'
	for modifier in modifiers('set1'): #would be a list of functions {'set1' : [mod1,mod2,mod5,mod99]}
		w=modifier(w,**k)

def mod1(x,**k): return {'id': x.__name__,'x' :initmodifier(x)}

def mod2(w,**k): return modfunction2(w)
