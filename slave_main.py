import bluetooth
import subprocess

from video_controller import Video
from constants import communication_port, VIDEO_PATH, START, QUIT


def make_device_discoverable():
    """
    Automates the process of making the Raspberry Pi discoverable via Bluetooth.
    """
    try:
        # Start bluetoothctl in subprocess
        subprocess.run(["bluetoothctl", "power", "on"], check=True)
        subprocess.run(["bluetoothctl", "discoverable", "on"], check=True)
        subprocess.run(["bluetoothctl", "pairable", "on"], check=True)
        print("Device is now discoverable and pairable.")
    except subprocess.CalledProcessError as e:
        print(f"Error enabling discoverability: {e}")


# Start listening for incoming connections
def receive_signal():
    try:
        server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        server_sock.bind(("", communication_port))
        server_sock.listen(communication_port)
        print("Waiting for connection...")

        client_sock, client_info = server_sock.accept()
        print(f"Connection accepted from {client_info}")

        data = client_sock.recv(1024).decode("utf-8")
        print(f"Received: {data}")

        client_sock.close()
        server_sock.close()

        return data
    except bluetooth.BluetoothError as e:
        print(f"Bluetooth error: {e}")


if __name__ == "__main__":
    make_device_discoverable()

    video = Video(VIDEO_PATH)
    while True:
        signal = receive_signal()
        if signal == START:
            print("Start signal received!")
            video.play()
        elif signal == QUIT:
            video.quit()
            break
