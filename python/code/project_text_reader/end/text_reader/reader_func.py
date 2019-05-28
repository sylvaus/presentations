import pyttsx3

from text_reader.speaker_func import say


def read_file(filepath: str, speaker: pyttsx3.Engine, special_actions: dict):
    with open(filepath, "r") as text_to_read:
        for line in text_to_read:
            _handle_line(line, speaker, special_actions)


def _handle_line(line, speaker, special_actions):
    special = False
    for key, func in special_actions.items():
        if key in line:
            func(line, speaker)
            special = True
            break

    if not special:
        say(speaker, line)
