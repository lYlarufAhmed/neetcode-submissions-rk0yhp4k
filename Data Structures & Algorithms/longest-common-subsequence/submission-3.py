class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        l_text1, l_text2 = map(len, [text1, text2])
        t1, t2 = (text1, text2) if l_text2 < l_text1 else (text2, text1)

        l_t1, l_t2 = len(t1), len(t2)

        dp = [0 for _ in range(l_t2 + 1)]
        for r in range(l_t1-1, -1, -1):
            prev = 0
            for c in range(l_t2-1, -1, -1):
                temp = dp[c]
                if t1[r] == t2[c]:
                    dp[c] = 1 + prev
                else:
                    dp[c] = max(dp[c], dp[c+1])
                
                prev = temp
        return dp[0]