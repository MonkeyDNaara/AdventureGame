import sys
import time

# def type_text(text, delay=0.03):
#     output_text = ""
#     for char in text:
#         # sys.stdout.write(char)
#         # sys.stdout.flush()
#         time.sleep(delay)
#         output_text += char
#     return output_text


intro_text = """
You wake up on a cold stone floor.
The air is wet and water is dropping from the ceiling.
You can't see anything, but you hear the drops.
"""

room_texts = {
    ("main", 17, 1): """
Your eyes need a moment to adjust to the darkness..
Wait.. In the distance, a faint orange light flickers.""",
    ("main", 16, 1): """
Your hand touches a wall. Another wall answers on the other side.
""",
    ("main", 15, 1): """
It's already getting a little bit lighter in front of you.
""",
    ("main", 11, 4): """
Old scratches cover the floor.
Something must have crossed this room many times.
""",
    ("main", 17, 13): """
The dark is restless here.

""",
    ("main", 19, 10): """
You have found the way out.
"""
}


# def get_room_text(level_name, x, y):
#     key = (level_name, x, y)

#     return room_texts.get(
#         key,
#         "The room is silent. The darkness seems to swallow every sound."
        
#     )


# def show_intro():
#     type_text(intro_text)