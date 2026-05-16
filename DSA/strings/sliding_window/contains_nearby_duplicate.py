class Solution:
    
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """
        PROBLEM: check if duplicate exists within k distance

        PATTERN: sliding window + set

        THE PLAN:  
        1.use a set to track numbers in current window (size <=k)
        2.slide through the array:
            .if current number already in set -> found duplicate within k distance return true
            .add current number to set
            .if window size exceeds k, remove leftmost element from the set
        3.if no duplicates found return False

        """
        window=set()
        range_of_indices = range(len(nums))
        for current_index in range_of_indices:
            if nums[current_index] in window:
                return True
            window.add(nums[current_index])

            if len(window)>k:
                window.remove(nums[current_index-k])
        return False