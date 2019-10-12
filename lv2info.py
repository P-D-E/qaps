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
    from commands import getoutput  # Python 2.X
except ImportError:
    from subprocess import getoutput  # Python 3.X
import os
import tempfile
import xml.etree.ElementTree as Et
from enum import Enum


def parse_lv2_info(file_name):
    states = Enum("States", "URN_SEARCH PORT_DATA_SEARCH PORT_DATA NAME_SEARCH NAME_GET")
    plugin = {"urn": "", "name": "", "names": [], "audio_in": 0, "audio_out": 0,
              "midi_in": 0, "midi_out": 0, "ports": []}
    port = {}
    names = ""
    try:
        state = states.URN_SEARCH
        with open(file_name, 'r') as f:
            for line in f:
                if state == states.URN_SEARCH:
                    if line.strip().startswith("<"):
                        plugin["urn"] = line.strip()[1:-1]
                        state = states.PORT_DATA_SEARCH
                elif state == states.PORT_DATA_SEARCH:
                    if line.strip().startswith("lv2:port ["):
                        state = states.PORT_DATA
                elif state == states.PORT_DATA:
                    if "lv2:index" in line:
                        port["index"] = " ".join(line.split(" ")[1:-1])
                    elif "lv2:name" in line:
                        port["name"] = " ".join(line.split('"')[1:-1])
                    elif "lv2:symbol" in line:
                        port["symbol"] = " ".join(line.split('"')[1:-1])
                    elif line.startswith("\t] , ["):  # this will skip nested lists as they have more leading tabs
                        plugin["ports"].append(port)
                        port = {}
                    elif "AudioPort" in line:
                        next_line = f.readline()
                        if "lv2:InputPort" in next_line:
                            plugin["audio_in"] += 1
                        elif "lv2:OutputPort" in next_line:
                            plugin["audio_out"] += 1
                    elif "AtomPort" in line:
                        next_line = f.readline()
                        if "lv2:InputPort" in next_line:
                            plugin["midi_in"] += 1
                        elif "lv2:OutputPort" in next_line:
                            plugin["midi_out"] += 1
                    elif line.startswith("\t] ;"):
                        plugin["ports"].append(port)
                        state = states.NAME_SEARCH
                elif state == states.NAME_SEARCH:
                    if line.strip().startswith("doap:name"):
                        if line.strip().endswith(";"):
                            plugin["name"] = line.split('"')[1]
                            break
                        else:
                            names = line.strip()
                            state = states.NAME_GET
                elif state == states.NAME_GET:
                    names += line.strip()
                    if line.strip().endswith(";"):
                        names_list = names.split(" ,")
                        for name in names_list:
                            plugin["names"].append(name.split('"')[1])
                        break
        print(plugin)
        return plugin
    except Exception as ex:
        print(str(ex))
        return None


def get_lv2_info(plugin_urn):
    try:
        tmp_file = tempfile.NamedTemporaryFile(delete=False)
        print(tmp_file.name)
        getoutput("lv2info -p " + tmp_file.name + " " + plugin_urn)
        return tmp_file.name
    except IOError:
        return None


def create_lv2_qtractor_plugin(plugin_urn):
    info_file_name = get_lv2_info(plugin_urn)
    if not info_file_name:
        return None
    plugin_info = parse_lv2_info(info_file_name)
    os.remove(info_file_name)
    if plugin_info["names"] and not plugin_info["name"]:
        plugin_info["name"] = "_".join(plugin_info["names"])
    plugin_tree = Et.parse('Qtractor-lv2-template.txt')
    plugin = plugin_tree.getroot()
    plugin.find("filename").text = plugin_info["urn"]
    plugin.find("label").text = plugin_info["name"].replace(" ", "_")
    params = plugin.find("params")
    for port in plugin_info["ports"]:
        param = Et.SubElement(params, "param", attrib={"index": port.get("index"), "name": port.get("name")})
        param.tail = "\n"
    print(Et.tostring(plugin))
    return plugin


def create_lv2_ardour_plugin(plugin_urn):
    info_file_name = get_lv2_info(plugin_urn)
    if not info_file_name:
        return None
    plugin_info = parse_lv2_info(info_file_name)
    os.remove(info_file_name)
    if plugin_info["names"] and not plugin_info["name"]:
        plugin_info["name"] = " - ".join(plugin_info["names"])
    plugin_tree = Et.parse('Ardour-lv2-template.txt')
    plugin = plugin_tree.getroot()
    plugin.set("unique-id", plugin_info["urn"])
    plugin.set("name", plugin_info["name"])
    params = plugin.find("lv2")
    for port in plugin_info["ports"]:
        if params:
            param = Et.SubElement(params, "Port", attrib={"symbol": port.get("symbol"), "value": ""})
            param.tail = "\n"
        param = Et.SubElement(plugin, "Controllable", attrib={"name": port.get("name"), "parameter": port.get("index"),
                                                              "symbol": port.get("symbol"), "value": ""})
        param.tail = "\n"
    print(Et.tostring(plugin))
    return plugin
