import time
from time import sleep
from gpiozero import Button, LED

from video_controller import Video
from constants import VIDEO_PATH

OUTPUT_PIN = 17
INPUT_PIN = 27
BUTTON_PIN = 18
QUIT_PIN = 23


def main():
    button = Button(BUTTON_PIN)
    out_connection = LED(OUTPUT_PIN)
    in_connection = Button(INPUT_PIN)

    time_log = [time.time()]

    def start():
        start_time = time.time()
        out_connection.on()
        in_connection.wait_for_press()
        print(f"signal received at {time.time() - start_time}")
        out_connection.off()

    def receive_signal():
        out_connection.on()
        sleep(0.1)
        out_connection.off()

    button.when_pressed = start
    in_connection.when_pressed = receive_signal

    print("starting main loop")
    while True:
        pass


if __name__ == "__main__":
    main()
