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

# Install Python dependencies with pip3
echo "Installing Python dependencies with pip3..."
sudo pip3 install --quiet omxplayer-wrapper pause

echo "All dependencies have been installed successfully!"
