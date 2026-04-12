class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        new_res = []

        for i in range(len(arr)-1):
            new_res.append(max(arr[i+1:]))
        
        new_res.append(-1)

        return new_res