#!/usr/bin/env python
import zlib,base64
import os

def get_themes():
	paths={
		'user' 		: os.path.expandvars('$HOME/.local/share/icons'),
		# 'system'	:	os.path.abspath('/usr/share/icons')
		}
	folders=[]
	themes={}
	for path in paths:
		folders=[dir for dir in os.listdir(paths[path]) if os.path.isdir(os.path.join(paths[path],dir))]

	for folder in folders:
		theme=folder.split('-')
		if theme[0] not in themes:
			if len(theme)>1:
				themes[theme[0]] = {theme[1]	: os.path.join(paths[path],folder)}
			else:
				themes[theme[0]] = {'regular': os.path.join(paths[path],folder)}
		else:
			if len(theme)>1:
				themes[theme[0]] |= {theme[1]	: os.path.join(paths[path],folder)}
			else:
				themes[theme[0]] |= {'regular': os.path.join(paths[path],folder)}
	return themes


themes=get_themes()
for theme in themes:
	print(theme)
	[print('\t',stheme, ' : ' , themes[theme][stheme] ) for stheme in themes[theme]]

theme=themes['Fluent']
for icon