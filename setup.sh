#!/usr/bin/env bash

#########################################################################
#  Project           		:   CEDIT-A PYTHON BASED TEXT EDITOR
#  Name of the file	        :   setup.sh
#  Brief Description of file   :   File for installing CEdit
#  Name                        :   KAPIL SHYAM.M 
#  Email ID                    :   cedit.ceo@gmail.com
#                                                                       #
#                                                                       #
#########################################################################

echo "\n\t\tCEdit-A Python based Text Editor\t"

echo '\n\t\tInstalling Necessary Files\t'

sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-tk
sudo pip3 install tkterminal
sudo apt-get install Pyinstaller

echo '\n\t\t Exporting to PATH\t '
export PATH=$PATH:~/cedit/dist/

echo '\n\n\t\t\tCompiling the Main Program....\t\n\n'

pyinstaller --onefile cedit.py

SOURCE="icons"
DESTINATION="dist/icons/"

cp -r "$SOURCE"* "$DESTINATION"

SOURCE="cemodules"
DESTINATION="dist/cemodules/"

cp -r "$SOURCE"* "$DESTINATION"

echo $"[Desktop Entry]
Encoding=UTF-8
Version=1.0.0
Name=CEdit
Comment=A Python based Text Editor
GenericName=Text Editor
Exec=/usr/share/cedit/dist/cedit
Path=/usr/share/cedit/dist/
Terminal=false
Icon=/usr/share/cedit/icons/CEdit_Icon.png
Type=Application
Categories=Utility;TextEditor;Development;IDE;" >cedit.desktop

sudo mv cedit.desktop /usr/share/applications/

sudo cp -r $HOME/cedit /usr/share/

echo '\n\n\t\tOpening The Text Editor...\t\n\n'

cd dist
./cedit

echo '\t\tHurray... Text Editor is in USE.....\t'
