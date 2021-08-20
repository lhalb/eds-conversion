echo off
pyrcc5 .\resources.qrc -o .\resources_rc.py
pyuic5 -x .\edsgui.ui -o edsgui.py
pyuic5 -x .\dialog.ui -o .\dialog.py