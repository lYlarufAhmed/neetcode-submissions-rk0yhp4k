class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        seen_num = set(nums)

        for num in seen_num:
            if num - 1 not in seen_num:
                curr_num = num
                curr_streak = 1

                while curr_num +1 in seen_num:
                    curr_num += 1
                    curr_streak += 1
                
                longest_streak = max(longest_streak, curr_streak)

        return longest_streak