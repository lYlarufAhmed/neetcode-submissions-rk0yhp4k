class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        max_num = arr[-1]
        new_res = [-1] * len(arr)

        for i in range(len(arr)-2, -1, -1):
            max_num = max(max_num, arr[i+1])
            new_res[i] = max_num
            
        

        return new_res