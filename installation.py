import subprocess
import sys


def run_command(command, description):
    """
    Run a shell command and print its description.
    Exit if the command fails.
    """
    print(f"Running: {description}")
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}. Command '{command}' failed.")
        sys.exit(1)


if __name__ == "__main__":
    # Update system package list
    run_command("sudo apt update -y", "Updating system package list")

    # Install Bluetooth dependencies
    run_command(
        "sudo apt install -y bluetooth bluez python3-bluez",
        "Installing Bluetooth dependencies",
    )

    # Install OMXPlayer
    run_command("sudo apt install -y omxplayer", "Installing OMXPlayer")

    # Install Python dependencies with pip3
    run_command(
        "sudo pip3 install --quiet --yes omxplayer-wrapper pause",
        "Installing Python dependencies (omxplayer-wrapper, pause) with pip3",
    )

    print("All dependencies have been installed successfully!")
