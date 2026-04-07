class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        l_arr = len(arr)
        if l_arr < 1:
            return 0

        prev_sum = sum(arr[:k])
        l = 0

        for r in range(k, l_arr):
            if (prev_sum/k) >= threshold:
                count += 1
            
            prev_sum -= arr[l]
            prev_sum += arr[r]

            l += 1
        if (prev_sum/k) >= threshold:
            count += 1

        return count