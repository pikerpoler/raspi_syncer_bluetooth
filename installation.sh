#!/bin/bash

# Update system package list
echo "Updating system package list..."
sudo apt update -y

# Install Bluetooth dependencies
echo "Installing Bluetooth dependencies..."
sudo apt install -y bluetooth bluez python3-bluez

# Install DBus dependencies
echo "Installing DBus dependencies..."
sudo apt-get update -y && sudo apt-get install -y libdbus-1{,-dev}

# Install Python dependencies with pip
echo "Installing Python dependencies with pip..."
pip install --quiet --yes omxplayer-wrapper
sudo pip3 install --quiet --yes pause

echo "All dependencies have been installed successfully!"
