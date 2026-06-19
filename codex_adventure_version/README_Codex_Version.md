# Codex Adventure Version

This folder is a separate working copy. The original files in `/Users/ericwilts/AdventureGame` were left untouched.

## Goal of this version

This version is intentionally simple. It avoids complicated systems like random spawns, combat flow, cooldowns, special weapon weaknesses, or multiple weapon slots. The code is written with short functions and simple dictionaries so it is easier to explain in a school project.

## Controls

- `W A S D`: move without pressing Enter.
- `Space`: pick up the item under the player or open a chest.
- `I`: open inventory outside combat.
- `9`: use a Small Potion in the inventory.
- `0`: use a Big Potion in the inventory.
- `Q`: asks for confirmation, then returns to the start screen.
- Start screen: Enter starts a new run, `i` shows instructions, `q` quits the program.

## Map Symbols

- `●`: player.
- `I`: wall.
- `F`: torch.
- `p`: Small Potion.
- `P`: Big Potion.
- `S`: sword.
- `e`: Enemy Level 1.
- `E`: Enemy Level 2.
- `m`: Enemy Level 3.
- `M`: Enemy Level 4.
- `B`: Boss Level 10.
- `x`: key.
- `X`: chest.
- `!`: secret door.
- `A`: exit.
- `□`: unknown field.

## Current Rules

- The player starts with no vision, but the torch lights a small area around itself.
- After taking the torch, player vision expands.
- Items are only picked up after pressing Space.
- Item prompts show the item name and weapon strength when useful.
- Enemies have fixed values, but fights are disabled for now. Enemies block the way.
- XP and HP use the same dot display.
- The chest `X` requires key `x`. It contains the Iron Sword and 3 Big Potions.
- The secret door `!` switches between the main maze and the 10x10 hidden room.

## GUI-Friendly Functions

- `Maze.render(player)` returns the visible maze as text.
- `Maze.move_player(direction)` moves the player or blocks movement.
- `Maze.collect_current_item(player)` handles Space pickup and chest opening.
- `Maze.get_current_item_prompt()` returns the text shown below the map.
- `format_status(player)` returns level, XP, and HP.
- `format_inventory(player)` returns potion/key/sword info.
- `consume_messages(player)` returns and clears messages for the GUI.
