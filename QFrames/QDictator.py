#!/usr/bin/env python
# Auth
from PyQt6 import QtWidgets,QtCore,QtSvg

from lib import gui,gnr,QtWgt
from lib.QModules import QHIncDec,QHSearch, QEditProp



GUI=gui.make('TEST')

# GUI['Elements']|=gnr.Element(component)

GUI['Elements']|= gnr.Element(QHSearch.make('Tree',margin=[0,0,0,0],Spacing=0))
GUI['Elements']|= gnr.Element(QEditProp.make('Key',margin=[0,0,0,0],Spacing=0))
GUI['Elements']|= gnr.Element(QEditProp.make('Val',margin=[0,0,0,0],Spacing=0))

# GUI['Elements']|= gnr.Element(QHIncDec.make('ColEx'))
# GUI['Elements']|= gnr.Element(QHSearch.make('Search'))
# GUI['Main']['Elements'] |= gnr.Element(QtWgt.make('iBtn_Edit'))
# GUI['Main']['Lay']['Lay'].addWidget(GUI['Main']['Elements']['iBtn_Edit']['Wgt'])
GUI['Run']()



# GUI['Elements'](QSearch.make_QSearch('SearchTree'))
# GUI['Elements'](QSearch.make_QSearchCtl('Search'))
# GUI['Elements'](QHSearch.make('TrSearch'))
# GUI['Fnx']['Add'](  QtWgt.make('trw_RegEx',))
# GUI['Elements'](elements.make_iBtn('Search'))
#
# GUI['Elements'] |= QtWgt.make(n='txt_EditProp')
# GUI['Elements'] |= elements.chkBox('RegEx')
# GUI['Elements'] |= QtWgt.make(n='chk_RegEx',)
# GUI['Elements'] |= QtWgt.make(n='trw_Tree')
# GUI['Elements'] |= QtWgt.make(n='lbl_Tree')
# GUI['Elements']['lbl_Tree']['Mtd']['setText']('Tree')