import bluetooth

from video_controller import Video
from utils import make_device_discoverable
from constants import COMMUNICATION_PORT, VIDEO_PATH, START, QUIT


def connect_to_server():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind(("", COMMUNICATION_PORT))
    server_sock.listen(COMMUNICATION_PORT)
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
