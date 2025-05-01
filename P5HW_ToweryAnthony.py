# Anthony Towery
# April 22nd, 2025
# P5HW 
# Making a game with Python coding
# Code credits goes to Microsoft Co-Pilot AI
# My ideas was a game where you have to escape a pyramid and without losing to the mummies, it is called Escaping the Pyramid!
import random  # Importing the random library for generating random events

def create_character(name):
    """
    Function name: create_character
    Parameters: name (str) - The name of the game character
    Returns: dict - A dictionary representing the game character
    This function creates and returns a game character with random attributes.
    """
    character = {
        'name': name,
        'health': random.randint(50, 100),
        'inventory': ['map', 'torch']
    }
    return character

def start(character):
    """
    Function name: start
    Parameters: character (dict) - The game character
    Returns: None
    This function starts the game and navigates the player through the pyramid.
    """
    print(f"You are stuck in the pyramid, {character['name']}. You need to find a way to escape.")
    paths = ['left', 'right', 'straight', 'down']
    random.shuffle(paths)
    choice = input(f"Do you want to go '{paths[0]}', '{paths[1]}', '{paths[2]}', or '{paths[3]}'? ")
    if choice.lower() == paths[0]:
        room1(character)
    elif choice.lower() == paths[1]:
        room2(character)
    elif choice.lower() == paths[2]:
        room3(character)
    elif choice.lower() == paths[3]:
        trap(character)
    else:
        print("Invalid choice. Try again.")
        start(character)

def room1(character):
    """
    Function name: room1
    Parameters: character (dict) - The game character
    Returns: None
    This function handles the logic for the first room in the pyramid.
    """
    print("You have entered a room with a treasure chest.")
    choice = input("Do you want to 'open' the chest or 'leave' the room? ")
    if choice.lower() == 'open':
        print("You found a golden idol! You win!")
    elif choice.lower() == 'leave':
        start(character)
    else:
        print("Invalid choice. Try again.")
        room1(character)

def room2(character):
    """
    Function name: room2
    Parameters: character (dict) - The game character
    Returns: None
    This function handles the logic for the second room in the pyramid.
    """
    print("You have entered a room with a sleeping mummy.")
    choice = input("Do you want to 'sneak' past the mummy or 'wake' the mummy? ")
    if choice.lower() == 'sneak':
        print("You successfully sneaked past the mummy and found the exit! You win!")
    elif choice.lower() == 'wake':
        print("The mummy woke up and attacked you. Prepare to fight!")
        fight_mummy(character)
    else:
        print("Invalid choice. Try again.")
        room2(character)

def room3(character):
    """
    Function name: room3
    Parameters: character (dict) - The game character
    Returns: None
    This function handles the logic for the third room in the pyramid.
    """
    print("You have entered a room with multiple mummies.")
    choice = input("Do you want to 'fight' the mummies or 'run' away? ")
    if choice.lower() == 'fight':
        fight_mummies(character)
    elif choice.lower() == 'run':
        print("You ran away and returned to the entrance.")
        start(character)
    else:
        print("Invalid choice. Try again.")
        room3(character)

def trap(character):
    """
    Function name: trap
    Parameters: character (dict) - The game character
    Returns: None
    This function handles the logic for falling into a trap.
    """
    print("You fell into a trap! Game over.")
    play_again(character)

def fight_mummy(character):
    """
    Function name: fight_mummy
    Parameters: character (dict) - The game character
    Returns: None
    This function handles the logic for fighting a single mummy.
    """
    print("You are fighting the mummy!")
    character['health'] -= random.randint(10, 30)
    if character['health'] <= 0:
        print("You have no health left. Game over.")
        play_again(character)
    else:
        print("You defeated the mummy and found the exit! You win!")

def fight_mummies(character):
    """
    Function name: fight_mummies
    Parameters: character (dict) - The game character
    Returns: None
    This function handles the logic for fighting multiple mummies.
    """
    print("You are fighting the mummies!")
    num_mummies = random.randint(1, 3)
    for _ in range(num_mummies):
        print("A mummy attacks!")
        character['health'] -= random.randint(10, 30)
        if character['health'] <= 0:
            print("You have no health left. Game over.")
            play_again(character)
            return
    print("You defeated the mummies and found the exit! You win!")

def play_again(character):
    """
    Function name: play_again
    Parameters: character (dict) - The game character
    Returns: None
    This function prompts the player to play again if they lose.
    """
    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() == 'yes':
        main()

def main():
    """
    Function name: main
    Parameters: None
    Returns: None
    This function initializes the game character and starts the game.
    """
    name = input("Enter your character's name: ")
    character = create_character(name)
    start(character)
    if character['health'] > 0:
        play_again(character)

if __name__ == "__main__":
    main()
