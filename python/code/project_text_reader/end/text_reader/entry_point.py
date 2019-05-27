import sys
import time

from text_reader.reader import Reader
from text_reader.speaker import Speaker


def pause(text, speaker):
    sleep_s = int(text.replace("pause:", ""))
    speaker.say("I will make a pause of {} seconds".format(sleep_s))
    time.sleep(sleep_s)


def main():
    if len(sys.argv) < 2:
        print("Not enough argument: one is needed")
        return

    speaker = Speaker()
    voice = speaker.voices[0]
    speaker.set_voice(voice)
    reader = Reader(speaker)
    reader.add_special_action("pause:", pause)
    reader.read(sys.argv[1])


if __name__ == '__main__':
    main()
