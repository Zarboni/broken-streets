# Broken Streets

*A 2D Side-Scrolling Beat 'Em Up Game built in Python using Pygame.*

---

## Concept
A street-level brawler inspired by classics like Final Fight, Punisher, and Streets of Rage.

Built from scratch for clean code, easy scaling, and future expansion.

---

## Features (v1.0.0)
- Game window with title `Broken Streets`
- Static background
- Controllable Player (move left/right)
- Base game structure for adding:
  - Characters
  - Enemies
  - Levels
  - Combat mechanics
  - Sound & Music

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

Future Roadmap

    Character Select Screen

    Enemy AI

    Punch & Combat System

    Health Bars

    Story Elements

    Scrolling Backgrounds

    Sound Effects & Music


---

## 2. CHANGELOG.md

```markdown
# Changelog

## [v1.0.0] - 2025-04-15

### Added
- Base project structure
- Game window (800x600)
- Static background
- Player character with left/right movement
- Ready for expansion (character select, enemies, etc.)

---

## Upcoming
- Character Select Screen
- Enemy AI & Behavior
- Combat System
- Health Bars
- Story Progression
