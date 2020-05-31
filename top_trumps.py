# Top Trumps

# A small game where players compare stats. The basic flow of the game is:
# 1. You are given a random card with different stats.
# 2. You select one of the card's stats.
# 3. Another random card is selected for your opponent (the computer)
# 4. The stats of the two cards are compared.
# 5. The player with the stat higher than their opponent wins. 

# The project will use the Pokemon API

total_opponent_score = 0
total_my_score = 0

def get():

    my_score = 0
    opponent_score = 0

    def choose_pokemon():
        for i in range(5):
            get_pokemon = random_pokemon()
            print(get_pokemon['name'].title())
    choose_pokemon()
    chosen_pokemon = input('Which pokemon would you like to choose? ')

    import requests
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(chosen_pokemon)
    # print(url)
    response = requests.get(url)
    my_pokemon = response.json()
    print("Your pokemon is {} with ID: {}, height: {}, and weight: {}.".format(my_pokemon['name'].title(), my_pokemon['id'], my_pokemon['height'], my_pokemon['weight']))

    # Get a random pokemon for the opponent
    opponents_pokemon = random_pokemon()
    print("The opponent's pokemon is: {}".format(opponents_pokemon['name'].title()))

    # Ask the player which stat they want to use
    chosen_stat = input('Which stat do you want to use? ')

    # Compare the opponents and players stat
    if my_pokemon[chosen_stat] > opponents_pokemon[chosen_stat]:
        my_score += 1
        print('You win this round!')
        return my_score, opponent_score
    elif my_pokemon[chosen_stat] < opponents_pokemon[chosen_stat]:
        opponent_score += 1
        print('You lose this round!')
        return my_score, opponent_score
    elif my_pokemon[chosen_stat] == opponents_pokemon[chosen_stat]:
        print('You draw!')
        my_score += 1
        opponent_score += 1
    return my_score, opponent_score

# Play multiple rounds and record the outcome of each round. The player with most
# number of rounds won, wins the game.

for score in range(5):
    total_me, total_opponent = get()
    total_my_score += total_me
    total_opponent_score += total_opponent
    # # total_opponent_score += get(opponent_score)
    # print(total_my_score, total_opponent_score)
    print("Your current score is {}. Your opponent's score is {}.".format(total_my_score, total_opponent_score))

# print(total_my_score, total_opponent_score)
if total_opponent_score > total_my_score:
    print('You lost to your opponent ({}, {}), better luck next time!'.format(total_my_score, total_opponent_score))
elif total_opponent_score < total_my_score:
    print('You won your opponent ({}, {}), well done!'.format(total_my_score, total_opponent_score))

# Record high scores for players and store them in a file

def pokemon_file():
    
    import csv
    import os.path
    field_names = ['My Score', 'Opponent Score']
    data = [
        {'My Score': total_my_score, 'Opponent Score': total_opponent_score},
    ]
    path = './scores.csv'

    if os.path.exists(path):
        with open('scores.csv', 'a') as csv_file:
            spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
            spreadsheet.writerows(data)
    else:
        with open('scores.csv', 'w+') as csv_file:
            spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
            spreadsheet.writeheader()
            spreadsheet.writerows(data)

pokemon_file()