#!/bin/bash

echo "Auto scan was pushed, scanning full page in 150 dpi to png format"

scanimage --format png --resolution 150 --mode color --output scan_$(date +"%Y%m%d_%H%M%S").png
