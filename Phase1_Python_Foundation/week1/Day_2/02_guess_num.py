"""
Docstring for AI_ML_MASTERY_JOURNEY.Phase1_Python_Foundation.week1.Day_2.02_guess_num

Challenge 2 · Easy
Number Guessing Game
The computer picks a random number between 1 and 100. 
The user keeps guessing. 
After each guess, say "Too high!" or "Too low!" 
until they get it right. Track the number of attempts.

Use import random and random.randint(1, 100)
Use a while loop (you don't know when they'll guess right)
Count attempts with a counter variable
Print congratulations with attempt count at the end

"""

import random

# print(computer_choice)
computer_choice = random.randint(1,100)

count = 0
max_attempts = 7
lower_bound = 1
upper_bound = 100

print(f"I am thinking of a number and you have {max_attempts} tries! ")

while count < max_attempts:
    print(f"\nHint: The number is between {lower_bound} and {upper_bound}")

    try:
        user_choice = int(input(f"Attemp : {count + 1} | Enter your guess: "))
    except:
        print("Invalid input! Please enter a whole number")
        continue

    

    

    #check the range first
    if user_choice < 1 or user_choice > 100:
        print("Out of range! Please enter the number between 1 to 100.")
        continue # skip the rest of the loop and ask again 
    
    # count increment
    count += 1

    # step to check guess
    if user_choice == computer_choice:
        print(f"You have guess the correct number i.e. {computer_choice} 😃 in {count} attempt 🔢")
        break
    
    elif user_choice < computer_choice:
        print("Too Short 📉!!")
        if user_choice >= lower_bound:
            lower_bound = user_choice + 1
            print(f"updated lower_bound is {lower_bound}")
    
    else:
        print("Too High ↗️ !!")
        if user_choice <= upper_bound:
            upper_bound = user_choice - 1
            print(f"updated upper_bound is {upper_bound}")

# Check if the loop finished because they ran out of tries
if user_choice != computer_choice:
    print("=" * 70)
    print(f"GAME OVER! You have used all the {max_attempts} Attempts")
    print(f"The correct guess was {computer_choice}")
    print("=" * 70)

