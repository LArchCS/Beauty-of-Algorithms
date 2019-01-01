import random

# The palyer who comes up with a random number for guesser, and tells result for each guess from guesser.
class Teller():
    def __init__(self, number):
        self.secretNumber = str(number)
        self.guesses = 0
        self.guess = ""

    # Returns a result based on comparing guess with secret number.
    def tellResult(self, value):
        self.guesses += 1
        res = "You got the answer {} with {} gusses".format(self.secretNumber, self.guesses)
        if self.guess != self.secretNumber:
            self.guess = str(value)
            if self.guess == "exit":
                res = "Exit"
            elif not isValidNumber(self.guess):
                res = "Please enter a valid number"
            else:
                A, B = checkResult(self.guess, self.secretNumber)
                if A != 4:
                    res = "{}A{}B".format(A, B)
        print(" Teller: {}".format(res))
        return res

# The player who guesses the number from teller.
class Guesser():
    def __init__(self):
        self.candidates = list(range(1023, 9877))
        self.guessed = {}
    
    # Returns a guess based on guesses alread made.
    def makeGuess(self):
        guess = "exit"
        while len(self.candidates) > 0 and not (isValidNumber(guess) and self.isValidGuess(guess)):
            guess = str(self.candidates.pop())
        print("Guesser: {}".format(guess))
        return guess
    
    # Registers a guess with a result.
    def registerGuessResult(self, guess, result):
        self.guessed[guess] = result
    
    def isValidGuess(self, value):
        for guess in self.guessed:
            try:
                A = int(self.guessed[guess][0])
                B = int(self.guessed[guess][2])
                a, b = checkResult(value, guess)
                if a != A or b != B:
                    return False
            except:
                continue
        return True

# Returns true if input number starts with non zero integer, has no dupicates, and has 4 digits.
def isValidNumber(number):
    try:
        int(number)
    except ValueError:
        return False
    number = str(number)
    if len(number) != 4:
        return False
    if number[0] == '0':
        return False
    seen = set()
    for n in number:
        if n in seen:
            return False
        seen.add(n)
    return True

# Returns the comparison result of guess and number in the format of (A, B).
def checkResult(guess, number):
    A = 0
    B = 0
    for i in range(4):
        if guess[i] == number[i]:
            A += 1
        elif guess[i] in number:
            B += 1
    return (A, B)

# Replaces guesser or teller with this method if you want to play against computer.
def readInput():
    return str(input("Please enter a valid number: "))

def __main__():
    secretNumber = str(random.randint(1023, 9877))
    while not isValidNumber(secretNumber):
        secretNumber = str(random.randint(1023, 9877))
    guess = ""

    teller = Teller(secretNumber)
    guesser = Guesser()

    while guess != secretNumber and guess != "exit":
        guess = guesser.makeGuess()
        guesser.registerGuessResult(guess, teller.tellResult(guess))

__main__()