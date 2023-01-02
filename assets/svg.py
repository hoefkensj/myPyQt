#!/usr/bin/env python
def attrs(lib):
	return ' '.join({f'{key}="{lib[key]}"' for key in lib})

def dict2svg(icon,theme):
	tags = {'svg': '<svg {ATTR} >{BODY}</svg>', 'obj': '<{OBJ} {ATTR} />'}
	data = {
		'attr': {
			'width': "16",
			'height': "16",
			'enable-background': "new",
			'version': "1.1",
			'xmlns': "http://www.w3.org/2000/svg",
		},
		'body': icon,
	}
	svg = {'tags': tags, 'data': data}
	themes={'light':'#363636','dark': '#ffffff'}
	svg_icon_skell=svg['tags']['svg'].format(BODY='\n\t'.join([svg['tags']['obj'].format(OBJ=key, ATTR=attrs(svg['data']['body'][key])) for key in svg['data']['body']]) ,ATTR=attrs(svg['data']['attr']))
	with open(f'icon_{theme}.svg', 'w') as f:
		f.write(svg_icon_skell.format(COLOR=themes[theme]))



search = {'path': {}}
search['path']['d']="m6.5 1c3.0376 0 5.5 2.4624 5.5 5.5 0 1.3388-0.4783 2.5659-1.2734 3.5196l4.127 4.1268c0.1952 0.1953 0.1952 0.5119 0 0.7072-0.1736 0.1735-0.443 0.1928-0.6379 0.0578l-0.0693-0.0578-4.1268-4.127c-0.9537 0.7951-2.1808 1.2734-3.5196 1.2734-3.0376 0-5.5-2.4624-5.5-5.5 0-3.0376 2.4624-5.5 5.5-5.5zm0 1c-2.4853 0-4.5 2.0147-4.5 4.5 0 2.4853 2.0147 4.5 4.5 4.5 2.4853 0 4.5-2.0147 4.5-4.5 0-2.4853-2.0147-4.5-4.5-4.5z"
search['path']['fill']="{COLOR}"

dict2svg(search,'dark')
# print('{ATTR}'.format(ATTR=' '.join({f'{key}="{svg["attr"][key]}"' for key in svg['attr']})),'\n')
# sleep(0.01)
# subprocess.run(shlex.split(f'python {sys.argv[0]}'))


