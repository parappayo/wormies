# wormies

Snake-like game protoype using Pygame. Loosely inspired by Slither.io.

## Setup

* `pipenv install`
* `pipenv run python wormies.py`

## Packages

The project architecture is split into packages:

* `gui` (Graphical User Interface) sits on top of pygame and implements graphics routines and input handlers, it is responsible for displaying the current state of the game and relaying input events back into the game state
* `game` implements the "buiness logic" of the game rules, it aims to be agnostic of how the game is interacted with

## Background Notes

In my opinion, Slither ought to refer to the Colecovision game riffing off of Atari's Centipede rather than Slither.io. It's worth noting that Slither.io is a close cousin of the classic Snake game. I've chosen the name Wormies for this project even though it conflicts with the Worms franchise.

See also: the episode of Red Dwarf entitled "Better than Life" where Cat says "it's party time for all those little worms." Red Dwarf is _strongly_ recommended.
