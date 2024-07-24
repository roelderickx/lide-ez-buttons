#!/usr/bin/env python

import usb.core
import usb.util
import subprocess

EZ_BUTTON_PDF = 8
EZ_BUTTON_AUTO_SCAN = 1
EZ_BUTTON_COPY = 2
EZ_BUTTON_EMAIL = 4

# find the Canon LiDE 110 scanner
device = usb.core.find(idVendor=0x04a9, idProduct=0x1909)
# was it found?
if device is None:
    raise ValueError('Device not connected')

# set the active configuration. With no arguments, the first
# configuration will be the active one
device.set_configuration()

# get an endpoint instance
configuration = device.get_active_configuration()
interface = configuration[(0,0)]

endpoint = usb.util.find_descriptor(
    interface,
    # match the first interrupt IN endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_IN and \
        usb.util.endpoint_type(e.bmAttributes) == usb.util.ENDPOINT_TYPE_INTR)

while True:
    try:
        # read buttons, timeout 5 seconds
        b = device.read(endpoint.bEndpointAddress, 1, 5000)

        usb.util.release_interface(device, interface)

        retval = 0
        if b[0] == EZ_BUTTON_PDF:
            retval = subprocess.call('scripts/ez_button_pdf.sh', shell=True)
        elif b[0] == EZ_BUTTON_AUTO_SCAN:
            retval = subprocess.call('scripts/ez_button_auto_scan.sh', shell=True)
        elif b[0] == EZ_BUTTON_COPY:
            retval = subprocess.call('scripts/ez_button_copy.sh', shell=True)
        elif b[0] == EZ_BUTTON_EMAIL:
            retval = subprocess.call('scripts/ez_button_email.sh', shell=True)

        usb.util.claim_interface(device, interface)

        if retval != 0:
            break
    except usb.core.USBTimeoutError:
        pass
