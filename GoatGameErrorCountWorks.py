import csv
from distutils.log import error
import random

from csv import DictReader
import re
from turtle import pos, position
from typing import List, Dict

shooting_guard_total = 0
point_guard_total = 0
power_forward_total = 0
small_forward_total = 0
center_total = 0
player_num_holder = []

error_count = 0
print("error count beginning: ", error_count)
position_selector_high = 0
position_selector_low = 0
team_scoring_total = 0
accumulated_remaining_funds = [15,0]
accumulated_funds_holder = 0


def remainingFundsFunction(accumulated_funds_holder, player_found_flag, remaining_funds, player_salary):

    
    
    #print("rfffff", accumulated_funds_holder, remaining_funds, player_salary)
    if player_found_flag == 'Y':
        #if accumulated_funds_holder is not None:
        #print(type(accumulated_funds_holder), type(accumulated_remaining_funds), type(player_salary))
        accumulated_funds_holder = remaining_funds - player_salary
        if accumulated_funds_holder < 0:
            print("Eroor: You went over your salary cap. Automatic Loss!!")
            quit()
        else:
            return int(accumulated_funds_holder)
         

        

def playerScoringCalculator(player_name, player_ppg, player_rpg, player_apg, player_rings, player_defesive_rating):


    player_num_total = [player_ppg, player_rpg, player_apg]
     
    player_num_total = sum(player_num_total)
    player_ring_multiplier = 0
    if player_rings == 1:
        player_ring_multiplier = player_rings * 1.5
        player_num_total = player_num_total * player_ring_multiplier
    elif player_rings > 1 and player_rings <= 4:
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
    
def positionSelector(error_count, remaining_funds, position_selector_high, position_selector_low, team_scoring_total  , position_count, player_name, player_position, player_salary, player_ppg, player_apg, player_rings, player_defesive_rating):
        
    #error_count = 0
    #print("we made it", remaining_funds)

    #print("salary cap in function: ", remaining_funds)    
    player_found_flag = False
    #print("cound, low, high", position_count, position_selector_low, position_selector_high)   
    #print(type(position_count), type(position_selector_low), type(position_selector_high)) 
    position_count = int(position_count)
    while player_found_flag is False:
        if position_count == player_code and position_count >=  position_selector_low and position_count <= position_selector_high:
            player_salary = int(player_salary)
            currency = 0
            currency = int(currency)
            print('You drafted', player_name, 'as your', player_position)
            #print(type(currency), type(player_salary))
            #print("fund in function", remaining_funds, player_salary)
            player_found_flag = 'Y'
            currency = remainingFundsFunction(team_scoring_total, player_found_flag, remaining_funds, player_salary)
            #print("currency, fund_after_function: ",  currency, remaining_funds, player_salary)
            if currency is None:
                pass
            else:
                funds_remaining = "${:,.2f}".format(currency)
            #print('You have', funds_remaining, 'left in your salary cap')
            player_scoring_total = playerScoringCalculator(player_name, player_ppg, player_rpg, player_apg, player_rings, player_defesive_rating)
            #print(player_name, player_ppg, player_rpg, player_apg, player_rings, player_defesive_rating)
            #print("team scoring total before: ", team_scoring_total)
            team_scoring_total = team_scoring_total + player_scoring_total
            #print("player scoring after ", player_scoring_total)
            #print("team scoring total before: ", team_scoring_total)
             
            #print("player score: ", player_scoring_total)
            if currency is None:
                return 0,0
            else:
                #print("team scoring total before return statemnt", team_scoring_total)
                return int(currency), int(team_scoring_total)
            
            
        
        elif position_count < position_selector_low or position_count > position_selector_high:
            if error_count <= 2:
                print("Error!! You must first choose a", player_position)
                position_count = input("Enter the player code (i.e. Michael Jordan = 1): ")
                position_count = int(position_count)
                print("error count before is ", error_count)
                error_count += 1
                print("error count  after is ", error_count)
            if error_count >= 3:
                print("You've exceeded your attempts! Game Over")
                quit()
                return 0,0
                break
        break


######### Shooting Guard Selection #########
 
file_handle =  open("playerdatabase.csv", "r", encoding="utf8")
csv_reader = DictReader(file_handle)
table: List[Dict[str,float]] = []
position_selector_low = 1
position_selector_high = 5
remaining_funds = 15
#error_count = 0

for row in csv_reader:
    float_row: Dict[str, float] = {}
    for column in row:
        float_row[column] = str(row[column])
    table.append(float_row)
    

# player_code,name,position,salary,ppg,rpg,apg,rings,defensiveranking
player_name: str = ' '
position_count = input("Enter the player code of your shooting guard (i.e. Michael Jordan = 1): ")
player_scoring_total = 0
#team_scoring_total = 0
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
     
    #position_count = int(position_count)
    #print(row)
    #remaining_funds = int(remaining_funds)
    #print("remaining funds ", remaining_funds, type(remaining_funds))
    #positionSelector(remaining_funds, position_selector_high, position_selector_low, team_scoring_total, position_count, player_name, player_position, player_salary, player_ppg, player_apg, player_rings, player_defesive_rating)
    #print("answer funds total: ", accumulated_remaining_funds)
    #accumulated_remaining_funds = positionSelector(remaining_funds, position_selector_high, position_selector_low, accumulated_remaining_funds[1], position_count, player_name, player_position, player_salary, player_ppg, player_apg, player_rings, player_defesive_rating)
    
    #print("none is ", accumulated_remaining_funds)
    #print("none is ", type(accumulated_remaining_funds))
    #accumulated_remaining_funds[0] = int(accumulated_remaining_funds[0])
    #res = tuple(int(num) for num in accumulated_remaining_funds('(', '').replace(')', '').replace('...', '').split(', '))
  
    #print(accumulated_remaining_funds[0], type(accumulated_remaining_funds[0]))
    #print(accumulated_remaining_funds[1], type(accumulated_remaining_funds[1]))
    #print(type(remaining_funds))
    #print("error count shooting guard: ", error_count)
    error_count += 1
    accumulated_remaining_funds = positionSelector(error_count, remaining_funds, position_selector_high, position_selector_low, team_scoring_total, position_count, player_name, player_position, player_salary, player_ppg, player_apg, player_rings, player_defesive_rating)
   # res = tuple(int(num) for num in accumulated_remaining_funds('(', '').replace(')', '').replace('...', '').split(', '))

    
    #print("arf 186: ", type(accumulated_remaining_funds))
    if accumulated_remaining_funds is None:
         
        pass
    else:
        #accumulated_remaining_funds = positionSelector(remaining_funds, position_selector_high, position_selector_low, accumulated_remaining_funds[1], position_count, player_name, player_position, player_salary, player_ppg, player_apg, player_rings, player_defesive_rating)

        remaining_funds = accumulated_remaining_funds[0]
        accumulated_funds_holder = accumulated_remaining_funds[1]
        print(player_name, "scored: ", accumulated_remaining_funds[1])
        print("Team scoring total is: ", accumulated_funds_holder)
        print("You have ", remaining_funds, "remaining")
    # if accumulated_remaining_funds != 0:
    #     pass
    # else:
    #     print("we are here")
    #     print("accumulated remaining funds", accumulated_remaining_funds, type(accumulated_remaining_funds))
    #     accumulated_remaining_funds = int(accumulated_remaining_funds)    
    #     remaining_funds = accumulated_remaining_funds
file_handle.close()     


########### Power Forward ###################

#print("remaining funds at start of function", remaining_funds)
error_count = 0
file_handle =  open("playerdatabase.csv", "r", encoding="utf8")
csv_reader = DictReader(file_handle)
table: List[Dict[str,float]] = []
#print("team score right now: ", team_scoring_total)

for row in csv_reader:
    float_row: Dict[str, float] = {}
    for column in row:
        float_row[column] = str(row[column])
    table.append(float_row)
    

# player_code,name,position,salary,ppg,rpg,apg,rings,defensiveranking
player_name: str = ' '
position_count = input("Enter the player code of your shooting guard (i.e. Tim Duncan = 6): ")
player_scoring_total = 0
position_selector_low = 6
position_selector_high = 10
#team_scoring_total = 0



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

    #remaining_funds = int(remaining_funds) 
    #position_count = int(position_count)
    #print(row)
    #print(player_code, type(player_code))

    #print("remaining funds power forward: ", remaining_funds)
    #print("team salary: ", player_name, player_salary)

    accumulated_remaining_funds = positionSelector(error_count, remaining_funds, position_selector_high, position_selector_low, team_scoring_total, position_count, player_name, player_position, player_salary, player_ppg, player_apg, player_rings, player_defesive_rating)
    
    if accumulated_remaining_funds is None:
        pass
    else:
        print("answer: ", accumulated_remaining_funds)
        remaining_funds = accumulated_remaining_funds[0]
        #print(accumulated_remaining_funds)
        accumulated_funds_holder =  accumulated_funds_holder + accumulated_remaining_funds[1]

        print(player_name, "scored: ", accumulated_remaining_funds[1]) 
        print("You have ", remaining_funds, " left to spend")
        print("total team points ", accumulated_funds_holder)
    #positionSelector(remaining_funds, position_selector_high, position_selector_low, team_scoring_total, position_count, player_name, player_position, player_salary, player_ppg, player_apg, player_rings, player_defesive_rating)
    
    # accumulated_remaining_funds = positionSelector(remaining_funds, position_selector_high, position_selector_low, team_scoring_total, position_count, player_name, player_position, player_salary, player_ppg, player_apg, player_rings, player_defesive_rating)
    # if accumulated_remaining_funds != 0:
    #     pass
    # else:
    #     print("we are here")
    #     print("accumulated remaining funds", accumulated_remaining_funds, type(accumulated_remaining_funds))
    #     accumulated_remaining_funds = int(accumulated_remaining_funds)    
    #     remaining_funds = accumulated_remaining_funds

file_handle.close()      

################# Small Forward ###############

error_count = 0
file_handle =  open("playerdatabase.csv", "r", encoding="utf8")
csv_reader = DictReader(file_handle)
table: List[Dict[str,float]] = []
position_selector_low = 11
position_selector_high = 15
 

for row in csv_reader:
    float_row: Dict[str, float] = {}
    for column in row:
        float_row[column] = str(row[column])
    table.append(float_row)
    

# player_code,name,position,salary,ppg,rpg,apg,rings,defensiveranking
player_name: str = ' '
position_count = input("Enter the player code of your shooting guard (i.e. Lebron James = 11): ")
player_scoring_total = 0
#team_scoring_total = 0
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
     
    #position_count = int(position_count)
    #print(row)
    #print(player_code, type(player_code))

    accumulated_remaining_funds = positionSelector(error_count, remaining_funds, position_selector_high, position_selector_low, team_scoring_total, position_count, player_name, player_position, player_salary, player_ppg, player_apg, player_rings, player_defesive_rating)
   
    
    if accumulated_remaining_funds is None:
        pass
    else:
        print("answer: ", accumulated_remaining_funds)
        remaining_funds = accumulated_remaining_funds[0]
        #print(accumulated_remaining_funds)
        accumulated_funds_holder =  accumulated_funds_holder + accumulated_remaining_funds[1]

        print(player_name, "scored: ", accumulated_remaining_funds[1]) 
        print("You have ", remaining_funds, " left to spend")
        print("total team points ", accumulated_funds_holder)
    # accumulated_remaining_funds = positionSelector(remaining_funds, position_selector_high, position_selector_low, team_scoring_total, position_count, player_name, player_position, player_salary, player_ppg, player_apg, player_rings, player_defesive_rating)
    # if accumulated_remaining_funds != 0:
    #     pass
    # else:
    #     print("we are here")
    #     print("accumulated remaining funds", accumulated_remaining_funds, type(accumulated_remaining_funds))
    #     accumulated_remaining_funds = int(accumulated_remaining_funds)    
    #     remaining_funds = accumulated_remaining_funds

file_handle.close()      
     
################# Center ###############

file_handle =  open("playerdatabase.csv", "r", encoding="utf8")
csv_reader = DictReader(file_handle)
table: List[Dict[str,float]] = []
position_selector_low = 16
position_selector_high = 20
error_count = 0


for row in csv_reader:
    float_row: Dict[str, float] = {}
    for column in row:
        float_row[column] = str(row[column])
    table.append(float_row)
    

# player_code,name,position,salary,ppg,rpg,apg,rings,defensiveranking
player_name: str = ' '
position_count = input("Enter the player code of your shooting guard (i.e. Kareem Abdul Jabar = 16): ")
player_scoring_total = 0
#team_scoring_total = 0
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
     
    #position_count = int(position_count)
    #print(row)
    #print(player_code, type(player_code))

    accumulated_remaining_funds = positionSelector(error_count, remaining_funds, position_selector_high, position_selector_low, team_scoring_total, position_count, player_name, player_position, player_salary, player_ppg, player_apg, player_rings, player_defesive_rating)
    
    if accumulated_remaining_funds is None:
        pass
    else:
        print("answer: ", accumulated_remaining_funds)
        remaining_funds = accumulated_remaining_funds[0]
        print(accumulated_remaining_funds)
        accumulated_funds_holder =  accumulated_funds_holder + accumulated_remaining_funds[1]

        print(player_name, "scored: ", accumulated_remaining_funds[1]) 
        print("You have ", remaining_funds, " left to spend")
        print("total team points ", accumulated_funds_holder)
    # accumulated_remaining_funds = positionSelector(remaining_funds, position_selector_high, position_selector_low, team_scoring_total, position_count, player_name, player_position, player_salary, player_ppg, player_apg, player_rings, player_defesive_rating)
    # if accumulated_remaining_funds != 0:
    #     pass
    # else:
    #     print("we are here")
    #     print("accumulated remaining funds", accumulated_remaining_funds, type(accumulated_remaining_funds))
    #     accumulated_remaining_funds = int(accumulated_remaining_funds)    
    #     remaining_funds = accumulated_remaining_funds

file_handle.close()      
     


     
################# Point Guard ###############

file_handle =  open("playerdatabase.csv", "r", encoding="utf8")
csv_reader = DictReader(file_handle)
table: List[Dict[str,float]] = []
position_selector_low = 21
position_selector_high = 25
error_count = 0


for row in csv_reader:
    float_row: Dict[str, float] = {}
    for column in row:
        float_row[column] = str(row[column])
    table.append(float_row)
    

# player_code,name,position,salary,ppg,rpg,apg,rings,defensiveranking
player_name: str = ' '
position_count = input("Enter the player code of your shooting guard (i.e. Magic Johnson = 22): ")
player_scoring_total = 0
#team_scoring_total = 0
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
    #print(row)
    #print(player_code, type(player_code))

    accumulated_remaining_funds = positionSelector(error_count, remaining_funds, position_selector_high, position_selector_low, team_scoring_total, position_count, player_name, player_position, player_salary, player_ppg, player_apg, player_rings, player_defesive_rating)
    
    if accumulated_remaining_funds is None:
        pass
    else:
        #print("answer: ", accumulated_remaining_funds)
        remaining_funds = accumulated_remaining_funds[0]
        #print(accumulated_remaining_funds)
        accumulated_funds_holder =  accumulated_funds_holder + accumulated_remaining_funds[1]

        print(player_name, "scored: ", accumulated_remaining_funds[1]) 
        print("You have ", remaining_funds, " left to spend")
        print("total team points ", accumulated_funds_holder)

    # accumulated_remaining_funds = positionSelector(remaining_funds, position_selector_high, position_selector_low, team_scoring_total, position_count, player_name, player_position, player_salary, player_ppg, player_apg, player_rings, player_defesive_rating)
    # if accumulated_remaining_funds != 0:
    #     pass
    # else:
    #     print("we are here")
    #     print("accumulated remaining funds", accumulated_remaining_funds, type(accumulated_remaining_funds))
    #     accumulated_remaining_funds = int(accumulated_remaining_funds)    
    #     remaining_funds = accumulated_remaining_funds
file_handle.close()      
     


    

    
    
    



    

    
    
    
