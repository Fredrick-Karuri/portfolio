class Solution:
    """
    THE PROBLEM: Determine if any value appears atleast twice in an integer array

    PATTERN: Hash Set

    INSIGHT: A hashset allows for lookup in constant time. As we iterate we can lookup
    to see if we have seen the current number before. If we have, a duplicate exists.

    THE PLAN:
    1. Initialize an empty hash set to keep track of unique numbers
    2. Iterate through each number in the input array
    3. If the current number is already present in the set, return True
    4. Otherwise, add the current number to the set and continue the loop
    5. Return False if the loop finishes without finding any duplicates

    Example: nums = [1, 2, 3, 1]
    - num = 1: not in set -> set = {1}
    - num = 2: not in set -> set = {1, 2}
    - num = 3: not in set -> set = {1, 2, 3}
    - num = 1: already in set! ✓
    Result: True

    TIME: O(n) - Single pass through the array of size n
    SPACE: O(n) - In the worst case, all elements are unique and stored in the set
    """
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen_numbers = set()

        for current_number in nums:
            if current_number in seen_numbers:
                return True
            seen_numbers.add(current_number)
        return False
        