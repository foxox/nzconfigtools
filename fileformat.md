# Overview
When you use "Save/load menu settings" in your Nikon Z camera, the camera saves a file to the memory card in slot 1 named NCSET006.BIN
This is a binary file and is not human-readable.
The locations of settings in the file seem to be consistent between saves.
Camera modes Manual, Aperture Priority, Shutter Priority, Program, and Auto seem to share the same config. This may be different in other cameras -- in the file format, there are multiple locations with the settings for these modes duplicated.
Camera modes U1, U2, and U3 each have a separate config.

# Byte ranges:
* 0-10
    * Camera model. "NIKON Z 5" text in ANSI characters here.
* 24-28
    * Firmware version. It was 01.02 when I did this investigation.
* 356?-6983?
    * Suspect this is something like the "most recent settings assigned" because it gets updated whether you change MASPA settings or user settings.
    Seems to be ignored on load.
    Unsure exactly what this range is for or where it really starts or ends, but I do know there is an i-menu range within it at 1280-1328. Also, "DSC" shows up at 1896-1898, so that is probably the filename prefix.
* 2042-82683
    * Zeroes
* 82684-85757
    * Picture control settings, unclear what for.
* 85758-166399
    * Zeroes
* 169824-176451
    * Primary MASPA config range
    This gets loaded when you load settings in the camera.
* 176452-183079
    * Secondary MASPA config range
    This gets ignored when you load settings in the camera.
    Perhaps this is used on other camera models.
* 183080-189707
    * U1 config range
* 189708-196335
    * U2 config range
* 196336-202963
    * U3 config range
* 202964-202965
    * XMODEM CRC-16 checksum computed over bytes 0-202963

## Sub-ranges
Within each config range, these sub-ranges are known:
*  924-972
    *  The i-menu config starts at offset 924 from the beginning of a config range. Each i-menu tile is configured as one byte and the bytes are spaced 4 apart. They go left to right, top to bottom. So the top left i-menu tile is set at offset 924. The second one (to the right of the top left corner) is 924+4, etc. The i-menu tile options are listed below.
    For example, the i-menu for U2 starts at offset 189708 + offset 924 = byte 190632. The second i-menu item for U2 starts 4 bytes later at 190632+4=190636.
*  1540-?
    *  The configured file prefix (the "DSC" in "DSC_****.***" filenames) starts at 1540 from beginning of config range. Not sure what the max length is.

## i-menu tile IDs (decimal)
* 0 Active D-Lighting
* 1 AF area mode
* 2 Do not use - causes strange i-menu behavior.
* 3 Auto bracketing
* 4 Bluetooth connection
* 5 Monitor/viewfinder brightness
* 6 Color space
* 7 Choose image area
* 8 Custom controls
* 9 Shutter type
* 10 Do not use - causes strange i-menu behavior.
* 11 Exposure compensation
* 12 Exposure delay mode
* 13 Flash compensation
* 14 Do not use - causes strange i-menu behavior.
* 15 Focus Mode
* 16 Do not use - causes strange i-menu behavior.
* 17 HDR
* 18 Do not use - causes strange i-menu behavior.
* 19 High ISO NR
* 20 Do not use - causes strange i-menu behavior.
* 21 Image Quality
* 22 Image Size
* 23 Do not use - causes strange i-menu behavior.
* 24 ISO sensitivity settings
* 25 Long exposure NR
* 26 Apply settings to live view
* 27 Metering
* 28 Do not use - causes strange i-menu behavior.
* 29 Multiple Exposure
* 30 Peaking Highlights
* 31 Set Picture Control
* 32 Release Mode
* 33 Silent Photography
* 34 "Disable" This item stands out. If you assign it and load it in a Z5 camera, it shows up as the icon for "Split-screen display zoom" with text "Disable" and if you select it, the camera freezes for a few moments, then the i-menu closes and the camera un-freezes. This feature is only available on other camera models like the Z6 or Z7. However it is the only unavailable option here which has an icon. I wonder if it was a feature cut late in the development process?
* 35 Vibration Reduction??
* 36 White Balance
* 37 Do not use - causes strange i-menu behavior.
* 38 Wifi connection
* 39 View memory card info
* 40 Interval timer shooting
* 41 Time-lapse movie
* 42 Focus shift shooting
* 43 Do not use - causes strange i-menu behavior.
* 44 Do not use - causes strange i-menu behavior.
* 45 Do not use - causes strange i-menu behavior.
* 46 Do not use - causes strange i-menu behavior.
* 47 Do not use - causes strange i-menu behavior.
* 48 Do not use - causes strange i-menu behavior.
* 49 Do not use - causes strange i-menu behavior.
* 50 Do not use - causes strange i-menu behavior.
* 51 Group flash options
Seems to be the end of usable options. Higher numbers all produce strange i-menu behavior.
