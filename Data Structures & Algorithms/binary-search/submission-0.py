class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # base case
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1

        
        while left <= right:
            # print('left ', left, 'right ', right)
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
        
        return -1
