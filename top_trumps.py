# Top Trumps

# A small game where players compare stats. The basic flow of the game is:
# 1. You are given a random card with different stats.
# 2. You select one of the card's stats.
# 3. Another random card is selected for your opponent (the computer)
# 4. The stats of the two cards are compared.
# 5. The player with the stat higher than their opponent wins. 

# The project will use the Pokemon API

def random_pokemon():
    # Generate a random number between 1 and 151 to use as the Pokemon ID number
    import random
    pokemon_number = random.randint(1, 152)
    import requests
    import json

    # Using the Pokemon API get a Pokemon based on its ID number
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    # print(pokemon['name'].title() + '\n' + str(pokemon_number) + '\n' + str(pokemon['height']) + '\n' + str(pokemon['weight']))

    # Create a dictionary that contains the returned Pokemon's name id, height and weight
    return {
        'name':pokemon['name'],
        'id':pokemon['id'],
        'height':pokemon['height'],
        'weight':pokemon['weight']
    }

# Get a random Pokemon for the player and another for their opponent
def get():
    my_pokemon = random_pokemon()
    print("Your pokemon is {} with ID: {}, height: {}, and weight: {}.".format(my_pokemon['name'].title(), my_pokemon['id'], my_pokemon['height'], my_pokemon['weight']))

    opponents_pokemon = random_pokemon()
    print("The opponent's pokemon is: {}".format(opponents_pokemon['name'].title()))

    # Ask the player which stat they want to use
    chosen_stat = input('Which stat do you want to use? ')

    # Compare the opponents and players stat
    if my_pokemon[chosen_stat] > opponents_pokemon[chosen_stat]:
        print('You win!')
    elif my_pokemon[chosen_stat] < opponents_pokemon[chosen_stat]:
        print('You lose!')
    elif my_pokemon[chosen_stat] == opponents_pokemon[chosen_stat]:
        print('You draw!')
get()
