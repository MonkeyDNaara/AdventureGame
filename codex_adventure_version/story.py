import sys
import time


DEFAULT_TYPE_DELAY = 0.05
DEFAULT_PARAGRAPH_PAUSE = 0.8


def type_text(text, delay=DEFAULT_TYPE_DELAY, paragraph_pause=DEFAULT_PARAGRAPH_PAUSE):
    paragraphs = [paragraph.strip() for paragraph in text.strip().split("\n\n") if paragraph.strip()]

    for index, paragraph in enumerate(paragraphs):
        for char in paragraph:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

        if index < len(paragraphs) - 1:
            time.sleep(paragraph_pause)
            print()


intro_text = """
You wake up on a cold stone floor.
Your eyes are open, but the dark gives you nothing back.

Somewhere ahead, a small flame coughs against the stone.
It is the only thing in this place that feels alive.

Your body understands before your memory does:
move toward the light.
"""


room_texts = {
    ("level_1", 18, 1): """
Your hand touches a wall. Another wall answers on the other side.
The only warmth comes from the corridor above you.
""",
    ("level_1", 17, 1): """
A torch waits in an iron ring.
The flame bends toward you as if it has been waiting.
""",
    ("level_1", 13, 3): """
The air changes here. Shadows gather, break apart, and gather again.
This room is dangerous, but it can make you stronger.
""",
    ("level_1", 15, 7): """
Old scratches cover the floor.
Something has crossed this room many times, and it may cross it again.
""",
    ("level_1", 17, 13): """
The dark is restless here.
If you need more experience before the guardian, this is where you can earn it.
""",
    ("level_1", 18, 10): """
The Maze Guardian falls. Behind it, the stone opens like a tired eye.
You have found the way out.
""",
}


def get_room_text(level_name, y, x):
    return room_texts.get((level_name, y, x), "")


def show_intro(delay=DEFAULT_TYPE_DELAY):
    type_text(intro_text, delay)
