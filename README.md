Ping Pong Game (Python Tkinter)

A simple yet dynamic Ping Pong (Pong) game built using Python and Tkinter, featuring AI opponent logic, real-time collision handling, and smooth gameplay.


Features

* Real-time ball movement using Tkinter `after()` game loop
* Player vs AI gameplay
* Score tracking system
* Game states (Start, Playing, Paused, Game Over)
* Increasing ball speed after paddle collisions
* AI paddle movement based on ball tracking
* Sound feedback on paddle hits
* Pause functionality


Controls

* W / Up Arrow → Move paddle up
* S / Down Arrow → Move paddle down
* Space → Start game
* P → Pause / Resume


Concepts Used

* Event-driven programming
* Game loop using `after()`
* Collision detection (ball vs paddle, walls)
* AI movement logic
* State management (start, playing, paused, game over)
* Speed scaling and clamping


Tech Stack

* Python
* Tkinter


How to Run

```bash
python main.py
```

Game Rules

* First to reach **5 points wins**
* Ball resets after each score
* Speed increases with each paddle hit
* AI reacts to ball movement

What I Learned

* Designing real-time game loops without freezing UI
* Handling collision physics and edge cases
* Implementing simple AI behavior
* Managing game states effectively
* Debugging timing and speed-related bugs

Future Improvements

* Add difficulty levels for AI
* Add sound effects using external files
* Add restart option after game over
* Improve UI with menus


Built as part of hands-on learning in game development using Python.
