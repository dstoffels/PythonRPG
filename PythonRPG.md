Python RPG
Learning objective: Use and practice Python fundamentals, with an emphasis on
Single Responsibility functions.
Technologies: Python, Functions, Data Types, Flow Control (Conditionals), Loops,
Dictionary/List Data Structures

Extra Credit Points: 5
You are Hercules, the greatest of the Greek Heroes! You have been tasked by King
Eurystheus to slay the vicious Nemean Lion, defeat the impossible nine-headed
Lernaean Hydra, and capture the guard dog of the underworld—Cerberus.

Features:

<!-- As a developer, I want to make at least five commits on GitHub with descriptive
messages. -->

As a user, I want an engaging story to be told using print() statements.

-dynamic user prompt should display current health and combat status

<!-- -player must be able to traverse a 10x10 grid of manually generated 'locations' -->
<!-- --persistent dict of locations keyed by coordinates -->
<!-- --each location must determine which directions are available based on all locations in locations dict -->
<!-- --player can move N,S,E or W -->
<!-- --when player moves, the location description is displayed to user -->

-need to display other entities at locations
--persistent list of all enemy entities and their locations
--each time player moves to one of these locations, a func displays entities in the room
--if other entity is an enemy, player movement is suspended by combat

As a user, I want Hercules (and each enemy), to have health, attack power, and a List of attack names saved in a Dictionary.

-attack power will be determined by Hercules'/enemy's active weapon
--Hercules will upgrade their attack power/weapon after killing enemies
--attacks can either fail or crit based on D20 roll (1 = fail, 20 = crit)

-weapons: AP (attack power)
--fists: 3
--gladius: 5
--falx: 10

-attack options: AP bonus (cooldown)
--swing: 0 (2s)
--thrust: +2 (3s)
--SMASH: +7 (10s)

As a user, I want the ability to select Hercules’ attack using a menu prompt.

-user can enter commands to change the active attack
--attack names will serve as the commands to switch attack type

As a user, I want the foe’s attack to be chosen at random.

As a user, I want the results of each attack to be logged in the terminal.

As a developer, I want to use an Attack() function that will terminate when Hercules or an enemy’s health reaches zero.
-command: 'attack' will engage the enemy and lock Hercules into combat (unable to move until complete)

<!-- As a developer, I want my RunGame() function to call my other functions in a logical
order that will determine game flow. -->

<!-- As a developer, I want all of my functions to have a Single
Responsibility. Remember, each function should do just one thing! -->
