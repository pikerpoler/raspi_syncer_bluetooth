from time import sleep
from gpiozero import Button, LED

from video_controller import Video
from constants import VIDEO_PATH

START_PIN = 17
BUTTON_PIN = 18
QUIT_PIN = 23


def main():
    button = Button(BUTTON_PIN)
    start_connection = LED(START_PIN)

    video = Video(VIDEO_PATH)

    def start():
        start_connection.on()
        video.play()
        sleep(0.1)
        start_connection.off()

    button.when_pressed = start

    print("starting main loop")
    while True:
        pass


if __name__ == "__main__":
    main()
