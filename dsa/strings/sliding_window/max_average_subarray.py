class Solution:
    def findMaxAverage( self, nums: list[int], k: int) -> float:

        """
        problem:find contiguous subarray of length k with maximum average

        pattern: sliding window (fixed size)

        the plan:
        1.calculate the sum of the first k elements (initial window)
        2.track this as max_sum
        3.slide the window one position at a time:
            .remove leftmost element (substract nums[new_index-k])
            .add new rightmost element (add nums[new_index])
            .update max_sum if current sum is larger
        4.return max_sum/k (the maximum average)

        """
        current_sum = sum(nums[:k])
        max_sum = current_sum

        for new_index in range(k,len(nums)):
            #remove left element, add right element
            current_sum = current_sum - nums[new_index - k] + nums[new_index]
            #update max if needed
            max_sum = max(max_sum,current_sum)
        return max_sum/k