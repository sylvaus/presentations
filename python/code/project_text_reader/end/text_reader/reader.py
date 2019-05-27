from collections import OrderedDict
from typing import Callable

from text_reader.speaker import Speaker


class Reader:
    def __init__(self, speaker: Speaker):
        self._speaker = speaker
        self._special_actions = OrderedDict()

    def add_special_action(self, key: str, func: Callable[[str, Speaker], None]):
        self._special_actions[key] = func

    def read(self, filepath: str):
        with open(filepath, "r") as text_to_read:
            for line in text_to_read:
                self._handle_line(line)

    def _handle_line(self, line):
        special = False
        for key, func in self._special_actions.items():
            if key in line:
                func(line, self._speaker)
                special = True
                break

        if not special:
            self._speaker.say(line)
