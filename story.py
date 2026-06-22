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

story_texts = {
    "intro":    "You wake up on a cold stone floor.\nThe air is wet and water is dropping from the ceiling.\nYou can't see anything, but you hear the drops.",
    "part1":    "Your eyes need a moment to adjust to the darkness..\nWait.. In the distance, a faint orange light flickers.",
    "part2":    "Your hand touches a wall. Another wall answers on the other side.",
    "part3":    "It's already getting a little bit lighter in front of you.",
    "part4":    "Old scratches cover the floor.\nSomething must have crossed this room many times.",
    "part5":    "The dark is restless here.",
    "torch_part":   "You picked up the torch.\nYou can now see around you. What a relief.",
    "boss_part" :   "You defeated the amazed boss :o",
    "exit_part" :   "You made it, You found the exit! Congrats!",
    "potion"    :   "You found a potion",
    "goblin"    :   "Goblin defeated",
    "chest"     :   "You found a chest"
    }

story_positions = {
    (18, 1): "intro", 
    (17, 1): "part1", 
    (16, 1): "part2", 
    (15, 1): "part3", 
    (11, 4): "part4", 
    (10, 5): "part5",
    (14, 1): "torch_part",
    (18, 10): "boss_part",
    (19, 10): "exit_part",
    ((1, 11), (9, 11), (11, 2), (14, 11), (18, 8)): "potion",
    ((2, 4), (4, 15), (14, 13), (15, 5)): "goblin",
    ((1, 14), (2, 1)): "chest"
    }




# def get_room_text(level_name, x, y):
#     key = (level_name, x, y)

#     return room_texts.get(
#         key,
#         "The room is silent. The darkness seems to swallow every sound."
        
#     )


# def show_intro():
#     type_text(intro_text)