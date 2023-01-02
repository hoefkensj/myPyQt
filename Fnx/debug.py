#!/usr/bin/env python
import inspect
def DebDec(fn):
	def debdec(*a,**k):
		caller=inspect.stack()[1][3]
		callerparent=inspect.stack()[2][3]
		print(f'{callerparent}.{caller}')
		breakpoint()
		return fn(*a,**k)
	return debdec


name=[]
breakpoint()
name+=['somename']
breakpoint()
print(name)