class Solution:
    def isPalindrome(self, s: str) -> bool:

        start, end = 0, len(s)-1

        while start < end:
            both_alnum = s[start].isalnum() and s[end].isalnum()
            if both_alnum and s[start].lower() != s[end].lower():
                return False
            if both_alnum:
                end -= 1    
                start += 1
            else:
                if not s[start].isalnum():
                    start += 1
                if not s[end].isalnum():
                    end -= 1
        return True
        