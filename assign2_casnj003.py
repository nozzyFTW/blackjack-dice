#
# File: assign2_casnj003.py
# Author: Noah Casey
# Email Id: casnj003
# Description: Assignment 2 - Blackjack - Dice Edition
#
#              DESCRIPTION
#
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

import blackjack

def display_details():
    """ Displays my details

    Parameters: None
    Returns: None
    """
    print("File\t : casnj003_battle_p2.py")
    print("Author\t : Noah Casey")
    print("Stud ID\t : 110443599")
    print("Email ID : casnj003")
    print("This is my own work as defined by the\nUniversity's Academic Misconduct Policy.", end="\n\n")

def read_file(filename: str) -> list[list]:
    """ Reads the player data from saved file
    
    Parameters: filename -- the name of the file to open -> type: str
    Returns: player_list -- list containing each player object (list) -> type: list[list]
    """
    player_list = []

    infile = open(filename, "r")

    # Reads all the lines of the text file to a list
    lines = infile.readlines()

    temp_player = []
    index = 0

    # Loop through list of lines
    for line in lines:
        # First line contains the name of the player
        # and second line contains the player's stats
        if index % 2 == 0:
            # Prevents later issues when displaying player's name
            # (prevents added new lines when not wanted)
            name = line.strip("\n")
        else:
            info_list = line.split()
            played = int(info_list[0])
            won = int(info_list[1])
            lost = int(info_list[2])
            drawn = int(info_list[3])
            chips = int(info_list[4])
            score = int(info_list[5])
            
            # Adds player to the player list using the format:
            # | Player Name | Games Played | Won | Lost | Drawn | Chips | Score |
            temp_player = [name, played, won, lost, drawn, chips, score]
            player_list.append(temp_player)
        index += 1

    infile.close()
    return player_list

def write_to_file(filename: str, player_list: list[list]) -> None:
    """ Writes player stats to file

    Parameters: filename -- the name of the file to write to -> type: str
                player_list -- list containing each player object (list) -> type: list[list]

    Returns: None
    """
    outfile = open(filename, "w")
    
    # Runs through each player and append players to the file using the format:
    # | Player Name |
    # | Games Played | Won | Lost | Drawn | Chips | Score |
    for player in player_list:
        outfile.write(f"{player[0]}\n{player[1]} {player[2]} {player[3]} {player[4]} {player[5]} {player[6]}\n")

    outfile.close()

def display_players(player_list: list[list]):
    print("===========================================================")
    print("-                     Player Summary                      -")
    print("===========================================================")
    print("-                             P  W  L  D   Chips   Score  -")
    print("-----------------------------------------------------------")

    # Displays each player's stats in format:
    # | Player Name | Games Played | Won | Lost | Drawn | Chips | Score |
    # |-----------------------------------------------------------------|
    for player in player_list:
        print(f"- {format(player[0], '25s')}  {format(player[1], '2d')} {format(player[2], '2d')} {format(player[3], '2d')} {format(player[4], '2d')}   {format(player[5], '5d')}   {format(player[6], '5d')}  -")
        print("-----------------------------------------------------------")
    print("===========================================================")

def find_player(player_list: list[list], name: str) -> int:
    """ Finds index of player within player list

    Parameters: player_list -- list containing each player object (list) -> type: list[list]
                name -- inputted player name -> type: str

    Returns: index | -1 -- if player is found, player's location in player list is returned -> type: int
                        -- if player is not found, return -1
    """
    index = 0
    for player in player_list:
        if name == player[0]:
            # return index of player in player_list
            return index
        index += 1
    # Returns -1 if no player found
    return -1

def buy_player_chips(player_list: list[list], name: str) -> None:
    """ Allows the player to buy chips

    Parameters: player_list -- list containing each player object (list) -> type: list[list]
                name -- inputted player name -> type: str
    
    Returns: None
    """
    player_index = find_player(player_list, name)
    # Checks if player exists based off returned player index
    if player_index != -1:
        print(f"{name} currently has {player_list[player_index][5]} chips.")

        request = True      # Changed to False when integer entered is between 1 and 100 and
                            # ensures that an input is made for requested_chips before continuing
        while request:
            requested_chips = input("How many chips would you like to buy? ")

            # Determines that the entered input can be converted to
            # an integer before testing if < 1 or > 100
            if not requested_chips.isdigit():
                print("Please enter an integer between 1-100.")
            else:
                requested_chips = int(requested_chips)
                if requested_chips < 1 or requested_chips > 100:
                    print("You may only buy between 1-100 chips at a time.")
                else:
                    request = False
                    player_list[player_index][5] += requested_chips
                    print(f"Successfully updated {name}'s chip balance to {player_list[player_index][5]}")
    else:
        print(f"{name} is not found in player list.")

def display_highest_chip_holder(player_list: list[list]) -> None:
    """ Displays the highest chip holder
    
    Parameters: player_list -- list containing each player object (list) -> type: list[list]
    Returns: None
    """
    highest_chip_index = -1     # The index of the highest chip holder (-1 to ensure 
                                # that the index isn't an actual index) -> type: int
    highest_chip = 0            # Highest amount of chips -> type: int
    index = 0                   # Used to set the highest_chip_index -> type: int

    for player in player_list:

        # Checks if player's chips is higher than current
        # highest chip holder's.
        if player[5] > highest_chip:
            highest_chip = player[5]
            highest_chip_index = index

        # Else it checks if the player has the same amount
        # of chips as the highest chip holder.
        elif player[5] == highest_chip:

            # If the player has the same amount of chips, then check if 
            # games played is less than highest chip holder.
            if player[1] < player_list[highest_chip_index[0]][1]:
                highest_chip = player[5]
                highest_chip_index = index
            
            # Else it checks if the player has the same amount
            # of games played as the highest chip holder
            elif player[1] == player_list[highest_chip_index[0]][1]:

                # If the player has the same amount of games played, then check if
                # the player's score is greater than the highest chip holder's score
                if player[6] > player_list[highest_chip_index[0]][6]:
                    highest_chip = player[5]
                    highest_chip_index = index

                # Else it checks if the player has the same score as 
                # the highest chip holder.
                elif player[6] == player_list[highest_chip_index[0]][6]:
                    
                    # If the player has the same score as the highest chip holder,
                    # then check if the player's win/loss percentage is higher.
                    player_win_percent = player[2] / player[1]
                    highest_win_percent = player_list[highest_chip_index[0]][2] / player_list[highest_chip_index[0]][1]
                    if player_win_percent > highest_win_percent:
                        highest_chip = player[5]
                        highest_chip_index = index

                    # Else, add the index of the player to a list with the highest chip holder
                    else:
                        if type(highest_chip_index) == int:
                            highest_chip_index = [highest_chip_index, index]
                        else:
                            highest_chip_index.append(index)
        index += 1
    if len(player_list) == 0:
        print("Error: There are no players in player list")
    elif highest_chip == 0:
        print("Error: Highest chip is 0.")
    elif type(highest_chip_index) == list:
        index = 0
        for player_pos in highest_chip_index:
            print(f"Highest Chip Holder => {player_list[player_pos][0]} with {highest_chip} chips!")
            index += 1
    else:
        print(f"Highest Chip Holder => {player_list[highest_chip_index][0]} with {highest_chip} chips!")


def add_player(player_list: list[list], name: str) -> list[list]:
    if find_player(player_list, name) == -1:
          player_list.append([name, 0, 0, 0, 0, 100, 0])
          print(f"Successfully added {name} to player list.")
    else:
        print(f"{name} already exists in player list.")

    return player_list

def remove_player(player_list: list[list], name: str) -> list[list]:
    player_index = find_player(player_list, name)
    if player_index == -1:
        print(f"{name} is not found in players.")

    else:
        updated_list = []
        for player in player_list:
            if player[0] != name:
                updated_list.append(player)
        print(f"Successfully removed {name} from player list.")
        return updated_list

def play_blackjack_games(player_list, player_pos):
    player = player_list[player_pos]

    # player[5] => Chips, player[6] => Score
    player[6], player[5] = blackjack.play_one_game(player[5])      # Returns list [score from game, number of chips]

    playing = None
    while playing != "y" and playing != "n":
        playing = input("Play again [y|n]? ")
        if playing == "y":
            play_blackjack_games(player_list, player_pos)
        elif playing != "n":
            print("Please enter 'y' or 'n'.")

# sorted [original index, games, chips, score]
def sort_by_chips(player_list: list[list]) -> list[list]:
    sorted_list = []
    index = 0
    for player in player_list:
        sorted_list = compare_chips(sorted_list, player, index)
        index += 1
    return sorted_list

def insert_item(target_list: list[list], target_index: int, item: any) -> list[list]:
    index = 0
    temp_list = []
    while index < (len(target_list) + 1):
        if index == target_index:
            temp_list.append(item)
        elif index > target_index:
            temp_list.append(target_list[index - 1])
        else:
            temp_list.append(target_list[index])
        index += 1
    return temp_list


def compare_chips(sorted_list: list[list], player: list, temp_index: int) -> list[list]:
    prev_temp = temp_index
    temp_index -= 1
    if len(sorted_list) == 0:
        sorted_list.append(player)
    elif player[5] > sorted_list[temp_index][5]:
        if temp_index == 0:
            sorted_list = insert_item(sorted_list, temp_index, player)
        else:
            sorted_list = compare_chips(sorted_list, player, temp_index)
    else:
        sorted_list = insert_item(sorted_list, prev_temp, player)
    return sorted_list

display_details()

player_list = read_file("players.txt")

choice = None
while choice != "quit":
    print("\nPlease enter choice")
    choice = input("[list, buy, search, high, add, remove, play, chips, quit]: ")
    print("")

    if choice == "list":
        display_players(player_list)

    elif choice == "buy":
        name = input("Please enter name: ")
        buy_player_chips(player_list, name)

    elif choice == "search":
        name = input("Please enter name: ")
        player_pos = find_player(player_list, name)
        
        if player_pos == -1:
            print(f"{name} is not found in player list.")
        else:
            player = player_list[player_pos]
            print(f"{name} stats:", end="\n\n")
            print("P  W  L  D  Score")
            print(f"{format(player[1], '<2')} {format(player[2], '<2')} {format(player[3], '<2')} {format(player[4], '<2')} {format(player[6], '<2')}", end="\n\n")
            print(f"Chips:  {player[5]}", end="\n")

    elif choice == "high":
        player_list = [['Bruce Wayne', 7, 4, 0, 3, 300, 15], ['Jessica Jones', 12, 0, 6, 6, 10, 6], ['Johnny Rose', 7, 4, 0, 3, 300, 15], ['Gina Linetti', 7, 4, 0, 3, 300, 15], ['Buster Bluth', 3, 0, 2, 1, 50, 1]]
        display_highest_chip_holder(player_list)

    elif choice == "add":
        name = input("Please enter name: ")
        add_player(player_list, name)

    elif choice == "remove":
        name = input("Please enter name: ")
        player_list = remove_player(player_list, name)

    elif choice == "play":
        name = input("Please enter name: ")
        player_pos = find_player(player_list, name)
        
        if player_pos == -1:
            print(f"{name} is not found in player list.")
        else:
            play_blackjack_games(player_list, player_pos)

    elif choice == "chips":
        sorted_list = sort_by_chips(player_list)
        display_players(sorted_list)

    elif choice == "quit":
        write_to_file("new_players.txt", player_list)
        print("\n-- Program terminating --", end="\n\n\n")
        print("NOTE: Your program should output the following information to a file - new_players.txt.", end="\n\n")
        
        # Display outputted data
        for player in player_list:
            print(f"{player[0]}\n{player[1]} {player[2]} {player[3]} {player[4]} {player[5]} {player[6]}")
    else:
        print("Not a valid command - please try again.")