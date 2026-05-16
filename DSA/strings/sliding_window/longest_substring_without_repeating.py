class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        THE PROBLEM: Find the length of the longest substring without repeating characters (Problem 3)

        PATTERN: Sliding window (Dynamic / Expand-Shrink)

        INSIGHT: Use a set to track unique characters in the current window.
        Expand the window to the right. 
        If a duplicate appears, shrink the window from the left until it is unique again.

        THE PLAN:
        1. Initialize left pointer, max_length tracking variable, and an empty hash set
        2. Iterate right pointer through the string to expand the window
        3. While right character exists in set, remove left character and increment left pointer
        4. Add right character to set and update max_length with current window size (right - left + 1)

        Example: s = "abcabcbb"
        - right=0 ('a'), set={'a'}, max=1
        - right=3 ('a'), duplicate! Shrink left past 'a'. set={'b','c','a'}, max=3
        Result: 3

        TIME: O(n)
        SPACE: O(min(m, n)) where n is string length and m is alphabet/charset size
        """
        left = 0
        char_set = set()
        max_length = 0

        for right in range(len(s)):
            #shrink while duplicates exist
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            #add current character
            char_set.add(s[right])

            # update max length
            max_length = max(max_length, right-left +1)

        return max_length
