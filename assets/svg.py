#!/usr/bin/env python
from time import sleep
from asyncio import run
import subprocess

import sys,shlex
svg_tag=['','','']
svg_tag[0]='''<svg {ATTR} xmlns="http://www.w3.org/2000/svg">{BODY}'''
svg_tag[2]='''width="{}" height="{}" enable-background="{}" version="1.1"'''
svg_tag[1]='</svg>'


svg={}
svg['tag']='<svg {ATTR} >{BODY}</svg>'

# svg['attr']={}
# svg['attr']['width']="16"
# svg['attr']['height']="16"
# svg['attr']['enable-background']="new"
# svg['attr']['version']="1.1"
# svg['attr']['xmlns']="http://www.w3.org/2000/svg"

# svg['attr']={}
# svg['attr']|={'width' : "16"}
# svg['attr']|={'height' : "16"}
# svg['attr']|={'enable-background' : "new"}
# svg['attr']|={'version' : "1.1"}
# svg['attr']|={'xmlns' : "http://www.w3.org/2000/svg"}

svg['attr']={
'width' : "16",
'height' : "16",
'enable-background' : "new",
'version' : "1.1",
'xmlns' : "http://www.w3.org/2000/svg",}

svg['rect']={}
svg['rect']['x']="{}"
svg['rect']['y']="{}"
svg['rect']['width']="{}"
svg['rect']['height']="{}"
svg['rect']['fill']="{}"
svg['rect']['transform']="{}"



svg['path']={}
svg['path']['d']="m6.5 1c3.0376 0 5.5 2.4624 5.5 5.5 0 1.3388-0.4783 2.5659-1.2734 3.5196l4.127 4.1268c0.1952 0.1953 0.1952 0.5119 0 0.7072-0.1736 0.1735-0.443 0.1928-0.6379 0.0578l-0.0693-0.0578-4.1268-4.127c-0.9537 0.7951-2.1808 1.2734-3.5196 1.2734-3.0376 0-5.5-2.4624-5.5-5.5 0-3.0376 2.4624-5.5 5.5-5.5zm0 1c-2.4853 0-4.5 2.0147-4.5 4.5 0 2.4853 2.0147 4.5 4.5 4.5 2.4853 0 4.5-2.0147 4.5-4.5 0-2.4853-2.0147-4.5-4.5-4.5z"
svg['path']['fill']="#363636"


svg={}
svg['tag']='<svg {ATTR} >{BODY}</svg>'

# svg['attr']={}
# svg['attr']['width']="16"
# svg['attr']['height']="16"
# svg['attr']['enable-background']="new"
# svg['attr']['version']="1.1"
# svg['attr']['xmlns']="http://www.w3.org/2000/svg"

# svg['attr']={}
# svg['attr']|={'width' : "16"}
# svg['attr']|={'height' : "16"}
# svg['attr']|={'enable-background' : "new"}
# svg['attr']|={'version' : "1.1"}
# svg['attr']|={'xmlns' : "http://www.w3.org/2000/svg"}

svg['attr']={
'width' : "16",
'height' : "16",
'enable-background' : "new",
'version' : "1.1",
'xmlns' : "http://www.w3.org/2000/svg",}

	#print(svg['tag'].format(BODY='\n\t{BODY}\n' ,ATTR=' '.join({f'{key}="{svg["attr"][key]}"' for key in svg['attr']})))
print('{ATTR}'.format(ATTR=' '.join({f'{key}="{svg["attr"][key]}"' for key in svg['attr']})),'\n')
sleep(0.01)
subprocess.run(shlex.split(f'python {sys.argv[0]}'))


