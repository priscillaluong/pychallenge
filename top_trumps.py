# Top Trumps

# A small game where players compare stats. The basic flow of the game is:
# 1. You are given a random card with different stats.
# 2. You select one of the card's stats.
# 3. Another random card is selected for your opponent (the computer)
# 4. The stats of the two cards are compared.
# 5. The player with the stat higher than their opponent wins. 

# The project will use the Pokemon API

# Generate a random number between 1 and 151 to use as the Pokemon ID number

import random
pokemon_number = random.randint(1, 152)

# Using the Pokemon API get a Pokemon based on its ID number

import requests
import json

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
response = requests.get(url)
pokemon = response.json()
poke_name = pokemon['name']
print(poke_name.title() + '\n' + str(pokemon_number))

