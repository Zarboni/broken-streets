# Broken Streets

*A 2D Side-Scrolling Beat 'Em Up Game built in Python using Pygame.*

---

## Concept
A street-level brawler inspired by classics like Final Fight, Punisher, and Streets of Rage.

Built from scratch for clean code, easy scaling, and future expansion.

---

## Features (v1.5.0)
- Character Select Screen (Graves, Red, Vee)
- Player Movement (Left / Right)
- Player Color changes based on selection
- Player Punch Mechanic (SPACE key)
- Enemy AI (Follows player)
- Enemy Health System (3 hits to die)
- Enemy Health Bar (Above enemy)
- Player Health System (3 HP)
- Player Health Bar (Above player)
- Enemy Punches Player on contact
- Game Over Screen on player death
- Restart (`R`) or Quit (`Q`) from Game Over



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

- Scrolling Backgrounds / Levels
- Multiple Enemies per level
- Level Transition System
- HUD Overlays (score, lives)
- Main Menu (Start / Options / Quit)
- Sound Effects & Music
- Punch + Death Animations
- Boss Fights & Stage Design
- Story & Dialogue Reveal
