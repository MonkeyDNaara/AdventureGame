# Adventure Game (Maze Runner)

A small dungeon-crawler built with Python and Tkinter, done together with Eric. You wake up in a dark maze, and have to explore it, fight enemies, collect items and find the exit — classic top-down maze RPG stuff, but from scratch with no game engine.

## Features

- Grid-based maze with a fog-of-war style vision range — you only see tiles around your current position
- Character stats: HP, attack, defense, XP and leveling (`game_logic.py`)
- Random encounters — goblins to fight, potions and chests to find
- A boss fight near the exit
- Story text tied to specific positions in the maze (`story.py`) — walking into certain tiles triggers narrative snippets, so exploring feels a bit more alive than just "you moved"
- Full Tkinter GUI (`gui.py`) showing the maze, stats panel and story log

## Structure

```
AdventureGame/
├── main.py         # Entry point, defines the maze layout, launches the GUI
├── gui.py          # Tkinter window, rendering, input handling
├── game_logic.py   # Character class — stats, leveling, combat
├── maze.py         # Maze representation + vision range logic
└── story.py        # Position-triggered story text
```

## Running it

No external dependencies — just Python 3 with Tkinter (comes bundled with most Python installs).

```bash
python main.py
```

## What I'd do differently next time

This was one of my earlier Python projects, and looking back there's stuff I'd restructure — the maze layout is hardcoded as a nested list in `main.py` instead of loaded from a file, and the GUI and game logic are a bit more tangled together than I'd like. Keeping it as-is for now as an honest snapshot of where I was at, but it's on my list to revisit once I've covered more OOP patterns in the course.
