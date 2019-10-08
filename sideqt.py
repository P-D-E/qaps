#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright (c) 2019 Paolo D'Emilio
#
# This file is part of Qaps.
#
# Qaps is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Qaps is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Qaps.  If not, see <https://www.gnu.org/licenses/>.

try:
    from PySide2 import QtGui, QtWidgets, QtCore
    from PySide2.QtCore import Slot as pyqtSlot
    from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QTreeWidgetItem, QMessageBox
    pass
except ImportError:
    try:
        from PyQt5 import QtGui, QtWidgets, QtCore
        from PyQt5.QtCore import pyqtSlot
        from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTreeWidgetItem, QMessageBox
    except ImportError:
        pass
