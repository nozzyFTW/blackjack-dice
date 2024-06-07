#
# File: assign2_casnj003.py
# Author: Noah Casey
# Email Id: casnj003
# Description: Assignment 2 - Blackjack
#
#              DESCRIPTION
#
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

import blackjack

def read_file(filename: str) -> list[list]:
    player_list = []

    infile = open(filename, "r")
    lines = infile.readlines()

    temp_player = []
    index = 0
    for line in lines:
        if index % 2 == 0:
            # Prevents later issues when displaying player's name
            name = line.strip("\n")
        else:
            info_list = line.split()
            played = int(info_list[0])
            won = int(info_list[1])
            lost = int(info_list[2])
            drawn = int(info_list[3])
            chips = int(info_list[4])
            score = int(info_list[5])

            temp_player = [name, played, won, lost, drawn, chips, score]
            player_list.append(temp_player)
        index += 1

    infile.close()
    return player_list

def write_to_file(filename: str, player_list: list[list]) -> None:
    outfile = open(filename, "w")
    
    for player in player_list:
        outfile.write(f"\n{player[0]}\n{player[1]} {player[2]} {player[3]} {player[4]} {player[5]} {player[6]}")

    outfile.close()

def display_players(player_list: list[list]):
    print("===========================================================")
    print("-                     Player Summary                      -")
    print("===========================================================")
    print("-                             P  W  L  D   Chips   Score  -")
    print("-----------------------------------------------------------")

    for player in player_list:
        print(f"- {format(player[0], '25s')}  {format(player[1], '2d')} {format(player[2], '2d')} {format(player[3], '2d')} {format(player[4], '2d')}   {format(player[5], '5d')}   {format(player[6], '5d')}  -")
        print("-----------------------------------------------------------")
    print("===========================================================")

def find_player(player_list: list[list], name: str) -> int:
    index = 0
    for player in player_list:
        if name == player[0]:
            return index
        index += 1
    return -1

def buy_player_chips(player_list: list[list], name: str) -> None:
    player_index = find_player(player_list, name)
    if player_index != -1:
        print(f"{name} currently has {player_list[player_index][5]} chips.")

        request = True
        while request:
            requested_chips = input("How many chipse would you like to buy? ")
            if not requested_chips.isdigit():
                print("Please enter an integer between 1-100.")
            elif requested_chips < 1 or requested_chips > 100:
                print("You may only buy between 1-100 chips at a time.")
            else:
                request = False
                player_list[player_index][5] += requested_chips
                print(f"Successfully updated {name}'s chip balance to {player_list[player_index][5]}")
    else:
        print(f"{name} is not found in player list.")

def display_highest_chip_holder(player_list: list[list]) -> None:
    highest_chip_index = -1
    highest_chip = 0
    index = 0

    for player in player_list:
        if player[5] > highest_chip:
            highest_chip = player[5]
            highest_chip_index = index
        elif player[5] == highest_chip:
            if player[1] < player_list[highest_chip_index][1]:
                highest_chip = player[5]
                highest_chip_index = index
            elif player[1] == player_list[highest_chip_index][1]:
                if player[6] > player_list[highest_chip_index][6]:
                    highest_chip = player[5]
                    highest_chip_index = index
                #elif player[6] ==
        index += 1
    if len(player_list) == 0:
        print("Error: There are no players in player list")
    elif highest_chip == 0:
        print("Error: Highest chip is 0.")
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
        del player_list[player_index]
        print(f"Successfully removed {name} from player list.")
    
    return player_list

def play_blackjack_games(player_list, player_pos):
    player = player_list[player_pos]

    # player[5] => Chips, player[6] => Score
    player[6], player[5] = blackjack.play_one_game(player[5])      # Returns list [score from game, number of chips]

    playing = None
    while playing != "y" or playing != "n":
        playing = input("Play again [y|n]? ")
        if playing == "y":
            play_blackjack_games(player_list, player_pos)
        elif playing == "n":
            pass
        else:
            print("Please enter 'y' or 'n'.")

# sorted [original index, games, chips, score]
def sort_by_chips(player_list: list[list]) -> list[list]:
    sorted_list = []
    index = 0
    for player in player_list:
        compare_chips(sorted_list, player, index)
        index += 1
    
    return sorted_list



def compare_chips(sorted_list: list[list], player: list, temp_index: int) -> None:
    temp_index -= 1
    if len(sorted_list) == 0:
        sorted_list.append(player)
    elif player[5] > sorted_list[temp_index][5]:
        if temp_index == 0:
            sorted_list.insert(temp_index, player)
        else:
            compare_chips(sorted_list, player, temp_index)
    else:
        sorted_list.append(player)

player_list = read_file("players.txt")

sorted_list = sort_by_chips(player_list)
print(sorted_list)

choice = None
while choice != "quit":
    print("Please enter choice")
    choice = input("[list, buy, search, high, add, remove, play, chips, quit]: ")

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
            print(f"{player[1]}  {player[2]}  {player[3]}  {player[4]}  {player[6]}", end="\n\n")
            print(f"Chips:  {player[5]}", end="\n\n\n")

    elif choice == "high":
        display_highest_chip_holder(player_list)
        print("\n")

    elif choice == "add":
        name = input("Please enter name: ")
        add_player(player_list, name)

    elif choice == "remove":
        name = input("Please enter name: ")
        remove_player(player_list, name)

    elif choice == "play":
        name = input("Please enter name: ")
        player_pos = find_player(player_list, name)
        play_blackjack_games(player_list, player_pos)

    elif choice == "chips":
        pass
    elif choice == "quit":
        write_to_file("players.txt", player_list)
        
        # Display outputted data
        for player in player_list:
            print(f"{player[0]}\n{player[1]} {player[2]} {player[3]} {player[4]} {player[5]} {player[6]}")

        print("\n\n-- Program terminating --\n")
    else:
        print("Not a valid command - please try again.")