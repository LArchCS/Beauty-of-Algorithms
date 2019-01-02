import random

# The palyer who comes up with a random number for guesser, and tells result for each guess from guesser.
class Teller():
    def __init__(self, number):
        self.secretNumber = number
        self.numGuesses = 0

    # Returns a result based on comparing guess with secret number.
    def tellResult(self, guess):
        self.numGuesses += 1
        res = ""
        if guess == "exit":
            res = "Exit"
        elif not isValidNumber(guess):
            res = "Please enter a valid number"
        else:
            A, B = checkResult(guess, self.secretNumber)
            if A == len(self.secretNumber):
                res = "You got the answer {} with {} guesses".format(self.secretNumber, self.numGuesses)
            else:
                res = "{}A{}B".format(A, B)
        return res

# The player who guesses the number from teller.
class Guesser():
    def __init__(self):
        self.candidates = [str(num) for num in range(9876, 1022, -1)]
        self.guessResults = {}

    # Returns a guess based on guesses alread made.
    def makeGuess(self):
        guess = "exit"
        while len(self.candidates) > 0 and not (isValidNumber(guess) and self.isValidGuess(guess)):
            guess = self.candidates.pop()
        return guess

    # Registers a guess with a result.
    def registerGuessResult(self, guess, result):
        self.guessResults[guess] = result

    def isValidGuess(self, value):
        for guess in self.guessResults:
            try:
                a = int(self.guessResults[guess][0])
                b = int(self.guessResults[guess][2])
                A, B = checkResult(value, guess)
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
    return A, B

# Replaces guesser with this method if you want to play against teller.
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
        result = teller.tellResult(guess)
        guesser.registerGuessResult(guess, result)
        print("Guesser: {}\n Teller: {}".format(guess, result))

__main__()

'''
Guesser: 1023
 Teller: 1A0B
Guesser: 1456
 Teller: 0A1B
Guesser: 4078
 Teller: 0A2B
Guesser: 5783
 Teller: 3A0B
Guesser: 6783
 Teller: You got the answer 6783 with 5 guesses
'''
