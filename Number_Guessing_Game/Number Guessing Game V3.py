#importing random
import random
#rest of the code
print("Number Guessing Game By Red_Cardinal \nPlease Do Not Input Words Or Typed Out Numbers")
#trying to see if the input is a valid number
while True:
    Repeat = 0
    while True:
        Repeat = 0 
        #asking the user name this will not be used out side of this code there in no leaderboard
        #if you get not a valid name somthing is broken
        while True:    
            try:    
                name = str(input("What is your name?:  "))
                break
            except ValueError:
                print("Not A Valid Name")
                continue
        print("Hello "+ name +" \nWould you like to play a game?")
        print("Type 1 to continue \nType 2 to stop")   
        #asking the user if they realy want to play
        while True:
            try:
                Repeat = int(input('Enter Number 1 or 2: '))
                break
            except ValueError:
                print("Not A Valid Number")
                continue
        
        if Repeat == 1 or Repeat == 2:
            break
        else:
            print("The input is not 1 or 2")
    
    if Repeat == 1:
        print("Get Ready "+name)
    elif Repeat == 2:
        break
    while True:    
        while True: 
            #asking for range values then checking to see if they are valid
            try:    
                range1 = int(input("Range Number 1:  "))
                break
            except ValueError:
                print("Not A Valid Number")
                continue
        while True:    
            try:    
                range2 = int(input("Range Number 2:  "))
                break
            except ValueError:
                print("Not A Valid Number")
                continue

        #defing the code
        def code():
            #setting the guess_taken to 1 to fix a bug
            guess_taken = 1  
            while True:  
                while True:
                    try:
                        Guess = int(input('Enter Number: '))
                        break
                    except ValueError:
                        print("Not A Valid Number")
                        continue
                Guess2 = str(Guess)
                #shows how many guess it took to get the answer and checking to make sure that the input is vaiid
                guess_taken2 = str(guess_taken) 
                if Guess < num and Guess >= range1:
                    print("The Number Is More Than  " + Guess2) 
                    guess_taken += 1
                elif Guess == num:
                    print("Congrants " + name +" \nIt Took You " + guess_taken2 + " Guesses To Find My Number")
                    break
                elif Guess > num and Guess <= range2:
                    print("The Number Is Less Than  "   + Guess2)
                    guess_taken += 1
                elif (Guess < range1 or Guess > range2):
                    print("The Number You Have Typed Is Outside The Range Values")
        #running the code          
        while True:    
            if range1 >= range2:
                print("Put The Bigger Number In Renge 2 \nOr Make The First Number Smaller")
                break
            else:
                num = random.randint(range1,range2)
                code()
                
            print(name +" Would You Like To Play Again? \nType 1 To Continue \nType 2 to Stop")
            #asking user if they want to repeat and checking to see if the number is valid
            while True:
                try:
                    Repeat = int(input('Enter Number 1 or 2: '))
                    break
                except ValueError:
                    print("Not A Valid Number")
                    continue
            if Repeat == 1 or Repeat == 2:
                break
            else:
                print("The input is not 1 or 2")
                break
        if Repeat == 2:
            break
        else:
            continue
    if Repeat == 1:
        continue
    elif Repeat == 2:
        break
