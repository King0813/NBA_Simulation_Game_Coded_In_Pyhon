import csv
from distutils.log import error
import random
import psycopg2

####### connect to database that lists winners of the game #######

hostname = 'localhost'
database = 'GoatGameWinnersWall'
username = 'postgres'
pwd      = 'More2007'
port_id  = 5432
conn     = None
cur     =  None


 
##### script closes database if original coonnection was succesful #######

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

from csv import DictReader
import re
from turtle import pos, position
from typing import List, Dict

shooting_guard_total = 0
point_guard_total = 0
power_forward_total = 0
small_forward_total = 0
center_total = 0
player_is_valid = True
player_num_holder = []
user_first_name = ' '
user_last_initial = ' '
            

error_count = 0
position_selector_high = 20
position_selector_low = 16
team_scoring_total = 0
accumulated_remaining_funds = [15,0]
accumulated_funds_holder = 0

def show_homepage():
    print("")
    print("                               === Welcome To Goat Game ===          ")
    print(" Purpose of Game: Build A Basketball Team That Can Beat The Computers Basketball Team")
    print("                                      === Rules ===                   ")
    print("Rule 1: You have a salary cap of $15")
    print("Rule 2: Each Player has a weighted value between $1 and $5")
    print("Rule 3: When you select a player that players salary is deducted from your remaining salary cap")
    print("Rule 4: If you go over the salary cap, you automatically lose")
    print("Rule 5: If you're lucky your player can have a career game and his point total is tripled")
    print("Rule 6: If you're unlucky your player can get hurt in the game and they will score ZERO points")
    print("Rule 7: You must select each posion in the order the game prompts you to")
    
    
show_homepage()

####### invoked when user gives incorrect entry when prompted to select a player ######## 

def positonBypass(position_count, position_selector_low, position_selector_high, error_count): 

    position_count = input("Enter the player code of your shooting guard (i.e. Michael Jordan = 1): ")
    position_count = int(position_count)

    
    if position_count >= position_selector_low and position_count <= position_selector_high:
        pass 
        
    else:
        
        while error_count > 0:
            print("Error!! You must first choose a shooting guard. You have", error_count, "chances left")
            position_count = input("Enter the player code (i.e. Michael Jordan = 1): ")
            position_count = int(position_count)
            
            if position_count >= position_selector_low and position_count <= position_selector_high: 
                error_count = 0

            if position_count <= position_selector_low or position_count >= position_selector_high:
                error_count = error_count - 1
    
                if error_count == 0:
                    print("You've exceeded your attempts! Game Over")
                    quit()
    
            
########## calculates the available salary cap for user's team #############

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
         

############ calculates score for each individual player and cumluative team score         

def playerScoringCalculator(player_name, player_ppg, player_rpg, player_apg, player_rings, player_defesive_rating):


    player_num_total = [player_ppg, player_rpg, player_apg]
     
    player_num_total = sum(player_num_total)
    player_ring_multiplier = 0

    ########## calculates bonuses determined by number of championchips won

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
    
    ########## calculates bonuses determined by defensive rating 

    if player_defesive_rating > 2 and player_defesive_rating < 4: 
        player_num_total = player_num_total * 1.25
    elif player_defesive_rating > 4:
        player_num_total = player_num_total * 1.5
    


    ############### takes random nuber to determine whether or not the player
    ############### suffered a injury. There is a 7% chance of injury. Injury 
    ############### will cause player score to be zero
      
    injury_odds_start = 1
    injury_odds_end = 100
    career_high_start = 1
    career_high_end = 100
    random_number =  random.randrange(injury_odds_start,injury_odds_end)
    career_high_random_number =  random.randrange(career_high_start,career_high_end)
    
    ############### takes random nuber to determine whether or not the player
    ############### had a career game. There is a 7% chance of such a game. 
    ############### This will cause player score to triple 

    if random_number > 10 and random_number < 18:
        player_num_total = 0
        print("Unfortunately, ", player_name, "was hurt during shoot around and he is out for the remainder of the game with zero points scored")
    else:
        career_high_random_number =  random.randrange(career_high_start,career_high_end)
        if career_high_random_number > 45 and random_number < 55:
            print("Wow!!! ", player_name, "had a career high in all categories tonite his score has tripled!!")
            player_num_total = player_num_total * 3
    return player_num_total

########### called after the user selects a player for a specific position
###########  returns the remaining salary cap and the total team score    
    
def positionSelector(error_count, remaining_funds, position_selector_high, position_selector_low, team_scoring_total  , position_count, player_name, player_position, player_salary, player_ppg, player_apg, player_rings, player_defesive_rating):
        
     
    player_found_flag = False
     
    position_count = int(position_count)
    while player_found_flag is False:
        if position_count == player_code and position_count >=  position_selector_low and position_count <= position_selector_high:
            player_salary = int(player_salary)
            currency = 0
            currency = int(currency)
            print('You drafted', player_name, 'as your', player_position)
             
            player_found_flag = 'Y'
            currency = remainingFundsFunction(team_scoring_total, player_found_flag, remaining_funds, player_salary)
             
            if currency is None:
                pass
            else:
                funds_remaining = "${:,.2f}".format(currency)
             
            player_scoring_total = playerScoringCalculator(player_name, player_ppg, player_rpg, player_apg, player_rings, player_defesive_rating)
            team_scoring_total = team_scoring_total + player_scoring_total
            if currency is None:
                return 0,0
            else:
                
                return int(currency), int(team_scoring_total)
        break        
            
####### for each respective positon the user selects their respective player       
        

######### Shooting Guard Selection #########
 
file_handle =  open("playerdatabase.csv", "r", encoding="utf8")
csv_reader = DictReader(file_handle)
table: List[Dict[str,float]] = []
position_selector_low = 1
position_selector_high = 5
remaining_funds = 15
computer_pick = 0
computer_team_scoring_total = 0
computer_player_scoring_total = 0
computer_remaining_funds = 15
position_count = 0

error_count = 3


####### builds table from csv file 

for row in csv_reader:
    float_row: Dict[str, float] = {}
    for column in row:
        float_row[column] = str(row[column])
    table.append(float_row)
    

 
player_name: str = ' '
print('                                ')
print('#################################################################')
print("######## First You Will Select A Shooting Guard #################")
print("### Michael Jordan's salary is: " , '$5 and his player code is: 1 ###')
print("### Kobe Bryant's salary is:    " , '$4 and his player code is: 2 ###')
print("### Allen Iverson's salary is:  " , '$3 and his player code is: 3 ###')
print("### Elgin Baylor's salary is:   " , '$2 and his player code is: 4 ###')
print("### Dwaye Wade's salary is:     " , '$1 and his player code is: 5 ###')
print('#################################################################')
 

positon_count = positonBypass(position_count, position_selector_low, position_selector_high, error_count)


position_count = int(position_count)

####### determines who the computer will draft based on who the user drafts


if position_count == 1:
    computer_pick = 2
    computer_remaining_funds = computer_remaining_funds - 4
    print('The computer has drafted', player_name)
else:
    computer_pick = 1
    computer_remaining_funds = computer_remaining_funds - 5
    print('The computer has drafted', player_name)

 
player_scoring_total = 0

########## iterates through table to define values for respective variables 
##########  while calling functions that tabulate user and computer scores

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
     
    if player_code == computer_pick:
        computer_player_scoring_total = playerScoringCalculator(player_name, player_ppg, player_rpg, player_apg, player_rings, player_defesive_rating)
        computer_team_scoring_total = computer_team_scoring_total + computer_player_scoring_total

        print(player_name, "has scored: ", computer_player_scoring_total, "for the computer")
        print("The computer has scored: ", computer_team_scoring_total, "total team points")
        print("The computer has ", computer_remaining_funds, "remaining in its salary cap")
        
    error_count += 1
    accumulated_remaining_funds = positionSelector(error_count, remaining_funds, position_selector_high, position_selector_low, team_scoring_total, position_count, player_name, player_position, player_salary, player_ppg, player_apg, player_rings, player_defesive_rating)
    
    if accumulated_remaining_funds is None:
         
        pass
    else:
 
        remaining_funds = accumulated_remaining_funds[0]
        accumulated_funds_holder = accumulated_remaining_funds[1]
        print(player_name, "scored: ", accumulated_remaining_funds[1])
        print("Team scoring total is: ", accumulated_funds_holder)
        print("You have ", remaining_funds, "remaining")
  
file_handle.close()     


########### Power Forward ###################

error_count = 0
file_handle =  open("playerdatabase.csv", "r", encoding="utf8")
csv_reader = DictReader(file_handle)
table: List[Dict[str,float]] = []
computer_pick = 0
position_count = 0
position_selector_low = 6
position_selector_high = 10
error_count = 3


####### builds table from csv file     

for row in csv_reader:
    float_row: Dict[str, float] = {}
    for column in row:
        float_row[column] = str(row[column])
    table.append(float_row)
    
 
player_name: str = ' '
print("----------------Next You Will Select A Power Forward --------------------------")
print("Tim Duncan's salary is:              " , '$5 and his player code is: 6')
print("Giannas Atentukumpo's salary is:     " , '$4 and his player code is: 7')
print("Charles Barkley's salary is:         " , '$3 and his player code is: 8')
print("Karl Malone's salary is:             " , '$2 and his player code is: 9')
print("Kevin Garnett's salary is:           " , '$1 and his player code is: 10')
 

positon_count = positonBypass(position_count, position_selector_low, position_selector_high, error_count)

position_count = int(position_count)
if position_count == 6:
    computer_pick = 7
    computer_remaining_funds = computer_remaining_funds - 4
     
else:
    computer_pick = 6
    computer_remaining_funds = computer_remaining_funds - 5

 
computer_player_found_flag = 'N'

position_count = int(position_count)
print("position count type in forward", type(position_count))

########## iterates through table to define values for respective variables 
##########  while calling functions that tabulate user and computer scores


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
    
    if player_code == computer_pick:
        computer_player_scoring_total = playerScoringCalculator(player_name, player_ppg, player_rpg, player_apg, player_rings, player_defesive_rating)
        computer_team_scoring_total = computer_team_scoring_total + computer_player_scoring_total
        print("The computer has drafted ", player_name)
        print(player_name, "has scored: ", computer_player_scoring_total, "for the computer")
        print("The computer has scored: ", computer_team_scoring_total, "total team points")
        print("The computer has ", computer_remaining_funds, "remaining in its salary cap")
     
     

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
     
file_handle.close()      

################# Small Forward ###############

error_count = 0
file_handle =  open("playerdatabase.csv", "r", encoding="utf8")
csv_reader = DictReader(file_handle)
table: List[Dict[str,float]] = []
computer_pick = 0
position_count = 0
error_count = 3
position_selector_low = 11
position_selector_high = 15
 
######## builds table from csv file 

for row in csv_reader:
    float_row: Dict[str, float] = {}
    for column in row:
        float_row[column] = str(row[column])
    table.append(float_row)
    

player_name: str = ' '
print("---------------- Next You Will Select A Small Forward --------------------------")
print("Lebron James's salary is:         " , '$5 and his player code is: 11')
print("Kevin Durant's salary is:         " , '$4 and his player code is: 12')
print("Larry Bird's salary is:           " , '$3 and his player code is: 13')
print("Scottie Pippen's salary is:       " , '$2 and his player code is: 14')
print("James Worthy's salary is:         " , '$1 and his player code is: 15')
positon_count = positonBypass(position_count, position_selector_low, position_selector_high, error_count)

position_count = int(position_count)
if position_count == 14:
    computer_pick = 15
    computer_remaining_funds = computer_remaining_funds - 1
     
else:
    computer_pick = 14
    computer_remaining_funds = computer_remaining_funds - 2

player_scoring_total = 0

########## iterates through table and assigns value to respective variables
############# calculates player totals and team totals

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

     

    if player_code == computer_pick:
        computer_player_scoring_total = playerScoringCalculator(player_name, player_ppg, player_rpg, player_apg, player_rings, player_defesive_rating)
        computer_team_scoring_total = computer_team_scoring_total + computer_player_scoring_total
        print(player_name, "has scored: ", computer_player_scoring_total, "for the computer")
        print("The computer has scored: ", computer_team_scoring_total, "total team points")
        print("The computer has ", computer_remaining_funds, "remaining in its salary cap")


    accumulated_remaining_funds = positionSelector(error_count, remaining_funds, position_selector_high, position_selector_low, team_scoring_total, position_count, player_name, player_position, player_salary, player_ppg, player_apg, player_rings, player_defesive_rating)
   
    
    if accumulated_remaining_funds is None:
        pass
    else:
        remaining_funds = accumulated_remaining_funds[0]
        accumulated_funds_holder =  accumulated_funds_holder + accumulated_remaining_funds[1]

        print(player_name, "scored: ", accumulated_remaining_funds[1]) 
        print("You have ", remaining_funds, " left to spend")
        print("total team points ", accumulated_funds_holder)

file_handle.close()      
     
################# Center ###############

file_handle =  open("playerdatabase.csv", "r", encoding="utf8")
csv_reader = DictReader(file_handle)
table: List[Dict[str,float]] = []
position_selector_low = 16
position_selector_high = 20
error_count = 3
computer_pick = 0
position_count = 0

############# builds table from csv file

for row in csv_reader:
    float_row: Dict[str, float] = {}
    for column in row:
        float_row[column] = str(row[column])
    table.append(float_row)
    
    

player_name: str = ' '
print("----------------Next You Will Select A Center --------------------------")
print("Kareem Abdul-Jabar's salary is:         " , '$5 and his player code is: 16')
print("Wilt Chamberlin's salary is:            " , '$4 and his player code is: 17')
print("Shaquille ONeal's salary is:            " , '$3 and his player code is: 18')
print("Bill Russell's salary is:               " , '$2 and his player code is: 19')
print("Hakeem Olajuwon's salary is:            " , '$1 and his player code is: 20')
positon_count = positonBypass(position_count, position_selector_low, position_selector_high, error_count)

position_count = int(position_count)
if position_count == 19:
    computer_pick = 20
    computer_remaining_funds = computer_remaining_funds - 1
     
else:
    computer_pick = 19
    computer_remaining_funds = computer_remaining_funds - 2


player_scoring_total = 0

############# iterates through table to assign values to variables
############# calculates player totals and team totals

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

    if player_code == computer_pick:
        computer_player_scoring_total = playerScoringCalculator(player_name, player_ppg, player_rpg, player_apg, player_rings, player_defesive_rating)
        computer_team_scoring_total = computer_team_scoring_total + computer_player_scoring_total
        print(player_name, "has scored: ", computer_player_scoring_total, "for the computer")
        print("The computer has scored: ", computer_team_scoring_total, "total team points")
        print("The computer has ", computer_remaining_funds, "remaining in its salary cap")
  
     

    accumulated_remaining_funds = positionSelector(error_count, remaining_funds, position_selector_high, position_selector_low, team_scoring_total, position_count, player_name, player_position, player_salary, player_ppg, player_apg, player_rings, player_defesive_rating)
    
    if accumulated_remaining_funds is None:
        pass
    else:
         
        remaining_funds = accumulated_remaining_funds[0]
        print(accumulated_remaining_funds)
        accumulated_funds_holder =  accumulated_funds_holder + accumulated_remaining_funds[1]

        print(player_name, "scored: ", accumulated_remaining_funds[1]) 
        print("You have ", remaining_funds, " left to spend")
        print("total team points ", accumulated_funds_holder)
     
file_handle.close()      
     


     
################# Point Guard ###############

file_handle =  open("playerdatabase.csv", "r", encoding="utf8")
csv_reader = DictReader(file_handle)
table: List[Dict[str,float]] = []
position_selector_low = 16
position_selector_high = 20
error_count = 3
position_count = 0
computer_pick = 0

########### builds table from csv file

for row in csv_reader:
    float_row: Dict[str, float] = {}
    for column in row:
        float_row[column] = str(row[column])
    table.append(float_row)
    

 
player_name: str = ' '

 
print("----------------FINALY You Will Select A Point Guard --------------------------")
print("Magic Johnson's salary is:         " , '$5 and his player code is: 21')
print("Steph Curry's salary is:           " , '$4 and his player code is: 22')
print("Isiah Thomas's salary is:          " , '$3 and his player code is: 23')
print("John Stockton's salary is:         " , '$2 and his player code is: 24')
print("Trey Young's salary is:            " , '$1 and his player code is: 25')
positon_count = positonBypass(position_count, position_selector_low, position_selector_high, error_count)

position_count = int(position_count)
if position_count == 24:
    computer_pick = 25
    computer_remaining_funds = computer_remaining_funds - 1
     
else:
    computer_pick = 24
    computer_remaining_funds = computer_remaining_funds - 2

player_scoring_total = 0

############# iterates through table to assign values to variables
############# calculates player totals and team totals


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
     
    if player_code == computer_pick:
            computer_player_scoring_total = playerScoringCalculator(player_name, player_ppg, player_rpg, player_apg, player_rings, player_defesive_rating)
            computer_team_scoring_total = computer_team_scoring_total + computer_player_scoring_total
            print(player_name, "has scored: ", computer_player_scoring_total, "for the computer")
            print("The computer has scored: ", computer_team_scoring_total, "total team points")
            print("The computer has ", computer_remaining_funds, "remaining in its salary cap")
  

     
    accumulated_remaining_funds = positionSelector(error_count, remaining_funds, position_selector_high, position_selector_low, team_scoring_total, position_count, player_name, player_position, player_salary, player_ppg, player_apg, player_rings, player_defesive_rating)
    
    if accumulated_remaining_funds is None:
        pass
    else:
         
        remaining_funds = accumulated_remaining_funds[0]
         
        accumulated_funds_holder =  accumulated_funds_holder + accumulated_remaining_funds[1]

        print(player_name, "scored: ", accumulated_remaining_funds[1]) 
        print("You have ", remaining_funds, " left to spend")
        print("total team points ", accumulated_funds_holder)

    if accumulated_funds_holder > computer_team_scoring_total and remaining_funds >= 0:
        print("Congratulations You Beat The Computer!! You are the GOAT!!")
        user_flag = input("Would you like to be added to the Wall of Winners? (Y/N)")
        if user_flag == "Y":
            user_first_name = input("Please enter your first name: ")
            user_last_initial = input("Please enter the initial of your last name")

    elif accumulated_funds_holder < computer_team_scoring_total:
        print("Unfortunately you lost. The computer is the GOAT")
    elif accumulated_funds_holder == computer_team_scoring_total and remaining_funds >= 0:
        print("Tie Game")

    
file_handle.close()      

###### Allows user to bypass script when invallid database credentials 
###### are entered and script can't connect to database 


try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database, 
        user = username,  
        password = pwd,
        port = port_id)
    
    cur = conn.cursor()

    create_script = ''' CREATE TABLE IF NOT EXISTS player (
                            rank            int,
                            player_id       int PRIMARY KEY,
                            first_name      varchar (40),
                            last_initial    varchar (40),
                            score           int) '''
    cur.execute(create_script)

    # insert_script = 'INSERT INTO player (rank, player_id, first_name, last_initial, score) VALUES (%s, %s, %s, %s)'

    # insert_values = (rank, player_id, first_name, last_name_initial, player_total_score)
    # for record in insert_values:
    #     cur.execute(insert_script, record)

    conn.execute = (insert_script, insert_value)


    conn.commit()
    
    
except Exception as error:
    print(error)

