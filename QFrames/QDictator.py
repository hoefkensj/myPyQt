#!/usr/bin/env python
# Auth


from lib import gui,gnr
from lib.QModules import QHIncDec,QHSearch, QEditProp

GUI=gui.make('TEST')
GUI['Elements']|= gnr.Element(QEditProp.make('Key'))
# GUI['Elements']|= gnr.Element(QEditProp.make('Val'))
# GUI['Elements']|= gnr.Element(QHIncDec.make('ColEx'))
# GUI['Elements']|= gnr.Element(QHSearch.make('Search'))
GUI['Run']()



# GUI['Elements'](QSearch.make_QSearch('SearchTree'))
# GUI['Elements'](QSearch.make_QSearchCtl('Search'))
# GUI['Elements'](QHSearch.make('TrSearch'))
# GUI['Fnx']['Add'](  QtWgt.make('trw_RegEx',))
# GUI['Elements'](elements.make_iBtn('Search'))
# GUI['Elements'] |= elements.iBtn('Edit',lbl='test')
# GUI['Elements'] |= QtWgt.make(n='txt_EditProp')
# GUI['Elements'] |= elements.chkBox('RegEx')
# GUI['Elements'] |= QtWgt.make(n='chk_RegEx',)
# GUI['Elements'] |= QtWgt.make(n='trw_Tree')
# GUI['Elements'] |= QtWgt.make(n='lbl_Tree')
# GUI['Elements']['lbl_Tree']['Mtd']['setText']('Tree')