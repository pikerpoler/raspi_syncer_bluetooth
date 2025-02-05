#!/bin/bash

# Prompt user for video name
read -p "Enter video name (including extension, e.g., video.mp4): " video_name

# Update constants.py
sed -i "s|VIDEO_PATH = .*|VIDEO_PATH = \"/home/pi/Videos/$video_name\"|" /home/pi/raspi_syncer_bluetooth/constants.py