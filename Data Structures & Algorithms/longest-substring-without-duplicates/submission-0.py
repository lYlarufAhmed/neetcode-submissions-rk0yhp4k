class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)

        start = 0
        res = 0

        mp = {}

        for end, end_c in enumerate(s):
            if end_c in mp:
                start = max(start, mp[end_c]+1)
            
            res = max(res, end-start+1)
            mp[end_c] = end

        return res
        