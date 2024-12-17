#!/bin/bash

# Update system package list
echo "Updating system package list..."
sudo apt update -y

# Install Bluetooth dependencies
echo "Installing Bluetooth dependencies..."
sudo apt install -y bluetooth bluez python3-bluez

# Install OMXPlayer
echo "Installing OMXPlayer..."
# sudo apt install -y omxplayer

wget http://archive.raspberrypi.org/debian/pool/main/o/omxplayer/omxplayer_20190723+gitf543a0d-1_armhf.deb
sudo dpkg -i omxplayer_20190723+gitf543a0d-1_armhf.deb
sudo apt-get -f install
rm omxplayer_20190723+gitf543a0d-1_armhf.deb

# Install Python dependencies with pip3
echo "Installing Python dependencies with pip3..."
sudo pip3 install --quiet omxplayer-wrapper pause

echo "All dependencies have been installed successfully!"
