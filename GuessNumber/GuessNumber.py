import random


def play_game():

    comNum = random_number()

    print ("Welcome to the number guessing game!")
    print ("I'm thinking of a number between 0 and 20.")


    while True:

        usernum = get_guess()

        if usernum == comNum:
            print ("Congratualations, you win!")
            break

        elif usernum > comNum:
            print ("Too high, guess again.")

        elif usernum < comNum:
            print ("Too low, guess again")

    #print ("Thanks for playing")



def random_number():

    number = random.randint(0,21)

    return number

def get_guess():

    usernum = int(input("Please enter a number: "))

    return usernum


if __name__ == '__main__':
    play_game()
