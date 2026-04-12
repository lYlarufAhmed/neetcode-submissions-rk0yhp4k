class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_c = 0
        for n in nums:
            if n != 1:
                count = 0
            elif n == 1:
                count += 1
                max_c = max(count, max_c)

        return max_c