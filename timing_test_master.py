from time import sleep
import bluetooth
from gpiozero import Button, LED

from constants import slave_mac_adresses, communication_port, START

CONNECTION_PIN = 17
BUTTON_PIN = 18

sockets = []
for mac_address in slave_mac_adresses:
    print(f"connecting to {mac_address}")
    try:
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((mac_address, communication_port))
        sockets.append(sock)
    except bluetooth.BluetoothError as e:
        print(f"Bluetooth error: {e}")


def send_signal(message):
    for sock in sockets:
        try:
            sock.send(message)
        except bluetooth.BluetoothError as e:
            print(f"Bluetooth error: {e}")


def main():
    button = Button(BUTTON_PIN)
    out_connection = LED(CONNECTION_PIN)

    def start():
        print("starting")
        out_connection.on()
        send_signal(START)
        sleep(1)
        out_connection.off()

    button.when_pressed = start

    print("starting main loop")
    while True:
        pass


if __name__ == "__main__":
    main()
