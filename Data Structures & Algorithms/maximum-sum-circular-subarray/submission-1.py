class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        global_max = nums[0]
        global_min = nums[0]


        curr_max = 0
        curr_min = 0
        total = 0

        for num in nums:

            curr_max = max(num, curr_max+num)
            curr_min = min(curr_min+num, num)
            total += num

            global_max = max(global_max, curr_max)
            global_min = min(global_min, curr_min)


        if total < 0:
            return global_max
        
        return max(global_max, total-global_min)


        