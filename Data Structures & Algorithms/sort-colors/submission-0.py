class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import defaultdict

        color_map = defaultdict(int)

        for num in nums:
            color_map[num] += 1
        i = 0
        for key in sorted(color_map.keys()):
            val = color_map[key]
            while val:
                nums[i] = key
                val -= 1
                i += 1