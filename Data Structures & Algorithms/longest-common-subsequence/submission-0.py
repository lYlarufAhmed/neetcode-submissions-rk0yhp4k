class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        str1_len, str2_len = map(len, [text1, text2])
        
        if text1 == text2:
            return str1_len
        

        prevRow = [0 for _ in range(str2_len + 1)]

        for r in range(str1_len-1, -1, -1):
            currRow = [0 for _ in range(str2_len + 1)]
            for c in range(str2_len-1, -1, -1):
                if text1[r] == text2[c]:
                    currRow[c] = 1 + prevRow[c+1]
                else:
                    currRow[c] = max(prevRow[c], currRow[c+1])
            
            prevRow, currRow = currRow, prevRow
        
        return prevRow[0]
