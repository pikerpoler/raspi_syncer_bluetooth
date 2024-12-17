echo "Installing dependancies..."
/bin/bash  /home/pi/raspi_syncer_bluetooth/script/dependency_installation.sh

# Set lunch_master.sh to run at startup using crontab
echo "Configuring lunch_master.sh to run at startup..."
(crontab -l 2>/dev/null; echo "@reboot /bin/bash /home/pi/raspi_syncer_bluetooth/script/lunch_master.sh") | crontab -