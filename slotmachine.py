import random

bal = 100
point = 0

def play():
    s1 = random.randint(1,9)
    s2 = random.randint(1,9)
    s3 = random.randint(1,9)

    point = 0
    
    print("spinning...")
    print("| x | x | x |")
    print("spinning...")
    print("|",s1,"| x | x |")
    print("spinning...")
    print("|",s1,"|",s2,"| x |")
    print("spinning...")
    print("|",s1,"|",s2,"|",s3,"|")
    


    if s1==s2==s3:
        print("JACKPOT!!!!")
        point+=1
        

    else:
        print("Better Luck Next Time!")
        
       
def balance():
    print("Your balance is:", bal)

print(
    '''
    --------------------------
    |  WELCOME TO ESH CASINO |
    --------------------------
    TYPE: 
    - SPIN    - TO START THE GAME
    - RULES   - SEE RULES
    - BALANCE - CHECK BALANCE
    - EXIST   - TO EXIST
    --------------------------
    '''
)
def points():
    print("Points:",point)

def rules():
    print(
        '''
        - type spin to start the game
        - type balance to check your balance
        - type exist to exist game
        '''
    )

while True:
    userInput = input("-> ").lower()   

    if(userInput == "spin"):
        bal-=1
        play()
        continue

    elif(userInput == "balance"):
        balance()
        continue

    elif(userInput == "exit"):  
        exit()
        
    elif(userInput == "rules"): 
        rules()
        continue
    elif(userInput == "points"): 
        points()
        continue    