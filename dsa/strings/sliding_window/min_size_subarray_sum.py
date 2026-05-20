class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """
        PROBLEM:find minimal length subarray with sum>= target

        PATTERN:sliding window (variable size)

        THE PLAN:
        1.use left and right pointers, current sum, and min_length tracker
        2.expand window: add nums[right] to current_sum
        3.shrink window: while sum is >= target:
            .update min_length
            .remove nums[left], move left forward
        4.return min_length (or 0 if never found)
        
        """
        left = 0
        current_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            #expand: add right element
            current_sum += nums[right]
            #shrink:while valid, try smaller windows
            while current_sum >= target:
                min_length = min(min_length,right-left+1)
                current_sum-=nums[left]
                left +=1
        return min_length if min_length != float('inf') else 0