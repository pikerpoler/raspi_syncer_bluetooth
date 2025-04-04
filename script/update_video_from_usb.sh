# #!/bin/bash

# # Extract VIDEO_PATH from constants.py
# VIDEO_PATH=$(python3 -c "import constants; print(constants.VIDEO_PATH)")
# echo $VIDEO_PATH
# VIDEO_NAME=$(basename "$VIDEO_PATH")
# DEST_FILE="$VIDEO_PATH"

# # Wait for USB to be detected (loop for max 30 seconds)
# USB_MOUNT=""
# for i in {1..30}; do
#     echo $i
#     USB_MOUNT=$(lsblk -o MOUNTPOINT -nr | grep '/media/pi/' | head -n 1)
#     if [ -n "$USB_MOUNT" ]; then
#         break
#     fi
#     sleep 1
# done

# # If USB was detected
# if [ -n "$USB_MOUNT" ]; then
#     echo "USB detected at $USB_MOUNT"

#     # Check if video exists on USB
#     SOURCE_FILE="$USB_MOUNT/pi-videos/$VIDEO_NAME"
#     if [ -f "$SOURCE_FILE" ]; then
#         echo "Updating video..."
#         mv "$SOURCE_FILE" "$DEST_FILE"
#         echo "Video updated successfully."
#     else
#         echo "Video not found on USB."
#     fi
# else
#     echo "No USB drive detected."
# fi


#!/bin/bash

# Extract VIDEO_PATH from constants.py
VIDEO_PATH=$(python3 -c "import constants; print(constants.VIDEO_PATH)")
VIDEO_NAME=$(basename "$VIDEO_PATH")
DEST_FILE="$VIDEO_PATH"

# Function to find and mount the USB
find_usb() {
    # Get the first partition of the USB (e.g., sda1)
    USB_PARTITION=$(lsblk -rpo "NAME,MOUNTPOINT" | awk '$2 == "" && $1 ~ /sda[0-9]/ {print $1; exit}')
    
    if [ -n "$USB_PARTITION" ]; then
        echo "USB detected at $USB_PARTITION"

        # Create a mount point
        MOUNT_POINT="/mnt/usb"
        sudo mkdir -p "$MOUNT_POINT"

        # Mount the USB
        sudo mount "$USB_PARTITION" "$MOUNT_POINT"
        echo "$MOUNT_POINT"
    else
        echo ""
    fi
}

# Try finding a mounted USB or manually mount it
USB_MOUNT=$(lsblk -o MOUNTPOINT -nr | grep '/media/pi/' | head -n 1)
if [ -z "$USB_MOUNT" ]; then
    USB_MOUNT=$(find_usb)
fi

if [ -n "$USB_MOUNT" ]; then
    echo "USB mounted at $USB_MOUNT"

    # Check if video exists on USB
    SOURCE_FILE="$USB_MOUNT/pi-videos/$VIDEO_NAME"
    if [ -f "$SOURCE_FILE" ]; then
        echo "Updating video..."
        mv "$SOURCE_FILE" "$DEST_FILE"
        echo "Video updated successfully."
    else
        echo "Video not found on USB."
    fi

    # Unmount USB after use
    sudo umount "$USB_MOUNT"
else
    echo "No USB drive detected."
fi
