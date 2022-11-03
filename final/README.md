# Final Project

## Rock Paper Scizor

A simple game to be played against the computer, the computer should choose its play randomly

### Arguments:

- max-score: when reached the game should end(infinite by default)
- player-name: Name of the player(use last used name by default)

### Possible Input:

- Rock, 0
- Paper, 1
- Scizor, 2
- Exit or Quit
- Instructions

### Input Rules

- All input is not case sensitive
- For all the inputs any subset of the word can be used as long as it starts the same
    - ex. for rock all of the following should be accepted: r,ro,R,Rock,rOc

### Additional requirements:

- Keep track of the score
    - keep posting the score in between every play and in the end
- Ask the player's name in the beginning unless it was given as an argument
    - if the player's name is provided as an argument no name is asked for
    - if the player name was defined before but not given as an argument ask the player name, but if one is not given use the previous one

### Optional Features:

- Beginner
    - Add local multiplayer setup
- Mid
    - Add some sort of GUI
- Advanced
    - Add remote multiplayer