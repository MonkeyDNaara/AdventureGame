import sys
import time


DEFAULT_TYPE_DELAY = 0.04


def type_text(text, delay=DEFAULT_TYPE_DELAY, wait_func=None):
    paragraphs = [part.strip() for part in text.strip().split("\n\n") if part.strip()]

    for index in range(len(paragraphs)):
        paragraph = paragraphs[index]

        for letter in paragraph:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)

        print()

        if index < len(paragraphs) - 1 and wait_func is not None:
            wait_func("\nPress Space to continue...")
            print()


intro_text = """
You wake up on a cold stone floor.
You try to grasp where you are, but there's.. nothing.. you can't remember anything.

The air is wet and water is dropping from the ceiling.
You can't see it, but you hear the drops.

It's completely silent around you. You can hear your own breath.
Goosebumps spread all over your body.

Your eyes need a moment to adjust to the darkness.
Wait.. In the distance, a faint orange light flickers.
"""


room_texts = {
    ("main", 18, 1): """
Your hand touches a wall. Another wall answers on the other side.
""",
    ("hidden", 1, 1): """
You enter a hidden room. The walls are tighter here.
""",
}


def get_room_text(map_name, row, col):
    return room_texts.get((map_name, row, col), "")


def show_intro(wait_func=None):
    type_text(intro_text, wait_func=wait_func)
