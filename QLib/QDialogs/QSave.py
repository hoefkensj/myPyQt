#!/usr/bin/env python
from Qt.QtLibs import QDialogs,QElements

def saveDialog():
	config=[
		QElements['wgt'](),
		"Save As",
		"",
		"All Files (*)",
	]
	def saveDialog():
		Path, Type =QDialogs['file'].getSaveFileName(*config)
		return Path
	return saveDialog()