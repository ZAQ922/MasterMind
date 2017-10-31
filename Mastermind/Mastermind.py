#__author__ = 'zaq92_000'
from random import randint  #for random fun


########################################################################################################################
class MM:  #creates the code, allows for input of guesses, checks guessList against theCode
########################################################################################################################
    def makeCode(self):  #makes the code to break
        theCode = []
        a = randint(1, 6)
        b = randint(1, 6)
        c = randint(1, 6)
        d = randint(1, 6)
        theCode.append(a)
        theCode.append(b)
        theCode.append(c)
        theCode.append(d)
        return theCode

    ########################################################################################################################
    def makeGuess(self):  #menu for getting input from user
        valid = False  #initially, the guessList is not valid
        guessList = []#empty guessList which is made of 4 Parts
        while not valid:  #while the guess isn't valid, keep getting input
            try:
                print("1=R, 2=O, 3=Y, 4=G, 5=B, 6=V")
                a, b, c, d = input("Input ONLY 4 numbers from 1-6: ")
                if (not a.isdigit()) or (not b.isdigit()) or (not c.isdigit()) or (not d.isdigit()):
                    if (0 > a > 7) or (0 > b > 7) or (0 > c > 7) or (0 > d > 7):
                        raise ValueError
                guessList.append(a)
                guessList.append(b)
                guessList.append(c)
                guessList.append(d)
                valid = True
            except(ValueError, TypeError):  #ensures wrong inputs get corrected
                guessList = [] #reset the guess empty
                print("ONLY 4 numbers from 1-6.")
                print(" ")
        return guessList


    ########################################################################################################################
    def checkGuess(self):#compares the guess with the code, outputs ticks
        tickB = 0
        tickW = 0
        none = 0
        aList = [1,2,3,4]
        aCode = self.makeCode()
        #aList = self.makeGuess()
        for idx, part in enumerate(aList):
            if part == aCode[idx]:
                tickB += 1
            elif part in aCode:
                tickW += 1
            else:
                none += 1
        print("B", tickB)
        print("W", tickW)
        print("none ", none)
        print(aCode)


########################################################################################################################
def main():
    MM().makeCode()
    MM().makeGuess()
    MM().checkGuess()


########################################################################################################################
if __name__ == '__main__':
    main()
