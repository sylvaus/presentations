import sys
import time
from collections import OrderedDict

from text_reader.reader_class import Reader
from text_reader.reader_func import read_file
from text_reader.speaker_class import Speaker
from text_reader.speaker_func import create_speaker, get_voices


def pause(text, speaker):
    sleep_s = int(text.replace("pause:", ""))
    speaker.say("I will make a pause of {} seconds".format(sleep_s))
    time.sleep(sleep_s)


def main_class():
    if len(sys.argv) < 2:
        print("Not enough argument: one is needed")
        return

    speaker = Speaker()
    voice = speaker.voices[0]
    speaker.set_voice(voice)
    reader = Reader(speaker)
    reader.add_special_action("pause:", pause)
    reader.read_file(sys.argv[1])


def main_func():
    if len(sys.argv) < 2:
        print("Not enough argument: one is needed")
        return

    speaker = create_speaker()
    voices = get_voices(speaker)
    speaker.set_voice(voices[0])
    special_actions = OrderedDict([("pause:", pause)])
    read_file(sys.argv[0], speaker, special_actions)


