import bluetooth

import time

from gpiozero import Button


from utils import make_device_discoverable
from constants import communication_port, START

INPUT_PIN = 17


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


time_log = [time.time()]


def main():

    def high_signal():
        last_event = time_log[-1]
        now = time.time()
        time_log.append(now)
        print(f"Signal received: HIGH. elapsed: {now - last_event}")

    def low_signal():
        last_event = time_log[-1]
        now = time.time()
        time_log.append(now)
        print(f"Signal received: LOW. elapsed: {now -last_event}")

    make_device_discoverable()
    client_sock = connect_to_server()

    input = Button(INPUT_PIN)
    input.when_pressed = low_signal
    input.when_released = high_signal

    while True:
        signal = receive_signal(client_sock)
        if signal == START:
            last_event = time_log[-1]
            now = time.time()
            time_log.append(now)
            print(f"Signal received: START. elapsed: {now - last_event}")


if __name__ == "__main__":
    main()
