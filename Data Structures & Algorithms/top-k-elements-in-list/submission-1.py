class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resDict = {}
        bucket = [[] for i in range(len(nums)+1)]
        for num in nums:
            resDict[num] = 1 + resDict.get(num, 0)

        for key, c in resDict.items():
            bucket[c].append(key)
        
        res = []

        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
