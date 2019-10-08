# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qaps.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
# ...and that means losing the sideqt import, that deals with PySide if found, or falls back to Qt5


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

from sideqt import QtCore, QtWidgets


class UiMainWindow(object):
    def __init__(self):
        self.centralwidget = None
        self.horizontalLayout_4 = None
        self.horizontalLayout = None
        self.verticalLayout = None
        self.horizontalLayout_2 = None
        self.button_qopen = None
        self.button_qbackup = None
        self.label_qproject = None
        self.tree_ctrl_qtractor = None
        self.button_qsave = None
        self.verticalLayout_2 = None
        self.label = None
        self.button_q_to_a = None
        self.button_a_to_q = None
        self.label_2 = None
        self.button_q_to_a_track = None
        self.button_a_to_q_track = None
        self.label_3 = None
        self.button_q_to_a_all = None
        self.button_a_to_q_all = None
        self.label_4 = None
        self.verticalLayout_3 = None
        self.horizontalLayout_3 = None
        self.button_aopen = None
        self.button_abackup = None
        self.label_aproject = None
        self.tree_ctrl_ardour = None
        self.button_asave = None
        self.statusbar = None

    def setup_ui(self, mainwindow):
        mainwindow.setObjectName("MainWindow")
        mainwindow.resize(940, 658)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_qopen = QtWidgets.QPushButton(self.centralwidget)
        self.button_qopen.setObjectName("button_qopen")
        self.horizontalLayout_2.addWidget(self.button_qopen)
        self.button_qbackup = QtWidgets.QPushButton(self.centralwidget)
        self.button_qbackup.setEnabled(False)
        self.button_qbackup.setObjectName("button_qbackup")
        self.horizontalLayout_2.addWidget(self.button_qbackup)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_qproject = QtWidgets.QLabel(self.centralwidget)
        self.label_qproject.setText("")
        self.label_qproject.setObjectName("label_qproject")
        self.verticalLayout.addWidget(self.label_qproject)
        self.tree_ctrl_qtractor = QtWidgets.QTreeWidget(self.centralwidget)
        self.tree_ctrl_qtractor.setHeaderHidden(True)
        self.tree_ctrl_qtractor.setObjectName("tree_ctrl_qtractor")
        self.tree_ctrl_qtractor.headerItem().setText(0, "1")
        self.verticalLayout.addWidget(self.tree_ctrl_qtractor)
        self.button_qsave = QtWidgets.QPushButton(self.centralwidget)
        self.button_qsave.setEnabled(False)
        self.button_qsave.setObjectName("button_qsave")
        self.verticalLayout.addWidget(self.button_qsave)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label.setWordWrap(False)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.button_q_to_a = QtWidgets.QPushButton(self.centralwidget)
        self.button_q_to_a.setObjectName("button_q_to_a")
        self.verticalLayout_2.addWidget(self.button_q_to_a)
        self.button_a_to_q = QtWidgets.QPushButton(self.centralwidget)
        self.button_a_to_q.setObjectName("button_a_to_q")
        self.verticalLayout_2.addWidget(self.button_a_to_q)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.button_q_to_a_track = QtWidgets.QPushButton(self.centralwidget)
        self.button_q_to_a_track.setObjectName("button_q_to_a_track")
        self.verticalLayout_2.addWidget(self.button_q_to_a_track)
        self.button_a_to_q_track = QtWidgets.QPushButton(self.centralwidget)
        self.button_a_to_q_track.setObjectName("button_a_to_q_track")
        self.verticalLayout_2.addWidget(self.button_a_to_q_track)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.button_q_to_a_all = QtWidgets.QPushButton(self.centralwidget)
        self.button_q_to_a_all.setObjectName("button_q_to_a_all")
        self.verticalLayout_2.addWidget(self.button_q_to_a_all)
        self.button_a_to_q_all = QtWidgets.QPushButton(self.centralwidget)
        self.button_a_to_q_all.setObjectName("button_a_to_q_all")
        self.verticalLayout_2.addWidget(self.button_a_to_q_all)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_aopen = QtWidgets.QPushButton(self.centralwidget)
        self.button_aopen.setObjectName("button_aopen")
        self.horizontalLayout_3.addWidget(self.button_aopen)
        self.button_abackup = QtWidgets.QPushButton(self.centralwidget)
        self.button_abackup.setEnabled(False)
        self.button_abackup.setObjectName("button_abackup")
        self.horizontalLayout_3.addWidget(self.button_abackup)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.label_aproject = QtWidgets.QLabel(self.centralwidget)
        self.label_aproject.setText("")
        self.label_aproject.setObjectName("label_aproject")
        self.verticalLayout_3.addWidget(self.label_aproject)
        self.tree_ctrl_ardour = QtWidgets.QTreeWidget(self.centralwidget)
        self.tree_ctrl_ardour.setHeaderHidden(True)
        self.tree_ctrl_ardour.setObjectName("tree_ctrl_ardour")
        self.tree_ctrl_ardour.headerItem().setText(0, "1")
        self.tree_ctrl_ardour.header().setVisible(False)
        self.verticalLayout_3.addWidget(self.tree_ctrl_ardour)
        self.button_asave = QtWidgets.QPushButton(self.centralwidget)
        self.button_asave.setEnabled(False)
        self.button_asave.setObjectName("button_asave")
        self.verticalLayout_3.addWidget(self.button_asave)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.statusbar.setToolTip("")
        self.statusbar.setStatusTip("")
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)

        self.retranslate_ui(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslate_ui(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("MainWindow", "Qaps"))
        self.button_qopen.setText(_translate("MainWindow", "Open Qtractor Project"))
        self.button_qbackup.setText(_translate("MainWindow", "BACKUP Qtractor Project"))
        self.button_qsave.setText(_translate("MainWindow", "Save Qtractor Project"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Plugin</p></body></html>"))
        self.button_q_to_a.setText(_translate("MainWindow", ">"))
        self.button_a_to_q.setText(_translate("MainWindow", "<"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Track</p></body></html>"))
        self.button_q_to_a_track.setText(_translate("MainWindow", ">>"))
        self.button_a_to_q_track.setText(_translate("MainWindow", "<<"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>All</p></body></html>"))
        self.button_q_to_a_all.setText(_translate("MainWindow", ">>>>"))
        self.button_a_to_q_all.setText(_translate("MainWindow", "<<<<"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.button_aopen.setText(_translate("MainWindow", "Open Ardour Project"))
        self.button_abackup.setText(_translate("MainWindow", "BACKUP Ardour Project"))
        self.button_asave.setText(_translate("MainWindow", "Save Ardour Project"))
