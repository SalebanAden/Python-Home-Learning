import random

print('Hello! What is your name?')
myName = input()
number = random.randint(1, 10)


def main():
    guesses=1
    print('Well, ' + myName + ', I am thinking of a number between 1 and 10.')

    while guesses < 6:
        guess = int(input("Take a guess:"))
        if guess < number:
            print('Your guess is too low.')
            guesses = guesses + 1
        if guess > number:
            print('Your guess is too high.')
            guesses = guesses + 1
        if guess == number:
            print("good job, " + myName + "you guessed my number")
            print("Thank you for playing")
            break
        else:
            print("wrong, have another guess")
            guesses = guesses + 1

main()
guesses = 0

while guesses <6:
    guesses = guesses + 1
    print("Take a guess.")
    guess = int (input ())

    if guess < number:
        print('Your guess is too low.')  # Eight spaces in front of "print"

    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        print("good job, " + myName + "you guessed my number")
        print("Thank you for playing")
        break
    else:
        print("wrong, have another guess")
        guesses = guesses + 1