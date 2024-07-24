#!/bin/bash

echo "PDF was pushed, scanning full page in 150 dpi to pdf format"

scanimage --format pdf --resolution 150 --mode color --output scan_$(date +"%Y%m%d_%H%M%S").pdf
