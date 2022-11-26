import random 

num = random.randint(1,9)
guess = 0

while guess < 5: 
    user_guess = int(input("Guess a number between 1-9, you only get 5 guesses \n"))
    guess +=1
    if user_guess == num:
        print("Good job you guessed the right number\n")
        break 
    else: 
        print("Sorry you did not guess the right number\n")