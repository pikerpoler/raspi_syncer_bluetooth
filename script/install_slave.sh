echo "Installing dependancies..."
/bin/bash  /home/pi/raspi_syncer_bluetooth/script/dependency_installation.sh

# Add lunch_master.sh to .bashrc for startup
BASHRC_LINE="/bin/bash /home/pi/raspi_syncer_bluetooth/script/lunch_slave.sh"
if ! grep -Fxq "$BASHRC_LINE" ~/.bashrc; then
    echo "Adding lunch_master.sh to .bashrc..."
    echo "$BASHRC_LINE" >> ~/.bashrc
else
    echo "lunch_master.sh is already in .bashrc."
fi