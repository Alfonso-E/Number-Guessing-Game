import random

top_of_range = input("Type a number greater than 0: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print('\nPlease type a number greater than 0: ')
        quit()
else:
    print("\nPlease type a number: ")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("\nTry to guess the number I'm thinking of: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    
    else:
        print("\nPlease type a number: ")
        continue
    
    if user_guess == random_number:
        print("\nCongratulations! You guessed the number correctly!")
        break
    
    elif user_guess > random_number:
            print("\nThe number you guessed is higher than the number I'm thinking of.")
    else:
            print("\nThe number you guessed is lower than the number I'm thinking of.")
        
print("\nYou got in", guesses, "guesses!")
        

    

