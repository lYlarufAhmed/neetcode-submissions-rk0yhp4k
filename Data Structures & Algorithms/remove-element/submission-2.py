class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # to solve this we will use two pointer
        # left one iterate to find and swap with right one index
        # one edge case to handle is to make sure k is not pointing
        # to val that's why we have inner while loop
        k = len(nums)
        i = 0
        while i < k:
            if nums[i] == val:
                # while k > i and nums[k-1] == val: # to handle whin
                #     k -= 1
                nums[k-1], nums[i] = nums[i], nums[k-1]
                k -= 1
            else:
                i += 1
        return k