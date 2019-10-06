# Memory
### A PyGame implementation of the traditional card-matching memory game

#### External libraries:
* PyGame

#### Instructions to run:
* Clone this repo from the command line: 
    * `git clone git@github.com:JacquelineMai/pygameMemory.git` with ssh
  or
    * `git clone https://github.com/JacquelineMai/pygameMemory.git` with https
* If you do not already have PyGame installed, run `pip install pygame`
* Enter the cloned directory and launch the game with `python3 game.py`

#### Explanation for design:
* I used the PyGame module because it allowed me to generate a graphical interface, which gave me a lot more freedom in designing the game
* The only class I built was the `Card` class, since it is the most modular component of the game
* The `game` file handles all the logic, which I broke up into functions based on the stage of the game in which the actions should be executed
* I tried to finish building this game within a time limit, but if I were to extend it I would further modularize the structure and probably break the grid out into an object of its own, as a container for the `Cards`
