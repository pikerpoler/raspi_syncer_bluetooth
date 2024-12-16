import subprocess


def make_device_discoverable():
    """
    Automates the process of making the Raspberry Pi discoverable via Bluetooth.
    """
    try:
        # Start bluetoothctl in subprocess
        subprocess.run(["bluetoothctl", "power", "on"], check=True)
        subprocess.run(["bluetoothctl", "discoverable", "on"], check=True)
        subprocess.run(["bluetoothctl", "pairable", "on"], check=True)

        subprocess.run(["bluetoothctl", "agent", "NoInputNoOutput"], check=True)
        subprocess.run(["bluetoothctl", "default-agent"], check=True)

        print("Device is now discoverable and pairable.")
    except subprocess.CalledProcessError as e:
        print(f"Error enabling discoverability: {e}")
