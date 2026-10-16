import time
import random
import gaming_tools


def start_game () :
 """"Start a new game: erase everithing(all planets and ships of the previous game are removed) and create the 2 imposed planets
 Aldebaran is palced at (0, 0) and Epsilon AUrigae at (1000, 1000). Both have no ressource
 """

def create_planet (planet, position_x, position_y) :
 """Add a planet to the board.
 The ressources of the planet are choosen radomly

 Parameters
 ------------
 planet: planet name (str)
 position_x: x postion of the planet, in parsec (int)
 position_y; y position of the planet, in parsec (int)
 
 Notes
 -------
 NOthing is created and an error message is printed if the name is invalid or already used, if a position is not
 an integer
 
 1 parsec = 3 * 10¹³ km   """

def create_ship () :
 """"Creates the ship of a player. All ship start the race on the planet Aldebaran.
 
 The ship is not broken, has a spees of 1 parsec/second and can play immediately.
 
 Parameters
 ------------
 ship: ship name (str)
 
 Notes
 -------
 Nothing is created and an error message is printed if the name is invalid or already used, or if the 
 game was not started(no Aldebaran)
 The rule "One ship per player " is not verify"""

def display_planent_info (planet): 
 """ Display the location and the ressources of a planet 
 
 Parameters
 ------------
 planet: planet name(str)
 
 Notes
 --------
 An error message is  printed if the  planet does not exist"""


def display_ship_info (ship):
 """" Dispaly the state of a ship (location, speed, condition)
 
 Parameters
 ------------
 ship: ship name (str)
 
 Notes
 -------
 An error message is prinnted if the planet does not exists"""

def move_ship (ship, destination) : 
 """"Make a ship perform a collapsar jump to the  indicated planet.
 
 The jump  lasts distance/speed seconds, during which the ship cannot receive any order. 
 The ship has 1 chnce out of 3 to breakdown; it still reach his destination but can then can only be repaiir.
 
 Parameters
 ------------
 ship: ship name (str)
 destination: name of the destination planet (str)
 
 Notes
 -------
 The move is  refused (an errror message) if the does not exist, is busy or broken, 
 if the destination does not exist or if the  ship is already on the destination"""


