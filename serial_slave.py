from time import sleep
from gpiozero import Button


from video_controller import Video
from constants import VIDEO_PATH

START_PIN = 27


def main():
    sleep(10)
    video = Video(VIDEO_PATH)

    def start():
        video.play()

    start_input = Button(START_PIN)
    start_input.when_pressed = start

    while True:
        pass


if __name__ == "__main__":
    main()
