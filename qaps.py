#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# This is the main launcher module. It can be invoked with -q -w or -t arguments to explicitly request the
# PySide2/Qt5, the WxWindows, or the Tkinter GUI; if the requested GUI is not available or no choice has been made,
# the first available one will be used.

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

import sys


def got_qt():
    """
    Retrieves the availability of the PySide2 or Qt5 GUI.
    :return bool: True if available, False if not
    """
    try:
        from sideqt import QtCore, QtGui, QtWidgets
    except ImportError:
        return False
    return True


def got_wx():
    """
    Retrieves the availability of the WxWindows GUI.
    :return bool: True if available, False if not
    """
    try:
        import wx
    except ImportError:
        return False
    return True


def got_tk():
    """
    Retrieves the availability of the Tkinter GUI.
    :return bool: True if available, False if not
    """
    try:
        # Python 2.X
        import Tkinter as tk
        import ttk
    except ImportError:
        try:
            # Python 3.X
            import tkinter as tk
            import tkinter.ttk as ttk
        except ImportError:
            return False
    return True


if __name__ == "__main__":
    qt_ok = got_qt()
    qt_wx = got_wx()
    qt_tk = got_tk()

    if "-q" in sys.argv and qt_ok:
        from qaps_qt5 import run
    elif "-w" in sys.argv and qt_wx:
        from qaps_wx import run
    elif "-t" in sys.argv and qt_tk:
        from qaps_tk import run
    else:
        if qt_ok:
            from qaps_qt5 import run
        elif qt_wx:
            from qaps_wx import run
        elif qt_tk:
            from qaps_tk import run
    run()
