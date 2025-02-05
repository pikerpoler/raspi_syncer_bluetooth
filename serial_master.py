from time import sleep
from gpiozero import Button, LED

from video_controller import Video
from constants import VIDEO_PATH

START_PIN = 16
BUTTON_PIN = 18
QUIT_PIN = 23


def main():
    button = Button(BUTTON_PIN)
    start_connection = LED(START_PIN)

    video = Video(VIDEO_PATH)

    def start():
        start_connection.on()
        sleep(0.01)
        start_connection.off()
        video.play()

    button.when_pressed = start
    
    print("starting main loop")
    while True:
        pass


if __name__ == "__main__":
    main()
