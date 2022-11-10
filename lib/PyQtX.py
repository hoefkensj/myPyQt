#!/usr/bin/env python
# Auth
from PyQt6 import QtCore,QtWidgets,QtGui
QtCore=QtCore
QtWidgets=QtWidgets
QtGui=QtGui

Qt=QtCore.Qt

QApplication	=QtWidgets.QApplication
QWidget				=QtWidgets.QWidget
QTreeWidget		=QtWidgets.QTreeWidget
QLabel				=QtWidgets.QLabel

QHBoxLayout		=QtWidgets.QHBoxLayout
QVBoxLayout		=QtWidgets.QVBoxLayout
QGridLayout		=QtWidgets.QGridLayout
QFormLayout		=QtWidgets.QFormLayout


QSizePolicy		=QtWidgets.QSizePolicy
Policy				=QSizePolicy.Policy
Preferred			=Policy.Preferred
Fixed					=Policy.Fixed
Minimum				=Policy.Minimum
Maximum				=Policy.Maximum
Expanding			=Policy.Expanding


ToolButtonStyle=Qt.ToolButtonStyle
ToolButtonIconOnly=ToolButtonStyle.ToolButtonIconOnly
ToolButtonTextOnly=ToolButtonStyle.ToolButtonTextOnly
ToolButtonFollowStyle=ToolButtonStyle.ToolButtonFollowStyle
ToolButtonTextBesideIcon=ToolButtonStyle.ToolButtonTextBesideIcon
ToolButtonTextUnderIcon=ToolButtonStyle.ToolButtonTextUnderIcon

