# Adventure Game (Maze Runner)

A small dungeon-crawler built with Python and Tkinter, done together with Eric. You wake up in a dark maze, and have to explore it, fight enemies, collect items and find the exit — classic top-down maze RPG stuff, but from scratch with no game engine.

## Features

- Grid-based maze with a fog-of-war style vision range — you only see tiles around your current position, and until you find the torch you only see what's right next to you
- Character stats: HP, attack, defense, EXP and leveling (`game_logic.py`)
- Round-based fights: every button press is one round — attack, defend (halves the damage you take), drink a potion or try to flee. If you flee, the enemy keeps its damage for the next try
- Goblins to fight, potions and chests to find, and a boss guarding the exit
- Type in your own hero name on the start screen (it stays the same when you restart)
- Game over when your HP hits 0, press Enter to try again
- Story text tied to specific positions in the maze (`story.py`) — walking into certain tiles triggers narrative snippets, so exploring feels a bit more alive than just "you moved"
- Full Tkinter GUI (`gui.py`) showing the maze, stats panel, inventory and story log

## Controls

| Key | Action |
| --- | --- |
| `Enter` | Start the game after typing your name / restart |
| `W` `A` `S` `D` | Move |
| `1` | Attack |
| `2` | Defend |
| `3` | Use potion |
| `4` | Flee |

## Structure

```
AdventureGame/
├── main.py              # Entry point, loads the level and starts the GUI
├── gui.py               # Tkinter window, rendering, input handling
├── game_logic.py        # Character, Enemy, Item and Fight classes
├── maze.py              # Maze class — movement, items, enemies, vision range
├── story.py             # Position-triggered story text
├── levels/
│   └── level_1.txt      # Maze layout (I = wall, O = player, A = exit, ...)
└── tests/               # unittest tests for game logic and maze
```

### How the classes work together

- `Character` holds stats, inventory and leveling. `Enemy` inherits from it and adds the EXP you get for a kill.
- `Fight` takes a player and an enemy and runs one round per player action, it returns the log text that the GUI shows.
- `Maze` knows the map and the player position. Walking into an enemy returns that enemy, and the GUI starts a `Fight` with it.
- `MainWindow` only draws and reacts to keys/buttons, the rules live in the other classes.

## Running it

No external dependencies — just Python 3 with Tkinter (comes bundled with most Python installs).

```bash
python main.py
```

Run the tests:

```bash
python -m unittest
```

## What I'd do differently next time

This was one of my earlier Python projects. After finishing it I went back, moved the maze layout into a text file, cleaned up the GUI (the maze grid used to be 25 copy-pasted labels) and finished the round-based fight system we had planned. Next steps would be more levels and enemies with different behaviour, and probably separating the game state from the GUI a bit more so the whole game could also run in the terminal.
