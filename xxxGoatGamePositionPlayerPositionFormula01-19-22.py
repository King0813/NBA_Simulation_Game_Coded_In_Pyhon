import csv
import random

from csv import DictReader
from turtle import pos, position
from typing import List, Dict

shooting_guard_total = 0
point_guard_total = 0
power_forward_total = 0
small_forward_total = 0
center_total = 0
player_num_holder = []
team_scoring_total = 0
error_count = 0




def playerScoringCalculator(player_name, player_ppg, player_rpg, player_apg, player_rings, player_defesive_rating):


    player_num_total = [player_ppg, player_rpg, player_apg]
     
    player_num_total = sum(player_num_total)
    player_ring_multiplier = 0
    if player_rings == 1:
        player_ring_multiplier = player_rings * 1.5
        player_num_total = player_num_total * player_ring_multiplier
    elif player_rings > 1 and player_rings < 4:
        player_ring_multiplier = player_rings * 2.5
        player_num_total = player_num_total * player_ring_multiplier
    elif player_rings >= 5 and player_rings < 7:
        player_ring_multiplier = player_rings * 3.5
        player_num_total = player_num_total * player_ring_multiplier
    elif player_rings >= 7:
        player_ring_multiplier = player_rings * 4.5
        player_num_total = player_num_total * player_ring_multiplier
    
    if player_defesive_rating > 2 and player_defesive_rating < 4: 
        player_num_total = player_num_total * 1.25
    elif player_defesive_rating > 4:
        player_num_total = player_num_total * 1.5
    
    injury_odds_start = 1
    injury_odds_end = 100
    career_high_start = 1
    career_high_end = 100
    random_number =  random.randrange(injury_odds_start,injury_odds_end)
    career_high_random_number =  random.randrange(career_high_start,career_high_end)
    if random_number > 10 and random_number < 18:
        player_num_total = 0
        print("Unfortunately, ", player_name, "was hurt during shoot around and he is out for the remainder of the game with zero points scored")
    else:
        career_high_random_number =  random.randrange(career_high_start,career_high_end)
        if career_high_random_number > 45 and random_number < 55:
            print("Wow!!! ", player_name, "had a career high in all categories tonite his score has tripled!!")
            player_num_total = player_num_total * 3
    return player_num_total
    


file_handle =  open("playerdatabase.csv", "r", encoding="utf8")
csv_reader = DictReader(file_handle)
table: List[Dict[str,float]] = []

for row in csv_reader:
    float_row: Dict[str, float] = {}
    for column in row:
        float_row[column] = str(row[column])
    table.append(float_row)
    

# player_code,name,position,salary,ppg,rpg,apg,rings,defensiveranking
player_name: str = ' '
position_count = input("Enter the player code of your shooting guard (i.e. Michael Jordan = 1): ")
player_scoring_total = 0
team_scoring_total = 0
for row in table:
    
    player_name = row["name"]
    player_code = int(row["player_code"])
    
    
    player_position = row["position"]
    player_salary = int(row["salary"])
    player_ppg = float(row["ppg"])
    player_rpg = float(row["rpg"])
    player_apg = float(row["apg"])
    player_rings = float(row["rings"])
    player_defesive_rating = float(row["defensiveranking"])
     
    position_count = int(position_count)
    print(row)

    def positionSelector(position_selection_variable, player_name, player_position, player_salary, ):
        pass

    if position_count == player_code and position_count >= 1 and position_count < 6:
        print('You drafted', player_name, 'as your', player_position)
        remainingFunds = 15 - player_salary
        currency = "${:,.2f}".format(remainingFunds)
        print('You have', currency, 'left in your salary cap')
        player_scoring_total = playerScoringCalculator(player_name, player_ppg, player_rpg, player_apg, player_rings, player_defesive_rating)
        print(player_name, player_ppg, player_rpg, player_apg, player_rings, player_defesive_rating)
        team_scoring_total = team_scoring_total + player_scoring_total
        print("team scoring ", team_scoring_total)
    
        print("player score: ", player_scoring_total)


    elif position_count != 0 and position_count > 5:
        while error_count < 3:
            print("Error!! You must first choose a shooting guard")
            position_count = input("Enter the player code of your shooting guard (i.e. Michael Jordan = 1): ")
            error_count += 1
        if error_count >= 3:
            print("You've exceeded your attempts! Game Over")
            break

file_handle.close()      


file_handle2 =  open("playerdatabase2.csv", "r", encoding="utf8")
csv_reader2 = DictReader(file_handle2)
table2: List[Dict[str,float]] = []


for row2 in csv_reader2:
    float_row2: Dict[str, float] = {}
    for column in row2:
        float_row2[column] = str(row2[column])
    table2.append(float_row2)


position_count = input("Enter the player code of your shooting guard (i.e. Tim Duncan = 6): ")
position_count = int(position_count)
print(position_count)

for row2 in table2:
    
    player_name = row2["name"]
    player_code = int(row2["player_code"])
    
    
    player_position = row2["position"]
    player_salary = int(row2["salary"])
    player_ppg = float(row2["ppg"])
    player_rpg = float(row2["rpg"])
    player_apg = float(row2["apg"])
    player_rings = float(row2["rings"])
    player_defesive_rating = float(row2["defensiveranking"])
    print(row2)

    if position_count == player_code and position_count >= 6 and position_count < 11:
        print('You drafted', player_name, 'as your', player_position)
        remainingFunds = 15 - player_salary
        currency = "${:,.2f}".format(remainingFunds)
        print('You have', currency, 'left in your salary cap')
        player_scoring_total = playerScoringCalculator(player_name, player_ppg, player_rpg, player_apg, player_rings, player_defesive_rating)
        print(player_name, player_ppg, player_rpg, player_apg, player_rings, player_defesive_rating)
        team_scoring_total = team_scoring_total + player_scoring_total
        print("team scoring ", team_scoring_total)
    
        print("player score: ", player_scoring_total)


    elif position_count != 0 and position_count >= 6 and position_count < 11:
        while error_count < 3:
            print("Error!! You must first choose a power forward")
            position_count = input("Enter the player code of your power forward (i.e. Tim Duncan = 6): ")
            error_count += 1
        if error_count >= 3:
            print("You've exceeded your attempts! Game Over")
            break
        


file_handle2.close()      
            
    



    

    
    
    
