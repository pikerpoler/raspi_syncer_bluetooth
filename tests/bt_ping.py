import bluetooth
import time
import threading

from constants import COMMUNICATION_PORT, SLAVE_MAC_ADDRESS
from utils import make_device_discoverable


def connect_to_server():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind(("", COMMUNICATION_PORT))
    server_sock.listen(COMMUNICATION_PORT)
    print("Waiting for connection...")

    client_sock, client_info = server_sock.accept()
    print(f"Connection accepted from {client_info}")
    server_sock.close()
    return client_sock


def connect_to_client():
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((SLAVE_MAC_ADDRESS[0], COMMUNICATION_PORT))
    return sock


def send_signal(message, sock):
    try:
        sock.send(message)
    except bluetooth.BluetoothError as e:
        print(f"Bluetooth error: {e}")


def receive_signal(sock):
    try:
        data = sock.recv(1024).decode("utf-8")
        return data

    except bluetooth.BluetoothError as e:
        print(f"Bluetooth error: {e}")
    except KeyboardInterrupt:
        print("Keyboard interrupt received. Exiting... (is this really necessary?)")
        exit()


def main():
    make_device_discoverable()

    client_sock = None
    try:
        client_sock = connect_to_client()
    except bluetooth.BluetoothError as e:
        print(f"Bluetooth error: {e}")

    server_sock = connect_to_server()

    if client_sock is None:
        client_sock = connect_to_client()

    def worker_function():
        while True:
            message = receive_signal(server_sock)
            send_signal(message, client_sock)

    # Create a thread and mark it as daemon
    worker_thread = threading.Thread(target=worker_function)
    worker_thread.daemon = (
        True  # This ensures the thread terminates with the main process
    )
    worker_thread.start()

    while True:
        user_input = input("Enter a message: ")
        start = time.time()
        send_signal(user_input, client_sock)
        message = receive_signal(server_sock)
        if message == user_input:
            end = time.time()
            print(f"Message sent: {user_input}. Time elapsed: {end - start}")


if __name__ == "__main__":
    main()
