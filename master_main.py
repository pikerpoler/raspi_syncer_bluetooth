from time import sleep
import bluetooth
from gpiozero import Button

from video_controller import Video
from utils import make_device_discoverable
from constants import SLAVE_MAC_ADDRESS, COMMUNICATION_PORT, START, QUIT, VIDEO_PATH

START_PIN = 18
QUIT_PIN = 23

sockets = []

for mac_address in SLAVE_MAC_ADDRESS:
    print(f"connecting to {mac_address}")
    while True:
        try:
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((mac_address, COMMUNICATION_PORT))
            sockets.append(sock)
        except bluetooth.BluetoothError as e:
            print(f"Bluetooth error: {e}")
        else:
            print(f"Successfully connected to {mac_address}")
            break


# Create a socket and send the message
def send_signal(message):
    for sock in sockets:
        try:
            sock.send(message)
        except bluetooth.BluetoothError as e:
            print(f"Bluetooth error: {e}")


def main():
    make_device_discoverable()
    start_button = Button(START_PIN)
    quit_button = Button(QUIT_PIN)
    video = Video(VIDEO_PATH)

    def start():
        send_signal(START)
        video.play()

    def quit_foo():
        print("sending quit signal")
        send_signal(QUIT)
        video.quit()
        sleep(1)
        print("exiting")
        exit()

    start_button.when_pressed = start
    quit_button.when_pressed = quit_foo

    while True:
        pass


if __name__ == "__main__":
    main()
