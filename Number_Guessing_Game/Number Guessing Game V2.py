#importing random
import random
#rest of the code
print("number guessing game Please Do NOT Input Words Or Typed Out Numbers")
#trying to see if the input is a valid number
while True:
    Repeat = 0
    while True:
        Repeat = 0 
        while True:    
            try:    
                name = str(input("what is your name?:  "))
                break
            except ValueError:
                print("Not A Name")
                continue
        print("hello "+ name +" Would you like to play a game?")
        print("to continue type 1 to stop type 2 ")   
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
        print("get ready "+name)
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
                    print("Num Is More Than  " + Guess2) 
                    guess_taken += 1
                elif Guess == num:
                    print("Congrants " + name +" It Took You " + guess_taken2 + " Guess To Find My Number")
                    break
                elif Guess > num and Guess <= range2:
                    print("Num Is Less Than  "   + Guess2)
                    guess_taken += 1
                elif (Guess < range1 or Guess > range2):
                    print("The Number You Have Typed Is Outside The Range Values")
        #running the code          
        while True:    
            if range1 >= range2:
                print("PUT THE BIGGER NUMBER IN RANGE 2 OR MAKE THE FIRST NUMBER SMALLER")
                break
            else:
                num = random.randint(range1,range2)
                code()
                
            print(name +" Would You Like To Play Again? Type 1 To Continue or 2 to Stop")
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
    
    