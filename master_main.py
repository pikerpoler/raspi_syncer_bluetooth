from time import sleep
import bluetooth
from gpiozero import Button

from video_controller import Video
from constants import slave_mac_adresses, communication_port, START, QUIT, VIDEO_PATH

START_PIN = 18
QUIT_PIN = 23

sockets = []

for mac_address in slave_mac_adresses:
    print(f"connecting to {mac_address}")
    try:
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((mac_address, communication_port))
        sockets.append(sock)
    except bluetooth.BluetoothError as e:
        print(f"Bluetooth error: {e}")


# Create a socket and send the message
def send_signal(message):
    for sock in sockets:
        try:
            sock.send(message)
        except bluetooth.BluetoothError as e:
            print(f"Bluetooth error: {e}")


def main():
    start_button = Button(START_PIN)
    quit_button = Button(QUIT_PIN)
    video = Video(VIDEO_PATH)

    def start():
        video.play()
        send_signal(START)

    def quit():
        video.quit()
        send_signal(QUIT)
        sleep(1)
        exit()

    start_button.when_pressed = start
    quit_button.when_pressed = quit

    while True:
        pass


if __name__ == "__main__":
    main()
