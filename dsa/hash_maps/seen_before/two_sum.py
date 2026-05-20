class Solution:
    """
    THE PROBLEM: Find two numbers that sum to target, return their indices

    PATTERN: Hash map

    INSIGHT: For each number, check if its complement(target-num) exists.
    Store seen numbers with their indices

    THE PLAN:
    1. Create hash map to store value -> index
    2. For each number, calculate complement
    3. If complement exists in map, return both indices
    4. Otherwise, store current number and continue

    Example: nums=[2,7,11,15], target=9
    - num=2: complement=7, not seen yet, store {2:0}
    - num=7: complement=2, found at index 0 ✓
    Result: [0,1]

    TIME: O(n)
    SPACE: O(n)
    """
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen_values = {}

        for current_index , current_number in enumerate(nums):
            complement = target - current_number

            if complement in seen_values:
                return [seen_values[complement], current_index]
            
            seen_values[current_number] = current_index
        return []