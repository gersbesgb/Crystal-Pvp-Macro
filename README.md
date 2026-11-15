# Minecraft Crystal Pvp Macros

A collection of lightweight, high-speed, and **file-less** macros designed for minecraft CPVP (Crystal PvP, Respawn Anchors, and Air Anchors). 

Built using Python with randomized timing loops to ensure smooth execution and compatibility with modern server anti-cheats.

---

## Quick Start (File-Less Launch)
You can launch any of these macros instantly on any PC without cloning the repository or manually managing Python files. 

1. Press **`Win + R`** on your keyboard.
2. Paste the desired command from below and hit **Enter**.

> **Note:** If the macro inputs do not register inside full-screen games, run your command prompt/terminal as **Administrator** (`Ctrl + Shift + Enter`).

---

## Available Macros & Launch Commands

### 1. All-in-One Combined Macro
Combines the D-tap, Anchor, and Air Anchor macros into a single macro with custom bind inputs on startup.
* **repositories**
   * [D-tap Macro](https://github.com/gersbesgb/D-tap-Macro)
   * [Anchor Macro](https://github.com/gersbesgb/Anchor-Macro)
   * [Air Anchor Macro](https://github.com/gersbesgb/Air-Anchor-Macro)

* **File-Less Launch Command:**
  ```cmd
  cmd /k python -m pip install -q keyboard mouse && python -c "import urllib.request; exec(urllib.request.urlopen('https://raw.githubusercontent.com/gersbesgb/Crystal-Pvp-Macro/refs/heads/main/cpvp.py').read().decode())"
