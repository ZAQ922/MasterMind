#__author__ = 'zaq92_000'
import random  #for random fun


########################################################################################################################
class MM:  #creates the code, allows for input of guesses, checks guessList against theCode
########################################################################################################################
    #theCode = []
    possible_numbers = range(1, 7)

    def makeCode(self):         #makes the code to break
        theCode = random.sample(self.possible_numbers, 4)
        return theCode          #return theCode to whoever called

########################################################################################################################
    def makeGuess(self):        #menu for getting input from user
        valid = False           #initially, the guessList is not valid
        guessList = []          #empty guessList which is made of 4 Parts
        while not valid:        #while the guess isn't valid, keep getting input
            try:
                print("1=R, 2=O, 3=Y, 4=G, 5=B, 6=V")
                a, b, c, d = input("Input ONLY 4 numbers from 1-6: ")
                a = int(a)                  #type casting: str -> int
                b = int(b)
                c = int(c)
                d = int(d)
                #input sanitation, the type casting catches non-int input, the if() catches unacceptable numbers
                if ((a < 1) or(a > 6)) or ((b < 1) or (b > 6)) or ((c < 1) or (c > 6)) or ((d < 1) or (d > 6)):
                    raise ValueError
                guessList.append(a)         #appending the input to guessList
                guessList.append(b)
                guessList.append(c)
                guessList.append(d)
                valid = True
                """guessList = [int(x) for x in input().split()]
                for x in guessList:
                    if x in self.possible_numbers:
                        range_count += 1
                if len(guessList) == len(self.theCode) and range_count == len(guessList):
                    valid = True                #if input is valid, continue
                else:
                    raise ValueError"""
            except(ValueError, TypeError):  #ensures wrong inputs get corrected
                guessList = []              #reset the guessList to empty
                print("ONLY 4 numbers from 1-6.")
                print(" ")
        return guessList                    #return guessList to whoever called


########################################################################################################################
    def checkGuess(self, code):             #compares the guess with the code, outputs ticks
        tickB = 0                           #set all ticks to 0
        tickW = 0
        none = 0
        remaining_code = []
        remaining_guess = []
        player_guess = self.makeGuess()            #calls makeGuess for the user's input
        for guess, part in zip(player_guess, code):  #index and part of the enumerated guess
            if guess == part:                #if it equals the code at this index
                tickB += 1
            else:
                remaining_code.append(part)  #whatever is left, see if it gets a tickW
                remaining_guess.append(guess)
        for guess in remaining_guess:       #cycle through the remaining guesses
            if guess in remaining_code:     #if it's in there, it gets tickW
                tickW += 1
            #   remaining_code.remove(guess)#can replace the "none += 1"
            else:                           #else it doesn't and should be blank
                none += 1
        return tickB, tickW, none


########################################################################################################################
def main():
    endgame = False     #won game flag
    ok = False          #initial playing flag
    count = 0           #ensure only 10 tries at a single code before asking to play again
    while not ok:       #while not ok to play
        try:            #ask if they want to play
            wanna = input("Do you want to play? (Y/N)")             #menu input
            if wanna == "Y" or wanna == "y":                        #if yes, play the game
                ok = True                                           #input flag = ok to play
                code = MM().makeCode()                              #creates the code for 1 round
                print(code)
                while count < 10 and not endgame:                   #within 10 tries and not a game ending event
                    black, white, no = MM().checkGuess(code)        #compares guess to code
                    if black == 4:                                  #when you get 4 black ticks you win
                        endgame = True                              #for ending the game once you've won
                        print("YOU WON")                            #banner for winning game
                    else:                                           #otherwise output ticks to help them solve it
                        print("Black:", black)                      #banner for mid-game
                        print("White:", white)
                        print("None:", no)
                    count += 1                                      #this comment is for Trevor
                    if count >= 10:                                 #once you're out of tries, you lose
                        endgame = True                              #for ending the game once you've lost
                        print("GET GUD")                            #banner for losing game
                        print("Code:", code)
            elif wanna == "N" or wanna == "n":          #if no, leave the game
                ok = True                               #input flag = ok to not play
                print("Goodbye")
            else:                                       #if input other that yes/no...
                raise ValueError
        except ValueError:                              #...tell them they're wrong
            print("Only Y or N")
            print(" ")



########################################################################################################################
if __name__ == '__main__':
    #MM().makeGuess()
    main()
