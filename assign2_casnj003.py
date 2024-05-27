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
        for info in player:
            outfile.write(f"{info[0]}\n{info[1]} {info[2]} {info[3]} {info[4]} {info[5]} {info[6]}")

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
            ##########################
            # WHAT HAPPENS IF EQUAL? #
            ##########################
        index += 1
    if len(player_list) == 0:
        print("Error: There are no players in player_list")
    elif highest_chip == 0:
        print("Error: Highest chip is 0.")
    else:
        print(f"Highest Chip Holder => {player_list[highest_chip_index][0]} with {highest_chip} chips!")

def add_player(player_list: list[list], name: str) -> list[list]:
    if name == (player[0] for player in player_list):
        print(f"{name} already exists in player list.")
        
    return player_list

player_list = read_file("players.txt")
display_players(player_list)
print(f"Player Found: {find_player(player_list, "Johnny Rose")}")