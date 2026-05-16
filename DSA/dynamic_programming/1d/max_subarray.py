class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        THE PROBLEM: Find the maximum sum of a contiguous subarray within an array (Problem 53)

        PATTERN: Dynamic Programming / Kadane's Algorithm

        INSIGHT: At each position, the maximum subarray ending there is either 
        the current number alone, or the current number added to the previous subarray sum.
        If the running sum drops below zero, reset it to the current number.

        THE PLAN:
        1. Initialize max_sum and current_sum to the first element of the array
        2. Iterate through the array starting from the second element
        3. For each number, update current_sum to be the max of current_number or (current_sum + current_number)
        4. Update max_sum if current_sum is greater than the global max_sum

        Example: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        - num = -2: current = -2, max = -2
        - num =  1: current = max(1, -2+1) = 1, max = 1
        - num = -3: current = max(-3, 1-3) = -2, max = 1
        - num =  4: current = max(4, -2+4) = 4, max = 4
        Result: 6 (from subarray [4, -1, 2, 1])

        TIME: O(n)
        SPACE: O(1)
        """
        if not nums:
            return 0
            
        max_sum = nums[0]
        current_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum
