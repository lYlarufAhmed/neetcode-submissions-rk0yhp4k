class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        len_s = len(s)

        for left in range(len_s):
            max_oc = 0
            count = defaultdict(int)
            for right in range(left, len_s):
                c = s[right]

                count[c] += 1

                subs_len = right - left+1

                max_oc = max(count[c], max_oc)

                c_k = subs_len - max_oc
                if c_k <= k:
                    print(count)
                    res = max(res, subs_len)
        return res