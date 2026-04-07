class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        res = []


        def backtrack(start, curr):
            if len(curr) == k:
                res.append(list(curr))


            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()
        

        backtrack(0, [])

        return res
