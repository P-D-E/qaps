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

import wx
from qapswx import WxFrame
from qaps_common import MyFrame as MyBaseFrame


class MyWxFrame(MyBaseFrame, WxFrame):

    def init_tree(self, gui_tree):
        gui_tree.DeleteAllItems()
        w_root = gui_tree.AddRoot("Tracks / Buses")
        return w_root

    def finalize_tree(self, gui_tree):
        w_root = gui_tree.GetRootItem()
        gui_tree.Expand(w_root)
        gui_tree.UnselectItem(w_root)

    def append_item(self, gui_tree, parent, text, tag=None):
        new_item = gui_tree.AppendItem(parent, text)
        if tag:
            gui_tree.SetItemData(new_item, tag)
        return new_item

    def show_message(self, title, message):
        msg = wx.MessageDialog(None, message, title)
        msg.ShowModal()

    def set_label(self, label, text):
        label.SetLabel(text)

    def set_status(self, text):
        self.label_status.SetLabel(text)
        self.label_status.Center(wx.HORIZONTAL)

    def get_item(self, gui_tree, parent=False):
        item = {}
        if not parent:
            tree_item = gui_tree.GetSelection()
        else:
            tree_item = gui_tree.GetItemParent(gui_tree.GetSelection())
        item["id"] = tree_item
        item["text"] = gui_tree.GetItemText(tree_item)
        item["tag"] = gui_tree.GetItemData(tree_item)
        return item

    def get_file_to_open(self, title, file_types, last_dir):
        fd = wx.FileDialog(self, message=title,
                           defaultDir=last_dir, defaultFile="",
                           wildcard=file_types, style=wx.FD_DEFAULT_STYLE,
                           pos=wx.DefaultPosition, size=wx.DefaultSize, name=wx.FileDialogNameStr)
        if fd.ShowModal() == wx.ID_OK:
            return fd.GetPath()
        else:
            return None

    def enable_buttons(self, buttons):
        for button in buttons:
            button.Enable(True)

    def button_qopen_click(self, event):
        MyBaseFrame.qopen_click(self, "Qtractor projects|*.qtr", [self.button_qbackup, self.button_qsave])

    def button_aopen_click(self, event):
        MyBaseFrame.aopen_click(self, "Ardour projects|*.ardour", [self.button_abackup, self.button_asave])

    def button_qbackup_click(self, event):
        MyBaseFrame.qbackup_click(self)

    def button_abackup_click(self, event):
        MyBaseFrame.abackup_click(self)

    def button_q_to_a_click(self, event):
        MyBaseFrame.q_to_a_click(self)

    def button_a_to_q_click(self, event):
        MyBaseFrame.a_to_q_click(self)

    def button_q_to_a_track_click(self, event):
        MyBaseFrame.q_to_a_track_click(self)

    def button_a_to_q_track_click(self, event):
        MyBaseFrame.a_to_q_track_click(self)

    def button_q_to_a_all_click(self, event):
        MyBaseFrame.q_to_a_all_click(self)

    def button_a_to_q_all_click(self, event):
        MyBaseFrame.a_to_q_all_click(self)

    def button_qsave_click(self, event):
        MyBaseFrame.qsave_click(self)

    def button_asave_click(self, event):
        MyBaseFrame.asave_click(self)


class MyApp(wx.App):
    def __init__(self):
        wx.App.__init__(self)
        self.frame = MyWxFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()

# end of class MyApp


def run():
    app = MyApp()
    app.MainLoop()


if __name__ == "__main__":
    run()
