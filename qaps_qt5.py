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

from sideqt import QApplication, QMainWindow, QFileDialog, QTreeWidgetItem, QMessageBox
from sideqt import pyqtSlot

from qapsqt5 import UiMainWindow
from qaps_common import MyFrame as MyBaseFrame


class MyQtFrame(MyBaseFrame, QMainWindow, UiMainWindow):

    def __init__(self):
        try:
            super().__init__()  # Python 3.X
        except TypeError:
            super(QMainWindow, self).__init__()  # Python 2.X

        # Set up the user interface from Designer.
        self.setup_ui(self)

        # Make some local modifications.
        self.set_status("Qtractor <-> Ardour Plugin Setter")

        # Connect up the buttons.
        self.button_qopen.clicked.connect(self.button_qopen_click)
        self.button_aopen.clicked.connect(self.button_aopen_click)
        self.button_q_to_a.clicked.connect(self.button_q_to_a_click)
        self.button_a_to_q.clicked.connect(self.button_a_to_q_click)
        self.button_q_to_a_track.clicked.connect(self.button_q_to_a_track_click)
        self.button_a_to_q_track.clicked.connect(self.button_a_to_q_track_click)
        self.button_q_to_a_all.clicked.connect(self.button_q_to_a_all_click)
        self.button_a_to_q_all.clicked.connect(self.button_a_to_q_all_click)
        self.button_qbackup.clicked.connect(self.button_qbackup_click)
        self.button_abackup.clicked.connect(self.button_abackup_click)
        self.button_qsave.clicked.connect(self.button_qsave_click)
        self.button_asave.clicked.connect(self.button_asave_click)

    def init_tree(self, gui_tree):
        gui_tree.takeTopLevelItem(0)
        w_root = QTreeWidgetItem(gui_tree)
        w_root.setText(0, "Tracks / Buses")
        return w_root

    def finalize_tree(self, gui_tree):
        gui_tree.expandToDepth(0)

    def append_item(self, gui_tree, parent, text, tag=None):
        new_item = QTreeWidgetItem(parent)
        new_item.setText(0, text)
        if tag:
            new_item.setText(1, tag)
        return new_item

    def show_message(self, title, message):
        QMessageBox.warning(self, title, message, QMessageBox.Ok)

    def set_label(self, label, text):
        label.setText(text)

    def set_status(self, text):
        self.statusBar().showMessage(text)

    def get_item(self, gui_tree, parent=False):
        item = {}
        if not parent:
            tree_item = gui_tree.currentItem()
        else:
            tree_item = gui_tree.currentItem().parent()
        item["id"] = tree_item
        item["text"] = tree_item.text(0)
        item["tag"] = tree_item.text(1)
        return item

    def get_file_to_open(self, title, file_types, last_dir):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, title, last_dir, file_types, options=options)
        return file_name

    def enable_buttons(self, buttons):
        for button in buttons:
            button.setEnabled(True)

    @pyqtSlot()
    def button_qopen_click(self):
        MyBaseFrame.qopen_click(self, "Qtractor projects (*.qtr)", [self.button_qbackup, self.button_qsave])

    @pyqtSlot()
    def button_aopen_click(self):
        MyBaseFrame.aopen_click(self, "Ardour projects (*.ardour)", [self.button_abackup, self.button_asave])

    @pyqtSlot()
    def button_qbackup_click(self):
        MyBaseFrame.qbackup_click(self)

    @pyqtSlot()
    def button_abackup_click(self):
        MyBaseFrame.abackup_click(self)

    @pyqtSlot()
    def button_q_to_a_click(self):
        MyBaseFrame.q_to_a_click(self)

    @pyqtSlot()
    def button_a_to_q_click(self):
        MyBaseFrame.a_to_q_click(self)

    @pyqtSlot()
    def button_q_to_a_track_click(self):
        MyBaseFrame.q_to_a_track_click(self)

    @pyqtSlot()
    def button_a_to_q_track_click(self):
        MyBaseFrame.a_to_q_track_click(self)

    @pyqtSlot()
    def button_q_to_a_all_click(self):
        MyBaseFrame.q_to_a_all_click(self)

    @pyqtSlot()
    def button_a_to_q_all_click(self):
        MyBaseFrame.a_to_q_all_click(self)

    @pyqtSlot()
    def button_qsave_click(self):
        MyBaseFrame.qsave_click(self)

    @pyqtSlot()
    def button_asave_click(self):
        MyBaseFrame.asave_click(self)


def run():
    import sys
    app = QApplication(sys.argv)
    ui = MyQtFrame()
    ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
