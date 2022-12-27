#!/usr/bin/env python
import PyQt6,sys,inspect
from PyQt6 import QtCore,QtGui,QtWidgets
import contextlib
def pTree(*a, **k):
	d = k.get('d')
	indent = k.get('indent') or 0
	keys=len(d.keys())
	for key in d:
		dkey=f'\x1b[32m{d[key]}()\x1b[0m' if callable(d[key]) else str(d[key])
		keys-=1
		if isinstance(d[key], dict):
			sys.stdout.write('  ┃  ' * (indent))
			sys.stdout.write('  ┗━━ ' if keys == 0 else '  ┣━━ ')
			sys.stdout.write(f'\x1b[1;34m{str(key)}:\x1b[0m\t')
			if len(d[key]) > 10:
				sys.stdout.write(f'\x1b[1;31m(+ {len(d[key])} items)' + '\x1b[0m\n')
			else:
				sys.stdout.write('\n')
				if indent <= k.get('max'):

					pTree(d=d[key], indent=indent + 1,max=k.get('max'))
		else:
			sys.stdout.write('  ┃  ' * (indent))
			sys.stdout.write('  ┗━━ ' if keys == 0 else '  ┣━━ ')
			sys.stdout.write(f'{str(key)}\t:\t{dkey}\n')
def branch(root):
	mp={}
	rdir=[item for item in dir(root) if '__' not in item ]
	for key in rdir:
		try:
			val=getattr(root,key)
		except AttributeError:
			continue
		if inspect.isclass(val)or inspect.ismethod(val) or inspect.ismodule(val):
			mp[key]= branch(val)
		else:
			mp[key]=str(val)
	return mp

mp=branch(PyQt6.QtWidgets)
pTree(d=mp,max=0)
