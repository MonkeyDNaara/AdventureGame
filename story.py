import sys
import time

def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


intro_text = """
You wake up on a cold stone floor.
Your head is spinning.
What happened last night?
You try to grasp what happend, but there's.. nothing.. you can't remember anything.

The air is wet and water is dropping from the ceiling,
you can't see it, but you hear the drops. 

You can hear your own breath. It's comeplety silent around you.
Goosebumps spread all over your body.

Your eyes need a moment to adjust to the darkness..
Wait.. In the distance, a faint orange light flickers.
"""


room_texts = {
    ("level_1", 0, 0): """
Your heart is pounding. You can feel your pulse in your chest. 
Your instincs are telling you to move and get the hell out of here.

Suddenly you hear a deep frightening scream not to far away.
Panic is setting in. 
For a moment, you froze. 
""",

    ("level_1", 0, 0): """ 
To get the light, you have to walk down that corridor.
(press up to move forwards - to the light)

""",
    ("level_1", 1, 0): """ 
It's cold and you can see your own breath.
It's getting a little bit brighter already.
(press up to move forwards)

""",
    ("level_1", 2, 0): """ 
What a nightmare, you think.
""",
    ("level_1", 3, 0): """ 
On the left wall next to you is a torch on the wall. 
You grab it. 
You can feel the warmth on your skin. 
"""
    ("level_1", 4, 0): """ 
The corridor narrows.
To your left, you hear a distant scream echoing though the walls.
Ahead of you lies a long, dark passage.
To your right stands a red door, its surface is marked with old scratches.

Where do you go?
(left, right , up)
""",
    }


def get_room_text(level_name, x, y):
    key = (level_name, x, y)

    return room_texts.get(
        key,
        "The room is silent. The darkness seems to swallow every sound."
        
    )


def show_intro():
    type_text(intro_text)