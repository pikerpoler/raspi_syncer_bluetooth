#!/bin/bash

# Update system package list
echo "Updating system package list..."
sudo apt update -y

# Install Bluetooth dependencies
echo "Installing Bluetooth dependencies..."
sudo apt install -y bluetooth bluez python3-bluez

# Install OMXPlayer
echo "Installing OMXPlayer..."
sudo apt install -y omxplayer

# sudo apt install -y gstreamer1.0-tools gstreamer1.0-plugins-base \
#     gstreamer1.0-plugins-good gstreamer1.0-plugins-bad \
#     gstreamer1.0-omx

# sudo apt-get install -y gstreamer-1.0
# sudo apt-get install libgtk-3-dev
# sudo apt-get install gir1.2-gtk-3.0
# sudo apt-get install python-gi python3-gi

# pip3 install --quiet pygobject


wget http://archive.raspberrypi.org/debian/pool/main/o/omxplayer/omxplayer_20190723+gitf543a0d-1_armhf.deb
sudo dpkg -i omxplayer_20190723+gitf543a0d-1_armhf.deb
sudo apt-get -f install
rm omxplayer_20190723+gitf543a0d-1_armhf.deb

# Install Python dependencies with pip3
echo "Installing Python dependencies with pip3..."
sudo pip3 install --quiet omxplayer-wrapper pause

echo "All dependencies have been installed successfully!"
