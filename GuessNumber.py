import random

comNum = random.randint(0,21)

print ("Welcome to the number guessing game!")
print ("I'm thinking of a number between 0 and 20.")

while True:

    usernum = int(input("Please enter a number: "))

    if usernum == comNum:
        print ("Congratualations, you win!")
        break

    elif usernum > comNum:
        print ("Too high, guess again.")

    elif usernum < comNum:
        print ("Too low, guess again")


print ("Thanks for playing")
