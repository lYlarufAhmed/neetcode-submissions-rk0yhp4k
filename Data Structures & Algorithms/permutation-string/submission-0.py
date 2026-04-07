import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_sorted = sorted(s1)


        for left in range((len(s2) - len(s1)) + 1):
            # for right in range(left+len(s1) , len(s2)):
            right = left+len(s1)
            # print(left, right)
            if s1_sorted == sorted(s2[left:right]):
                return True

        return False
