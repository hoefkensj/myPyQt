#!/usr/bin/env python

from Qt.PyQtX import QtWidgets, QtCore

QSizePolicies = {
	'Pol': QtWidgets.QSizePolicy,
	'P'       :		QtWidgets.QSizePolicy.Policy.Preferred,
	'M'       :		QtWidgets.QSizePolicy.Policy.Maximum,
	'm'       :		QtWidgets.QSizePolicy.Policy.Minimum,
	'E'       :		QtWidgets.QSizePolicy.Policy.Expanding,
	'mE'      :		QtWidgets.QSizePolicy.Policy.MinimumExpanding,
	'F'       :		QtWidgets.QSizePolicy.Policy.Fixed,
}

QLayouts				=	{
	'H'       :		QtWidgets.QHBoxLayout,
	'V'       :		QtWidgets.QVBoxLayout,
	'G'       :		QtWidgets.QGridLayout,
	'F'       :		QtWidgets.QFormLayout,
}

QElements				=	{
	'app'     :		QtWidgets.QApplication,
	'lbl'     :		QtWidgets.QLabel,
	'trW'     :		QtWidgets.QTreeWidget,
	'txtE'    :		QtWidgets.QLineEdit,
	'btn'     :		QtWidgets.QPushButton,
	'frm'     :		QtWidgets.QFrame,
	'grp'     :		QtWidgets.QGroupBox,
	'cmbB'    :		QtWidgets.QComboBox,
	'chkB'    :		QtWidgets.QCheckBox,
	'mnu'     :		QtWidgets.QMenu,
	'rBtn'    :		QtWidgets.QRadioButton,
	'mBar'    :		QtWidgets.QMenuBar,
	'dSpn'    :		QtWidgets.QDoubleSpinBox,
	'pBtn'    :		QtWidgets.QPushButton,
	'tBtn'    :		QtWidgets.QToolButton,
	'iBtn'    :		QtWidgets.QToolButton,
	'wgt'     :		QtWidgets.QWidget,
	'TrItem'  :		QtWidgets.QTreeWidgetItem,
}

QToolButtons		=	{
	'I'       : 	QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly,
	'T'       :		QtCore.Qt.ToolButtonStyle.ToolButtonTextOnly,
	'FS'      :		QtCore.Qt.ToolButtonStyle.ToolButtonFollowStyle,
	'IT'      :		QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon,
	'It'      :		QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon,
}

QCores					=	{
	'Size'    :		QtCore.QSize,
	'Timer'   :		QtCore.QTimer,
	'Margins' :		QtCore.QMargins,
	}