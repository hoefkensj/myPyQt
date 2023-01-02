#!/usr/bin/env python
def attrs(lib):
		return ' '.join({f'{key}="{lib[key]}"' for key in lib})

def icodata(name):
	data={
		'edit'	:	[
			{	'path'	:	{
					'd' 		: 'm12.238 1-0.353 0.36-8.969 9.095-0.03 0.045c-0.061 0.099-0.27 0.45-0.583 1.088-0.314 0.638-0.7 1.51-1.012 2.492l-0.291 0.92 0.92-0.291a18.163 18.163 0 0 0 2.492-1.012c0.638-0.314 0.987-0.52 1.088-0.584l0.045-0.029 9.455-9.322zm-8.347 9.89 1.218 1.22-0.177 0.175c7e-3 -5e-3 -0.379 0.227-0.961 0.514-0.214 0.105-0.536 0.222-0.834 0.338l-0.274-0.274c0.116-0.298 0.233-0.62 0.338-0.834 0.287-0.582 0.518-0.966 0.514-0.96z',
					'fill'	: '{COLOR}',},},],
		'search'	:	 [
			{	'path'	:	{
					'd'			: 'm6.5 1c3.0376 0 5.5 2.4624 5.5 5.5 0 1.3388-0.4783 2.5659-1.2734 3.5196l4.127 4.1268c0.1952 0.1953 0.1952 0.5119 0 0.7072-0.1736 0.1735-0.443 0.1928-0.6379 0.0578l-0.0693-0.0578-4.1268-4.127c-0.9537 0.7951-2.1808 1.2734-3.5196 1.2734-3.0376 0-5.5-2.4624-5.5-5.5 0-3.0376 2.4624-5.5 5.5-5.5zm0 1c-2.4853 0-4.5 2.0147-4.5 4.5 0 2.4853 2.0147 4.5 4.5 4.5 2.4853 0 4.5-2.0147 4.5-4.5 0-2.4853-2.0147-4.5-4.5-4.5z',
					'fill'	: '{COLOR}'},},],
		'inc'		:	[
			{	'rect'	:	{
					'x' : '2',
					'y' : '7',
					'width' : '11',
					'height' : '1',
					'fill' : '{COLOR}',},},
			{	'rect'	:	{
					'x' : '2',
					'y' : '-8',
					'width' : '11',
					'height' : '1',
					'transform' : 'rotate(90)',
					'fill' : '{COLOR}',},},],
		'dec'			:	[
			{	'path'	:	{
					'd' : 'm3 8h10v1h-10z',
					'stroke-width' : '.70711',
					'fill' : '{COLOR}',},},],
		'>'				:	[
			{	'path':	{
					'd':'M 4.6367,1.6367 11,8 4.6367,14.3633 3.92967,13.65627 9.58587,8.00007 3.92967,2.34387 4.6367,1.63684 Z',
					'fill':'{COLOR}'},},],
		'<'				:	[
			{	'path':	{
					'd':'m 10.363 1.6367-6.3633 6.3633 6.3633 6.3633 0.70703-0.70703-5.6562-5.6562 5.6562-5.6562-0.70703-0.70703 z',
					'fill':'{COLOR}'},},],
	}
	return data.get(name.casefold())

def svgIcon(icon, theme):
		tags = {
				'svg'	: '<svg {ATTR} >{BODY}</svg>',
				'obj'	: '<{OBJ} {ATTR} />',
				'def'	:	'<defs>{BODY}</defs>',
				'css'	:	'<style {ATTR}>{BODY}</style',
		}
		data = {
			'attr': {
				'width'	: "16",
				'height': "16",
				'enable-background': "new",
				'version': "1.1",
				'xmlns'	: "http://www.w3.org/2000/svg",
			},
				'body': icodata(icon),
			}
		svg = {'tags': tags, 'data': data}
		themes = {'light': '#363636', 'dark': '#dedede'}
		body_list = []
		# breakpoint()
		for idx,obj in enumerate(svg['data']['body']):
				objstr = svg['tags']['obj']
				attr = attrs(svg['data']['body'][idx][[*svg['data']['body'][idx].keys()][0]])
				body_list.append(objstr.format(OBJ=[*svg['data']['body'][idx].keys()][0], ATTR=attr))
		body = '\n\t'.join(body_list)
		attr = attrs(svg['data']['attr'])
		svg_icon_skell = svg['tags']['svg'].format(BODY=body, ATTR=attr)
		with open(f'icon_{theme}.svg', 'w') as f:
				f.write(svg_icon_skell.format(COLOR=themes[theme]))


# svgIcon('Search','dark')