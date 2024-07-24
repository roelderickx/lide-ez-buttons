# lide-ez-buttons
Python script to start shell scripts triggerd by the EZ buttons on a Canon LiDE 110 scanner

# Limitations
This script is written to use the 4 front buttons on a Canon LiDE 110 scanner as an alternative to scanbuttond. It will probably work with any other LiDE scanner provided you modify the vendor and product codes in the script.

# Requirements

You need a working installation of python and pyusb.

# Usage

Start the script and push the front buttons, the will invoke the scripts in the scripts directory. As an example the scripts prvided will do the following:
- PDF: scan the whole page in 150 dpi to pdf format, the file will be saved in the lide-ez-buttons directory
- Auto-scan: scan the whole page in 150 dpi to png format, the file will be saved in the lide-ez-buttons directory
- Copy: prints a message indicating the script does nothing else
- Email: ends the `easyscan.py` script (the shell script returns a non-zero value)

