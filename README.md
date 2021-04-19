# Hello!
This is a collection of tools for working with Nikon Z5 settings files (NCSET006.BIN as saved to your memory card in slot 1 when you use "Save/load menu settings").
Developed for and tested on Nikon Z5 firmware version 01.02.


# copyconfig.py
Copies all user settings in a config file from one of the U modes (U1/U2/U3) to the M/A/S/P/Auto modes. This also invokes fixcrc.py on the file to update its CRC.

Example command:

python copyconfig.py G:\NCSET006.BIN 1

This command would copy the settings from U1 to M/A/S/P/Auto. Change the 1 to 2 or 3 to use U2 or U3 instead, respectively.


# fixcrc.py
Recomputes and replaces the CRC code and the end of a config file. If the file contents were not changed, the CRC code will not change. If you change file contents, you must fix the CRC or the camera will not allow you to load the file.

Example command:

python fixcrc.py G:\NCSET006.BIN

This command would change the CRC code at the end of NCSET006.BIN to match its contents.


# settings_file_layout.txt
This file has information about the settings file format.


# diff.py
Computes and displays the differences between two config files.

Example command:

python diff.py G:\NCSET006.BIN G:\NCSET006_backup.BIN

This command would find all of the differences between the two input files and print them to the terminal.


# runtests.py
This file just runs some tests on the code. Helps during development. You don't need to use it.

Example command:

python runtests.py


# tests directory
Contains unit test resources.
