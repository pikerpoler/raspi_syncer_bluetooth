import time
from gpiozero import Button
from signal import pause

from video_controller import Video
from constants import VIDEO_PATH

START_PIN = 17


def main():
    video = Video(VIDEO_PATH)

    def start():
        video.play()

    start_input = Button(START_PIN)
    start_input.when_pressed = start

    while True:
        pause


if __name__ == "__main__":
    main()
