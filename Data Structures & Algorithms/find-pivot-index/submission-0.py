class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        prefixSum = [nums[0]] * n


        for i in range(1, n):
            prefixSum[i] = nums[i] + prefixSum[i-1]
        
        for i in range(n):
            leftSum = prefixSum[i] - nums[i]
            rightSum = prefixSum[n - 1] - prefixSum[i]

            if leftSum == rightSum:
                return i 

        print(prefixSum) 
            
        return -1