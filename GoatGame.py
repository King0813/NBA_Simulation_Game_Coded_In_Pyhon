from csv import DictReader
from typing import List, Dict

shootingGuard5 = 'Michael Jordan'
shootingGuard4 = 'Kobe Bryant'
shootingGuard3 = 'Allen Iverson'
shootingGuard2 = 'Dwayne Wade'
shootingGuard1 = 'Elgin Baylor'

powerForward5 = 'Tim Duncan'
powerForward4 = 'Giannas Atentukumpo'
powerForward3 = 'Charles Barkley'
powerForward2 = 'Karl Malone'
powerForward1 = 'Kevin Garnett'


smallForward5 = 'Lebron James'
smallForward4 = 'Kevin Durant'
smallForward3 = 'Larry Bird'
smallForward2 = 'Scottie Pippen'
smallForward1 = 'James Worthy'

center5 = 'Kareem Abdul-Jabar'
center4 = 'Wilt Chamberlin'
center3 = 'Shaquille ONeal'
center2 = 'Bill Russell'
center1 = 'Hakeem Olajuwon'

pointGuard5 = 'Magic Johnson'
pointGuard4 = 'Steph Curry'
pointGuard3 = 'Isiah Thomas'
pointGuard2 = 'John Stockton'
pointGuard1 = 'Trey Young'

remainingFunds = 15
salaryCap = "${:,.2f}".format(remainingFunds)

print()

print('Welcome to Goat Game. You have the chance to build a all time NBA starting 5 to beat the computers starting 5')

print('Your original salary cap is:', salaryCap)
print()
print('First you will choose your shooting guard')
print('The value of each player is as follows:')
print(shootingGuard5 , '= $5')
print(shootingGuard4 , '= $4')
print(shootingGuard3 , '= $3')
print(shootingGuard2 , '= $2')
print(shootingGuard1 , '= $1')
print()
 

UserShootingGuard = input("Enter the initials of your shooting guard (i.e. Michael Jordan = 'MJ'): ")

if UserShootingGuard == 'MJ':
    print('You drafted', shootingGuard5, 'as your shooting guard')
    remainingFunds = 15 - 5
    currency = "${:,.2f}".format(remainingFunds)
    print('You have', currency, 'left in your salary cap')

if UserShootingGuard == 'KB':
        print('You drafted', shootingGuard4 , 'as your shooting guard')
        remainingFunds = 15 - 4
        currency = "${:,.2f}".format(remainingFunds)
        print('You have', currency, 'left in your salary cap')

if UserShootingGuard == 'AI':
        print('You drafted', shootingGuard3, 'as your shooting guard')
        remainingFunds = 15 - 3
        currency = "${:,.2f}".format(remainingFunds)
        print('You have', currency, 'left in your salary cap')

if UserShootingGuard == 'DW':
        print('You drafted', shootingGuard2, 'as your shooting guard')
        remainingFunds = 15 - 2
        currency = "${:,.2f}".format(remainingFunds)
        print('You have', currency, 'left in your salary cap')

if UserShootingGuard == 'EB':
        print('You drafted', shootingGuard1, 'as your shooting guard')
        remainingFunds = 15 - 1
        currency = "${:,.2f}".format(remainingFunds)
        print('You have', currency, 'left in your salary cap')


print()
print('The value of each player is as follows:')
print(pointGuard5 , '= $5')
print(pointGuard4 , '= $4')
print(pointGuard3 , '= $3')
print(pointGuard2 , '= $2')
print(pointGuard1 , '= $1')

 
salaryCap = "${:,.2f}".format(remainingFunds)

UserPointGuard = input("Enter the initials of your point guard (i.e. John Stockton = 'JS'): ")

if UserPointGuard == 'MJ':
    print('You drafted', pointGuard5, 'as your point guard')
    remainingFunds2 = remainingFunds - 5
    currency = "${:,.2f}".format(remainingFunds2)
    print('You have', currency, 'left in your salary cap')
        
if UserPointGuard == 'SC':
    print('You drafted', pointGuard4, 'as your shooting guard')
    remainingFunds2 = remainingFunds - 4
    currency = "${:,.2f}".format(remainingFunds2)
    print('You have', currency, 'left in your salary cap')
        
if UserPointGuard == 'IT':
    print('You drafted', pointGuard3, 'as your shooting guard')
    remainingFunds2 = remainingFunds - 3
    currency = "${:,.2f}".format(remainingFunds2)
    print('You have', currency, 'left in your salary cap')
        

if UserPointGuard == 'JS':
    print('You drafted', pointGuard2, 'as your shooting guard')
    remainingFunds2 = remainingFunds - 2
    currency = "${:,.2f}".format(remainingFunds2)
    print('You have', currency, 'left in your salary cap')
        
if UserPointGuard == 'TY':
    print('You drafted', pointGuard1, 'as your shooting guard')
    remainingFunds2 = remainingFunds - 1
    currency = "${:,.2f}".format(remainingFunds2)
    print('You have', currency, 'left in your salary cap')

        

 
salaryCap = "${:,.2f}".format(remainingFunds)

print('Next, you will choose your point guard')
print('The value of each player is as follows:')
print(smallForward5 , '= $5')
print(smallForward4 , '= $4')
print(smallForward3 , '= $3')
print(smallForward2 , '= $2')
print(smallForward1 , '= $1')


UserSmallForward = input("Enter the initials of your point guard (i.e. Scottie Pippen = 'SP'): ")
    
if UserSmallForward == 'LJ':
        print('You drafted', smallForward5, 'as your small forward')
        remainingFunds3 = remainingFunds2 - 5
        currency = "${:,.2f}".format(remainingFunds3)
        print('You have', currency, 'left in your salary cap')
            
if UserSmallForward == 'KD':
        print('You drafted', pointGuard4, 'as your shooting guard')
        remainingFunds2 = remainingFunds - 4
        currency = "${:,.2f}".format(remainingFunds2)
        print('You have', currency, 'left in your salary cap')
            
if UserSmallForward == 'LB':
        print('You drafted', pointGuard3, 'as your shooting guard')
        remainingFunds2 = remainingFunds - 3
        currency = "${:,.2f}".format(remainingFunds2) 
        print('You have', currency, 'left in your salary cap')
            
if UserSmallForward == 'SP':
        print('You drafted', pointGuard2, 'as your shooting guard')
        remainingFunds2 = remainingFunds - 2
        currency = "${:,.2f}".format(remainingFunds2)
        print('You have', currency, 'left in your salary cap')
            
if UserSmallForward == 'JW':
        print('You drafted', pointGuard1, 'as your shooting guard')
        remainingFunds2 = remainingFunds - 1
        currency = "${:,.2f}".format(remainingFunds2)
        print('You have', currency, 'left in your salary cap')
    
            
    
print('Next, you will choose your powerForward')
print('The value of each player is as follows:')
print(powerForward5 , '= $5')
print(powerForward4 , '= $4')
print(powerForward3 , '= $3')
print(powerForward2 , '= $2')
print(powerForward1 , '= $1')


UserPowerForward = input("Enter the initials of your power forward (i.e. Tim Duncan = 'TD'): ")
    
if UserPowerForward == 'TD':
        print('You drafted', powerForward5, 'as your small forward')
        remainingFunds3 = remainingFunds2 - 5
        currency = "${:,.2f}".format(remainingFunds3)
        print('You have', currency, 'left in your salary cap')
            
if UserPowerForward == 'KD':
        print('You drafted', powerForward4, 'as your shooting guard')
        remainingFunds2 = remainingFunds - 4
        currency = "${:,.2f}".format(remainingFunds2)
        print('You have', currency, 'left in your salary cap')
            
if UserPowerForward == 'LB':
        print('You drafted', powerForward3, 'as your shooting guard')
        remainingFunds2 = remainingFunds - 3
        currency = "${:,.2f}".format(remainingFunds2) 
        print('You have', currency, 'left in your salary cap')
            
if UserPowerForward == 'SP':
        print('You drafted', powerForward2, 'as your shooting guard')
        remainingFunds2 = remainingFunds - 2
        currency = "${:,.2f}".format(remainingFunds2)
        print('You have', currency, 'left in your salary cap')
            
if UserPowerForward == 'JW':
        print('You drafted', powerForward1, 'as your shooting guard')
        remainingFunds2 = remainingFunds - 1
        currency = "${:,.2f}".format(remainingFunds2)
        print('You have', currency, 'left in your salary cap')
    

print('Next, you will choose your Center')
print('The value of each player is as follows:')
print(center5 , '= $5')
print(center4 , '= $4')
print(center3 , '= $3')
print(center2 , '= $2')
print(center1 , '= $1')


UserCenter = input("Enter the initials of your Center (i.e. Shaquille Oneal = 'SO'): ")
    
if UserCenter == 'KJ':
        print('You drafted', center5, 'as your center')
        remainingFunds3 = remainingFunds2 - 5
        currency = "${:,.2f}".format(remainingFunds3)
        print('You have', currency, 'left in your salary cap')
            
if UserCenter == 'WC':
        print('You drafted', center4, 'as your center')
        remainingFunds2 = remainingFunds - 4
        currency = "${:,.2f}".format(remainingFunds2)
        print('You have', currency, 'left in your salary cap')
            
if UserCenter == 'SO':
        print('You drafted', center3, 'as your center')
        remainingFunds2 = remainingFunds - 3
        currency = "${:,.2f}".format(remainingFunds2) 
        print('You have', currency, 'left in your salary cap')
            
if UserCenter == 'BR':
        print('You drafted', center2, 'as your center')
        remainingFunds2 = remainingFunds - 2
        currency = "${:,.2f}".format(remainingFunds2)
        print('You have', currency, 'left in your salary cap')
            
if UserCenter == 'HO':
        print('You drafted', center1, 'as your center')
        remainingFunds2 = remainingFunds - 1
        currency = "${:,.2f}".format(remainingFunds2)
        print('You have', currency, 'left in your salary cap')
    
            
file_handle =  open("playerdatabase.csv", "r", encoding="utf8")
csv_reader = DictReader(file_handle)
table: List[Dict[str,float]] = []

for row in csv_reader:
        float_row: Dict[str, float] = {}
        for column in row:
                print(row)
                print(column)
                # if type(float_row[column]) == str:
                #         float_row[column] = str(row[column])
                # else:   
                #         float_row[column] = float(row[column])
        table.append(float_row)
        #print(row)

print(table)


file_handle.close()     
    

    
    
    
