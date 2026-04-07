class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        


        res = []
        res.append(nums.copy())


        l = len(nums)

        for i in range(l-1):
            temp = []

            for curr in res:
                for j in range(i+1, l):
                    t = curr.copy()
                    t[i], t[j] = t[j], t[i]
                    temp.append(list(t))
            res = res + temp
        return res