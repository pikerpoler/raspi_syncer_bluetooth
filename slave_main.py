import bluetooth

from video_controller import Video
from constants import communication_port, VIDEO_PATH, START, RESET, QUIT


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
    video = Video(VIDEO_PATH)
    while True:
        signal = receive_signal()
        if signal == START:
            print("Start signal received!")
            video.play()
        elif signal == RESET:
            video.reset()
        elif signal == QUIT:
            video.quit()
            break
