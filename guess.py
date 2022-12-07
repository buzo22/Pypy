secret_number = 21

while True:
    guess = int(input("Guess the number between 1 and 40: "))
   
    if guess == secret_number:
        print("You guessed it")
    else:
        print("Wrong choice")
        break