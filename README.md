# Qaps
Qaps (pron. "caps") is a tool written in Python that lets you exchange plugin settings between Qtractor and Ardour projects.
A few times I started a project in one of the DAWs and then decided to work on the other one, and it happened both ways; recreating the tracks and adding the plugins was little work compared to setting all the plugin parameters one by one, hence Qaps was born (initially as a wx-only, 2-file tool).


## Usage and general information
Run qaps.py without arguments to let it pick one of the available GUI toolkits on your system, or specify one of the command line options -q -w -t to explicitly ask for the PySide/Qt5, wxWidgets, or TkInter GUI respectively.

Open the Qtractor and Ardour projects in the respective panes, create backups for safety measure (more on that later), then you can:

- select matching plugins in any two tracks and copy the settings from one to another with the buttons under the "Plugin" label

- select any two tracks and copy the plugin settings from one to another with the buttons under the "Track" label

- copy the plugin settings from one project to another with the buttons under the "All" label

Once you're done, save the modified project; it will be overwritten without asking, and that's the main good reason for creating backups first.

Plugins are matched by URN (e.g. http://calf.sourceforge.net/plugins/Equalizer8Band), you won't be able to copy settings from, say, a Calf Equalizer 8 Band to a 12 band one.

When copying entire tracks, the missing plugins in the destination track will be created (see Requirements below); Qaps also deals with multiple copies of the same plugin (e.g. EQ both before and after compression) in the same order.

When copying entire projects, tracks and buses are matched by name, regardless of their position.

The other good reason for creating backups is the floating point precision difference for the parameters: a valued saved by Ardour as 0.7070000171661377 corresponds to a 0.707 in Qtractor, but Qaps copies them as they are without making adjustments; although I've had no issues so far with modified projects having the wrong precision, you're better safe than sorry, hence create your backups.

Speaking of backups, no file name is asked; the backup is automatically created in the same location as qaps-<timestamp>-<original file name>, e.g. qaps-2016-07-13T16-32-04-HighFlight.qtr
Feel free to modify it to your needs, if you prefer being able to choose a different file name and/or folder.


## Requirements
The lv2info program is needed for plugin creation.


## Known issues
Qaps has been developed for Ardour 5.X; 4.X projects have a different structure, so they won't be supported unless someone still uses them, to keep the code short.

Qtractor MIDI buses are ignored, as I've never needed plugins on them in either DAW.

Barebone GUIs (feel free to say ugly :) ) because I just needed the tool to work.

Lack of i18n support, also because I just needed the tool to work.

Fixed backup naming scheme because (you guessed it! :) ) I just needed the tool to work.

Lack of a test suite, I know, I know... O:-)


## Assorted notes
One intent is to keep the widest compatibility and the lowest requirements and dependencies possible.
Using Abstract Base Classes would help ensuring that all the methods to override are overridden, but given the different syntax for Python 2.X and 3.X, it's been left apart, leaving qaps-common.py's comments and docstrings to act as a reference.

PySimpleGUI looks like a great tool to avoid creating the various GUI parts as I did but, besides this having been a fun experiment, I preferred not to have an extra requirement for such a simple project.

Most of the respective naming conventions of the toolkits have been ignored; having the same widget and function names across the GUIs made it easier to create and maintain the business models.

The GUI source files are included in the guis subfolder, but the Python modules built on them have been modified later; that's especially the case with the Tk GUI, where I manually set the mix of absolute/relative widget positions and sizes to my liking, and did some other minor changes. The qapstk_support.py module was also renamed to qaps_tk.py for naming coherence across GUIs.


## Tools of the trade
- PAGE 4.25.1 - for the TkInter GUI
- wxGlade 0.8.3 - for the wxWidgets GUI
- Qt 5 Designer 5.11.3 - for the PySide/Qt5 GUI
- pyuic5 from PyQt5 5.12.3 - for the Python module compilation
- PyCharm Community Edition 2019.2 - for development
- Xml Copy Editor 1.2.1.3 - for XML study on the Qtractor and Ardour project files



## Acknowledgements
- Qtractor - https://qtractor.sourceforge.io/
- Ardour - https://ardour.org
- PAGE - http://page.sourceforge.net/
- wxGlade - http://wxglade.sourceforge.net
- Qt 5 Designer - https://www.qt.io/developers/
- pyuic5 from PyQt5 - https://riverbankcomputing.com/software/pyqt/intro
- PyCharm - https://www.jetbrains.com/pycharm/
- Xml Copy Editor - http://xml-copy-editor.sourceforge.net
