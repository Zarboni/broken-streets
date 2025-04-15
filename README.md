# Broken Streets

*A 2D Side-Scrolling Beat 'Em Up Game built in Python using Pygame.*

---

## Concept
A street-level brawler inspired by classics like Final Fight, Punisher, and Streets of Rage.

Built from scratch for clean code, easy scaling, and future expansion.

---

## Features (v1.2.0)
- Character Select Screen (Graves, Red, Vee)
- Player color changes based on selected character
- Player Movement (Left / Right)
- Player Punch Mechanic (SPACE)
- Enemy AI: Walks towards player
- Enemy Health System with Health Bar
- Enemy dies after 3 hits


---

## Setup Instructions

```bash
# Activate virtual environment
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate

# Install dependencies
pip install -r requirements.txt

# Run the game
python main.py

Project Structure

    main.py → Game loop

    settings.py → Global settings

    game/ → Game logic (Player, Enemy, Level, etc.)

    assets/ → Images, Sounds, Fonts

    data/ → JSON files for character info

    requirements.txt → Python dependencies

    CHANGELOG.md → Version history

    TESTING.md → Manual testing notes

## Future Roadmap

- Player Health Bar
- Enemy Punch / Attack Mechanic
- Multiple Enemies
- Player Death + Game Over screen
- Level Transitions
- Sound Effects & Music
