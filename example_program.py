from random import randint

def the_program():
    print("")
    print("Guess a number between 0 and 15!")
    a = int(input("What is your guess?: "))
    b = randint(0, 15)
    if a == b:
        print("Good job, you've guessed the number!")
    elif a != b:
        print("Better luck next time...") 