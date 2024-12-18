from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep

from datetime import datetime, timedelta


def parse_time(time_string):
    strings = time_string.split()
    for s in strings:
        if ":" in s:
            return [int(t) for t in s.split(":")]


class Video:

    def __init__(self, video_path):
        self.player = OMXPlayer(Path(video_path), args=["--loop"])
        self.player.set_position(0)

    def play(self):
        if self.player.is_playing():
            self.player.pause()
            self.player.set_position(0)
        else:
            self.player.play()

    def reset(self):
        self.player.set_position(0)
        self.player.pause()

    def quit(self):
        self.player.quit()
        exit()
