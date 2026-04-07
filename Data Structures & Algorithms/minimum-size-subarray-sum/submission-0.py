class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        l_nums = len(nums)
        curr_sum = 0
        l = 0
        r = 0

        while r < l_nums:
            if nums[r] >= target:
                return 1 # base case
            
            curr_sum += nums[r]

            while curr_sum >= target and l < r:

                min_len = min(min_len, r-l+1)
                curr_sum -= nums[l] # make sure to keep curr_sum ready for next sub array search
                l += 1 # shrink the window from left

            r += 1 # expand the window from right

        
        return min_len if min_len != float('inf') else 0