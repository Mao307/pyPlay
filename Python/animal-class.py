# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 03:31:05 2023

@author: Moawia
"""
import math
import string
class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        
    def attack(self, player):
        # Call the player's take_damage method to reduce their health by the enemy's damage
        player.take_damage(self.damage)
    def recive_damage (self, damage):
        self.health-= damage

class Zombie(Enemy):
    def __init__(self):
        # Initialize the zombie's attributes using the parent class's constructor
        super().__init__('Zombie', 50, 5)

    
class Vampire(Enemy):
    def __init__(self):
        # Initialize the vampire's attributes using the parent class's constructor
        super().__init__('Vampire', 100, 10)
        self.life_steal = 0.1


class Player:
    def __init__(self, name, health,damage):
        self.name = name
        self.health = health
        self.damage= damage
    def take_damage(self, damage):
        # Reduce the player's health by the given amount of damage
        self.health -= damage
    def attack(self, enemy):
        enemy.recive_damage(self.damage)

# Create instances of the enemy and player classes
vampire = Vampire()
zombie = Zombie()
player = Player('moawia', 100, 20)

# Have the enemies attack the player and print their remaining health


zombie.attack(player)
print(f"{player.name}'s health: {player.health}")

vampire.attack(player)
print(f"{player.name}'s health: {player.health}")

# Print the vampire's life steal attribute
print(f"{vampire.name}'s life steal: {vampire.life_steal}")

player.attack(vampire)
print(vampire.health)

player.attack(zombie)
print(zombie.health)

print(isinstance(math))
