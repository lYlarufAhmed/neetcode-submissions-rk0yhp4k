class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1: # Base case: array with 0 or 1 element
            return n

        # max_len = 1 # Initialize max length to 1 (a single element is turbulent)
        
        # We need to store the comparison result of the *previous* pair.
        # Initialize it to something neutral or handle the first comparison separately.
        # Let's initialize it based on the first pair.
        
        # Handle the first pair comparison separately to establish the initial 'last' state.
        # If arr[0] == arr[1], the first turbulent subarray starting at index 0 has length 1.
        # If arr[0] != arr[1], the turbulent subarray starting at index 0 has length 2.
        
        # A cleaner way: iterate through pairs and track current length.
        
        # Let's re-think: we need to compare arr[i-1] and arr[i]
        # We need to know the sign of the comparison of the previous pair.
        
        max_length = 1
        current_length = 1
        
        # Variable to store the sign of the previous comparison: 1 for >, -1 for <, 0 for ==
        prev_sign = 0 
        
        for i in range(1, n):
            current_sign = 0
            if arr[i-1] < arr[i]:
                current_sign = 1 # Increasing
            elif arr[i-1] > arr[i]:
                current_sign = -1 # Decreasing
            
            if current_sign == 0: # If current elements are equal, turbulence is broken.
                current_length = 1 # Start a new sequence of length 1 (the current element)
            elif current_sign != prev_sign: # If the sign alternates or it's the first non-equal pair
                current_length += 1 # Extend the current turbulent subarray
            else: # If the sign is the same as the previous one, turbulence is broken.
                  # The new subarray starts from the previous element.
                current_length = 2 # Reset to length 2 (the previous element and the current one)
            
            # Update max_length at each step
            max_length = max(max_length, current_length)
            
            # Update prev_sign for the next iteration
            prev_sign = current_sign
            
        return max_length

