# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        h = n
        while l<=h:
            mid = (l+h)//2
            ans = guess(mid)
            if ans > 0:
                l = mid +1 ## +1 numif lower than picked number
            elif ans < 0: 
                h = mid - 1  ## -1 if num higher than picked numer
            else:
                return mid 
            