#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# This is the platform independent part; the class MyFrame contains all the needed functions, and the stubs of the
# platform specific functions to be overridden in the relative descendant classes.

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

import os
import shutil
import datetime
import xml.etree.ElementTree as Et


class Counter(object):
    """
    This class is used to count multiple occurrences of the same plugin on a track, allowing their ordered copy.
    """
    c = None

    def __init__(self):
        """
        Initializes the empty dictionary
        """
        self.c = {}

    def inc(self, item):
        """
        Adds 1 to the item's count if present, sets it to 0 otherwise
        :param str item: the name of the item
        :return int: the updated zero-based count for the item
        """
        if item in self.c:
            self.c[item] = self.c[item] + 1
        else:
            self.c[item] = 0
        return self.c[item]


class MyFrame(object):
    """
    This is the platform independent class all the GUI classes derive from; it provides the common functions.
    """
    # Project file names
    file_qtractor = ""
    file_ardour = ""
    # Previous directories for the file open dialogs
    last_dir_qtractor = ""
    last_dir_ardour = ""
    # XML trees
    q_tree = None
    a_tree = None
    # References to GUI objects
    tree_ctrl_qtractor = None
    tree_ctrl_ardour = None
    label_qproject = None
    label_aproject = None
    button_qbackup = None
    button_abackup = None
    button_qsave = None
    button_asave = None

    # <editor-fold desc="Methods to be overridden in the toolkit-specific classes">
    def init_tree(self, gui_tree):
        """
        Clears a GUI tree and adds the root item
        :param gui_tree: the tree to work on
        :return: the root item or its id
        """
        return 1

    def finalize_tree(self, gui_tree):
        """
        Expands all the items in a GUI tree and deselects the eventually selected item
        :param gui_tree: the tree to work on
        """
        pass

    def append_item(self, gui_tree, parent, text, tag=None):
        """
        Appends an item to a GUI tree
        :param gui_tree: the tree to work on
        :param parent: the parent of the item to append
        :param str text: the text of the item
        :param str tag: the tag of the item
        :return: the id of the appended item
        """
        return 1

    def show_message(self, title, message):
        """
        Shows a message in a message box.
        :param str title: the message window title
        :param str message: the message
        """
        pass

    def set_label(self, label, text):
        """
        Sets the text in a label.
        :param label: the label to set
        :param str text: the text to be shown
        """
        pass

    def set_status(self, text):
        """
        Sets the text in a status bar or dedicated label.
        :param str text: the text to be shown
        """
        pass

    def get_item(self, gui_tree, parent=False):
        """
        Returns the current item or its parent from a GUI tree.
        :param gui_tree: the GUI tree
        :param bool parent: if True, the function must return the specified item's parent
        :return dict: a dict with the tree's currently selected item, or its parent if called with parent=True
        """
        item = {"id": "foo", "text": "bar", "tag": "baz"}
        return item

    def get_file_to_open(self, title, file_types, last_dir):
        """
        Asks for a file to be opened, via a file open dialog, and returns its name.
        :param str title: the file open dialog window title
        :param str file_types: the filter for the allowed file type(s)
        :param str last_dir: the previously used directory
        :return: the name of the chosen file, if any.
        """
        return ""

    def enable_buttons(self, buttons):
        """
        Enables a list of buttons.
        :param list buttons: list of buttons to enable
        """
        pass
    # </editor-fold>

    def get_selections(self):
        """
        Returns the GUI trees and their selected items, only if both are selected.
        :return: the GUI trees and their selected items, only if both are selected
        """
        try:
            a_tree = self.tree_ctrl_ardour
            q_tree = self.tree_ctrl_qtractor
            a_item = self.get_item(a_tree)
            q_item = self.get_item(q_tree)
            return q_tree, q_item, a_tree, a_item
        except AttributeError:
            return None, None, None, None

    def get_tracks(self):
        """
        Returns the names and tags of the selected items, but only if they're tracks.
        :return: the names and tags of the selected items, but only if they're tracks
        """
        q_gui_tree, q_item, a_gui_tree, a_item = self.get_selections()
        try:
            if a_item["tag"] in ["T", "B"] and q_item["tag"] in ["T", "B"]:
                return q_item["text"], q_item["tag"], a_item["text"], a_item["tag"]
            else:
                return "", "", "", ""
        except TypeError:
            return "", "", "", ""

    def get_tracks_and_plugins(self):
        """
        Returns the selected plugins, and the names and tags of the tracks they belong to.
        :return: the selected plugins, and the names and tags of the tracks they belong to
        """
        q_gui_tree, q_item, a_gui_tree, a_item = self.get_selections()
        q_plug = q_tag = a_plug = a_tag = ""
        try:
            q_plug = q_item["text"]
            q_tag = q_item["tag"]
            a_plug = a_item["text"]
            a_tag = a_item["tag"]
        except TypeError:
            pass
        print(q_plug, q_tag)
        print(a_plug, a_tag)
        if (a_plug.replace(" ", "_") != q_plug) or a_tag != "P" or q_tag != "P" or not a_plug or not q_plug:
            self.show_message("Qaps", "Select matching plugins in both projects")
            return None, None, None, None, None, None
        q_track = self.get_item(q_gui_tree, parent=True)
        a_track = self.get_item(a_gui_tree, parent=True)
        print(q_track["text"], q_track["tag"])
        print(a_track["text"], a_track["tag"])
        return q_track["text"], q_track["tag"], q_plug, a_track["text"], a_track["tag"], a_plug

    def backup_file(self, file_path):
        """
        Creates a backup of a file.
        :param str file_path: the file to backup
        :return str: the creation or failure message
        """
        file_dir, file_name = os.path.split(file_path)
        # prepend "qaps-<timestamp>-" to the backup file name
        backup_name = "qaps-" + datetime.datetime.now().isoformat().split(".")[0].replace(":", "-") + "-" + file_name
        backup_path = os.path.join(file_dir, backup_name)
        try:
            os.remove(backup_path)
        except FileNotFoundError:
            pass
        try:
            shutil.copyfile(file_path, backup_path)
            return "Backup created as " + backup_path
        except IOError:
            self.show_message("ATTENTION!", "BACKUP FAILED!")
            return "ATTENTION! BACKUP FAILED!"

    def a_fill(self, gui_tree, x_tree):
        """
        Fills Ardour's GUI tree with the data from a project's XML tree.
        :param gui_tree: the GUI tree to fill
        :param ElementTree x_tree: the project's XML tree
        """
        gui_root = self.init_tree(gui_tree)
        root = x_tree.getroot()
        try:
            tracks = root.find("Routes").findall("Route")
            for track in tracks:
                a_flags = track.find("PresentationInfo").attrib["flags"]  # This is Ardour 5.X specific
                if ("AudioTrack" in a_flags) or ("MidiTrack" in a_flags):  # it's a track
                    tag = "T"
                else:  # it's a bus
                    tag = "B"
                track_item = self.append_item(gui_tree, gui_root, track.get("name"), tag)
                plugins = track.findall("Processor")
                for plugin in plugins:
                    self.append_item(gui_tree, track_item, plugin.get("name"), "P")
            self.finalize_tree(gui_tree)
        except AttributeError:
            self.show_message("Attention", "This doesn't appear to be an Ardour 5.X project.")

    def q_track(self, gui_root, gui_tree, tracks, tag):
        """
        Appends all the specified tracks and their plugins to Qtractor's GUI tree.
        :param gui_root: the root item of Qtractor's GUI tree
        :param gui_tree: Qtractor's GUI tree
        :param list tracks: list of tracks to append
        :param str tag: the tag for the tracks; "T" for audio tracks, "B" for buses
        """
        for track in tracks:
            track_item = self.append_item(gui_tree, gui_root, track.attrib["name"], tag)
            try:
                plugins = track.findall(".//plugin")
                for plugin in plugins:
                    self.append_item(gui_tree, track_item, plugin.find("label").text, "P")
            except AttributeError:
                continue

    def q_fill(self, gui_tree, x_tree):
        """
        Fills Qtractor's GUI tree with the data from a project's XML tree.
        :param gui_tree: the GUI tree to fill
        :param ElementTree x_tree: the project's XML tree
        """
        gui_root = self.init_tree(gui_tree)
        root = x_tree.getroot()
        tracks = root.find("tracks").findall("track")
        self.q_track(gui_root, gui_tree, tracks, "T")
        tracks = root.find("devices/audio-engine").findall("audio-bus")
        self.q_track(gui_root, gui_tree, tracks, "B")
        self.finalize_tree(gui_tree)

    @staticmethod
    def q_to_a_plugin_copy(src_plugin, dest_plugin):
        """
        Copies the settings from a Qtractor plugin to an Ardour plugin.
        :param Element src_plugin: the source Qtractor plugin
        :param Element dest_plugin: the destination Ardour plugin
        """
        print("\nBefore:", Et.tostring(dest_plugin))
        for dest_param in dest_plugin.findall(".//Controllable"):
            src_param = src_plugin.find(".//param[@name='" + dest_param.get("name") + "']")
            try:
                dest_param.set("value", src_param.text)
                port = dest_plugin.find("lv2/Port[@symbol='" + dest_param.get("symbol") + "']")
                port.set("value", dest_param.get("value"))
            except AttributeError:
                continue
        print("\nAfter: ", Et.tostring(dest_plugin))

    @staticmethod
    def a_to_q_plugin_copy(src_plugin, dest_plugin):
        """
        Copies the settings from an Ardour plugin to a Qtractor plugin.
        :param Element src_plugin: the source Ardour plugin
        :param Element dest_plugin: the destination Qtractor plugin
        """
        print("\nBefore:", Et.tostring(dest_plugin))
        for dest_param in dest_plugin.findall(".//param"):
            src_param = src_plugin.find(".//Controllable[@name='" + dest_param.get("name") + "']")
            try:
                dest_param.text = src_param.get("value")
            except AttributeError:
                continue
        print("\nAfter: ", Et.tostring(dest_plugin))

    @staticmethod
    def q_to_a_track_copy(src_track, dest_track):
        """
        Copies all the plugin settings from a Qtractor track to an Ardour track.
        :param Element src_track: the source Qtractor track
        :param Element dest_track: the destination Ardour track
        """
        count = Counter()
        for dest_plugin in dest_track.findall(".//Processor"):
            name = dest_plugin.get("name")
            index = count.inc(name)
            try:
                src_plugin = src_track.findall(".//plugin[label='" + name.replace(" ", "_") + "']")[index]
                if src_plugin:
                    MyFrame.q_to_a_plugin_copy(src_plugin, dest_plugin)
            except IndexError:
                pass

    @staticmethod
    def a_to_q_track_copy(src_track, dest_track):
        """
        Copies all the plugin settings from an Ardour track to a Qtractor track.
        :param Element src_track: the source Ardour track
        :param Element dest_track: the destination Qtractor track
        """
        count = Counter()
        for dest_plugin in dest_track.findall(".//plugin"):
            name = dest_plugin.find("label").text
            index = count.inc(name)
            try:
                src_plugin = src_track.findall(".//Processor[@name='" + name.replace("_", " ") + "']")[index]
                if src_plugin:
                    MyFrame.a_to_q_plugin_copy(src_plugin, dest_plugin)
            except IndexError:
                pass

    def get_xml_plugins(self):
        """
        Retrieves the XML elements for the currently selected plugins.
        :return: the current Qtractor plugin and the current Ardour plugin
        """
        q_track, q_tag, q_plug, a_track, a_tag, a_plug = self.get_tracks_and_plugins()
        if not q_track:
            return None, None
        if q_tag == "T":  # it's a track
            q_plugin = self.q_tree.find(".//track[@name='" + q_track + "']/plugins/plugin[label='" + q_plug + "']")
        else:  # it's a bus
            q_plugin = self.q_tree.find(".//audio-bus[@name='" + q_track + "']/output-plugins/plugin[label='"
                                        + q_plug + "']")
        a_plugin = self.a_tree.find(".//Route[@name='" + a_track + "']/Processor[@name='" + a_plug + "']")
        return q_plugin, a_plugin

    def get_xml_tracks(self):
        """
        Retrieves the XML elements for the currently selected tracks.
        :return: the current Qtractor track (or bus) and the current Ardour track
        """
        if self.q_tree is None or self.a_tree is None:
            return None, None
        q_name, q_tag, a_name, a_tag = self.get_tracks()
        a_track = self.a_tree.find(".//Route[@name='" + a_name + "']")
        if q_tag == "T":  # it's a track
            q_track = self.q_tree.find(".//track[@name='" + q_name + "']")
        else:  # it's a bus
            q_track = self.q_tree.find(".//audio-bus[@name='" + q_name + "']")
        if q_track is not None and a_track is not None:
            return q_track, a_track
        else:
            return None, None

    # <editor-fold desc="Methods to be bound to the respective button press events in the toolkit-specific classes">
    def qopen_click(self, file_types, buttons):
        """
        Opens a Qtractor project and fills its GUI tree.
        :param file_types: file type filter for the file open dialog
        :param list buttons: list of buttons to enable
        """
        file_name = self.get_file_to_open("Open Qtractor project", file_types, self.last_dir_qtractor)
        if file_name:
            self.file_qtractor = file_name
            self.last_dir_qtractor = os.path.dirname(self.file_qtractor)
            self.q_tree = Et.parse(self.file_qtractor)
            self.q_fill(self.tree_ctrl_qtractor, self.q_tree)
            self.set_label(self.label_qproject, file_name)
            self.enable_buttons(buttons)

    def aopen_click(self, file_types, buttons):
        """
        Opens an Ardour project and fills its GUI tree.
        :param file_types: file type filter for the file open dialog
        :param list buttons: list of buttons to enable
        """
        file_name = self.get_file_to_open("Open Ardour project", file_types, self.last_dir_ardour)
        if file_name:
            self.file_ardour = file_name
            self.last_dir_ardour = os.path.dirname(self.file_ardour)
            self.a_tree = Et.parse(self.file_ardour)
            self.a_fill(self.tree_ctrl_ardour, self.a_tree)
            self.set_label(self.label_aproject, file_name)
            self.enable_buttons(buttons)

    def qbackup_click(self):
        """
        Creates a backup of the Qtractor project. Connect this to the qbackup button press.
        """
        backup = self.backup_file(self.file_qtractor)
        self.set_status(backup)

    def abackup_click(self):
        """
        Creates a backup of the Ardour project. Connect this to the abackup button press.
        """
        backup = self.backup_file(self.file_ardour)
        self.set_status(backup)

    def q_to_a_click(self):
        """
        Copies a Qtractor plugin's settings to an Ardour plugin. Connect this to the q_to_a button press.
        """
        q_plugin, a_plugin = self.get_xml_plugins()
        if q_plugin and a_plugin:
            self.q_to_a_plugin_copy(q_plugin, a_plugin)

    def a_to_q_click(self):
        """
        Copies an Ardour plugin's settings to a Qtractor plugin. Connect this to the a_to_q button press.
        """
        q_plugin, a_plugin = self.get_xml_plugins()
        if q_plugin and a_plugin:
            self.a_to_q_plugin_copy(a_plugin, q_plugin)

    def q_to_a_track_click(self):
        """
        Copies a Qtractor track's plugin settings to an Ardour track. Connect this to the q_to_a_track button press.
        """
        q_track, a_track = self.get_xml_tracks()
        if a_track and q_track:
            self.q_to_a_track_copy(q_track, a_track)
            self.set_status("Track plugin settings copied from Qtractor to Ardour")
        else:
            self.show_message("Qaps", "Select tracks in both projects")

    def a_to_q_track_click(self):
        """
        Copies an Ardour track's plugin settings to a Qtractor track. Connect this to the a_to_q_track button press.
        """
        q_track, a_track = self.get_xml_tracks()
        if a_track and q_track:
            self.a_to_q_track_copy(a_track, q_track)
            self.set_status("Track plugin settings copied from Ardour to Qtractor")
        else:
            self.show_message("Qaps", "Select tracks in both projects")

    def q_to_a_all_click(self):
        """
        Copies all Qtractor plugin settings to Ardour's project. Connect this to the q_to_a_all button press.
        """
        for a_track in self.a_tree.findall(".//Route"):
            a_flags = a_track.find("PresentationInfo").get("flags")
            if ("AudioTrack" in a_flags) or ("MidiTrack" in a_flags):
                q_track = self.q_tree.find(".//track[@name='" + a_track.get("name") + "']")
            else:
                q_track = self.q_tree.find(".//audio-bus[@name='" + a_track.get("name") + "']")
            if not q_track:
                continue
            self.q_to_a_track_copy(q_track, a_track)
        self.set_status("All plugin settings copied from Qtractor to Ardour")

    def a_to_q_all_click(self):
        """
        Copies all Ardour plugin settings to Qtractor's project. Connect this to the a_to_q_all button press.
        """
        for q_track in self.q_tree.findall(".//track") + self.q_tree.findall(".//audio-bus"):
            a_track = self.a_tree.find(".//Route[@name='" + q_track.get("name") + "']")
            if not a_track:
                continue
            self.a_to_q_track_copy(a_track, q_track)
        self.set_status("All plugin settings copied from Ardour to Qtractor")

    def qsave_click(self):
        """
        Saves the Qtractor project.
        """
        self.q_tree.write(self.file_qtractor)

    def asave_click(self):
        """
        Saves the Ardour project.
        """
        self.a_tree.write(self.file_ardour)
    # </editor-fold>
