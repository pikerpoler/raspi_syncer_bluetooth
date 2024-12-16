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


def connect_to_server():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind(("", communication_port))
    server_sock.listen(communication_port)
    print("Waiting for connection...")

    client_sock, client_info = server_sock.accept()
    print(f"Connection accepted from {client_info}")
    server_sock.close()
    return client_sock


# Start listening for incoming connections
def receive_signal(client_sock):
    try:
        data = client_sock.recv(1024).decode("utf-8")
        return data

    except bluetooth.BluetoothError as e:
        print(f"Bluetooth error: {e}")
    except KeyboardInterrupt:
        print("Keyboard interrupt received. Exiting... (is this really necessary?)")
        exit()


def main():
    make_device_discoverable()
    client_sock = connect_to_server()

    video = Video(VIDEO_PATH)
    while True:
        signal = receive_signal(client_sock)
        if signal == START:
            video.play()
        elif signal == QUIT:
            print("Received QUIT signal. Exiting...")
            video.quit()
            client_sock.close()
            break


if __name__ == "__main__":
    main()
