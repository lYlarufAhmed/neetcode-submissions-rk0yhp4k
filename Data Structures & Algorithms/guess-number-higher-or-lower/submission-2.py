# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:


        if guess(n) == 0: return n

        high = n
        low = 1

        while True:
            guessNumber = (high+low) // 2
            guessResult = guess(guessNumber)

            if guessResult == 1: # guessNumber < pick
                low = guessNumber
            elif guessResult == -1: # pick > guessNumber
                high = guessNumber
            else:
                return guessNumber