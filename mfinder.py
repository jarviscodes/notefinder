from itertools import cycle
from collections import deque

class Neck(object):
    def __init__(self):
        self.high_e_string = ""
        self.b_string = ""
        self.g_string = ""
        self.d_string = ""
        self.a_string = ""
        self.low_e_string = ""

    def load_string(self, guitar_string):
        if guitar_string.startswith("e"):
            self.high_e_string = guitar_string
        if guitar_string.startswith("B"):
            self.b_string = guitar_string
        if guitar_string.startswith("G"):
            self.g_string = guitar_string
        if guitar_string.startswith("D"):
            self.d_string = guitar_string
        if guitar_string.startswith("A"):
            self.a_string = guitar_string
        if guitar_string.startswith("E"):
            self.low_e_string = guitar_string

    def translate_neck(self):
        self.high_e_string = GuitarString.translate_tab_to_notes(self.high_e_string)
        self.b_string = GuitarString.translate_tab_to_notes(self.b_string)
        self.g_string = GuitarString.translate_tab_to_notes(self.g_string)
        self.d_string = GuitarString.translate_tab_to_notes(self.d_string)
        self.a_string = GuitarString.translate_tab_to_notes(self.a_string)
        self.low_e_string = GuitarString.translate_tab_to_notes(self.low_e_string)

    def __str__(self):
        return self.high_e_string + "\n" + self.b_string + "\n" + self.g_string + "\n" + self.d_string + "\n" + self.a_string + "\n" + self.low_e_string + "\n"

    @property
    def is_complete(self):
        if not len(self.low_e_string) > 0:
            return False
        if not len(self.a_string) > 0:
            return False
        if not len(self.d_string) > 0:
            return False
        if not len(self.g_string) > 0:
            return False
        if not len(self.b_string) > 0:
            return False
        if not len(self.high_e_string) > 0:
            return False

        return True

class GuitarString(object):
    rotation_values = {
        "E": -7,
        "A": -12,
        "D": -17,
        "G": -22,
        "B": -26,
        "e": -31
    }

    octave_count = 8
    octaves = list(range(octave_count))
    tones = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    tone_ladder = []

    for i in range(octave_count):
        for tone in tones:
            tone_ladder.append(f"{tone}{i}")


    @classmethod
    def translate_tab_to_notes(cls, tab_string):
        transformable_ladder = deque(cls.tone_ladder)
        counter = 0
        double_digit_toggle = False
        translated_string = tab_string

        # Transform Deque for correct string
        string_key = tab_string[0]
        transformable_ladder.rotate(cls.rotation_values.get(string_key))

        for character in tab_string:
            if character.isdigit():
                # peekahead
                if tab_string[counter + 1].isdigit():
                    double_digit_toggle = True
                    character = int(f"{character}{tab_string[counter + 1]}")
                    translated_string = translated_string.replace(str(character), transformable_ladder[int(character)])


                else:
                    if not double_digit_toggle:
                        translated_string = translated_string.replace(str(character), transformable_ladder[int(character)])
                    else:
                        double_digit_toggle = False
            counter += 1

        return translated_string

# load the file
with open('./tab.txt', "r") as _tab_file:
    tab_data = [guitar_string.strip() for guitar_string in _tab_file.readlines() if len(guitar_string.strip()) > 0]

all_necks = []
# Extract a full neck from the file:
# Prepare a neck object
new_neck = Neck()
for line in tab_data:
    new_neck.load_string(line)
    if new_neck.is_complete:
        new_neck.translate_neck()
        all_necks.append(new_neck)
        new_neck = Neck()



for neck in all_necks:
    print(neck)
    print("\n")
