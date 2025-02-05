#!/bin/bash

cd ~/raspi_syncer_bluetooth

/bin/bash  /home/pi/raspi_syncer_bluetooth/script/update_video_from_usb.sh

sudo python3 slave_main.py