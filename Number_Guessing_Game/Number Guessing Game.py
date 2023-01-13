#importing random
import random
#rest of the code
print("number guessing game Please Do NOT Input Words Or Typed Out Numbers")
range1 = int(input("Range Number 1:  "))
range2 = int(input("Range Number 2:  "))
#stops the code
stop = 2

guess_taken = 0
num = random.randint(range1,range2)
while stop < 5:   
    Guess = int(input('Enter Number: '))
    Guess2 = str(Guess)
    #shows how many guesse it took to get the answer
    guess_taken2 = str(guess_taken + 1) 
    if Guess < num and Guess > range1:
        print("Num Is More Than  " + Guess2)  
        guess_taken += 1
    elif Guess == num:
        print("You Found My Number")
        print("Total Guesses Taken  " + guess_taken2)
        stop += 1000 
    elif Guess > num and Guess < range2:
        print("Num Is Less Than  "   + Guess2)
        guess_taken += 1
    elif Guess < range1 or Guess > range2:
        print("The Number You Have Typed Is Outside The Range Values")