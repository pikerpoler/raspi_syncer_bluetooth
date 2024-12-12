import bluetooth


from constants import slave_mac_adresses, communication_port, START, RESET, QUIT


# Create a socket and send the message
def send_signal(message):
    for mac_address in slave_mac_adresses:
        try:
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((mac_address, communication_port))
            sock.send(message)
            print(f"Sent: {message}")
            sock.close()
        except bluetooth.BluetoothError as e:
            print(f"Bluetooth error: {e}")


if __name__ == "__main__":
    signal = input("Enter 'start' or 'reset': ").strip().lower()
    if signal == "start":
        send_signal(START)
        # TODO: start the video
    elif signal == "reset":
        # TODO: reset the video
        send_signal(RESET)
    elif signal == "quit":
        # TODO: reset the video
        send_signal(QUIT)
        exit()
    else:
        print("Invalid input!")
