class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = nums[0]

        currSum = 0

        for i in nums:
            currSum = max(currSum, 0) # avoid negative number
            currSum += i
            maxSum = max(maxSum, currSum)

        return maxSum
        