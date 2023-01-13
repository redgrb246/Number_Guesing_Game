#importing random
import random
#rest of the code
print("Number Guessing Game By Red_Cardinal \nPlease Do Not Input Words Or Typed Out Numbers")
#trying to see if the input is a valid number
while True:
    Repeat = 0
    while True:
        Repeat = 0 
        while True:    
            try:    
                name = str(input("What is your name?:  "))
                break
            except ValueError:
                print("Not A Vailid Name")
                continue
        print("Hello "+ name +" \nWould you like to play a game?")
        print("Type 1 to continue \nType 2 to stop")   
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
                #shows how many guesse it took to get the answer
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
    #asking user if they want to repeat    
    
    #repeating code
    
    