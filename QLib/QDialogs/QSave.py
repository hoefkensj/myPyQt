#!/usr/bin/env python
def saveDialog():
	def saveDialog():
		Path, Type =QtWidgets.QFileDialog.getSaveFileName(QtWidgets.QWidget(),"Save As","","All Files (*)")
		return Path
	return saveDialog()