import bluetooth
from gpiozero import Button

from constants import slave_mac_adresses, communication_port, START, QUIT

START_PIN = 18
QUIT_PIN = 23


# Create a socket and send the message
def send_signal(message):
    for mac_address in slave_mac_adresses:
        print(f"Sending signal to {mac_address}")
        try:
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((mac_address, communication_port))
            sock.send(message)
            print(f"Sent: {message}")
            sock.close()
        except bluetooth.BluetoothError as e:
            print(f"Bluetooth error: {e}")


def start():
    print("start foo")
    send_signal(START)


def quit():
    print("quit foo")
    send_signal(QUIT)


if __name__ == "__main__":
    start_button = Button(START_PIN)
    quit_button = Button(QUIT_PIN)

    start_button.when_pressed = start
    quit_button.when_pressed = quit

    while True:
        pass
