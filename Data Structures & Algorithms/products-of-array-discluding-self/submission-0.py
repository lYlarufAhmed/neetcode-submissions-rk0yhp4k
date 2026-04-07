class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        l, r, ans = [0] * length, [0] * length, [0] * length

        l[0] = 1
        for i in range(1, length):
            l[i] = l[i-1] * nums[i-1]
        
        r[length-1] = 1
        for i in range(length-2, -1, -1):
            r[i] = r[i+1] * nums[i+1]
        

        for i in range(length):
            ans[i] = l[i] * r[i]
        
        return ans