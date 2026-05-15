class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
        PROBLEM:longest substing without repeating characters

        PATTERN:sliding window + set/hashmap

        THE PLAN:
        1.use left pointer, set to track characters in window, max_length
        2.expand: add s[right] to window
        3.shrink: whiles[right] is duplicate:
            .remove s[left] from set
            .move left forward
        4.update max_length after each window adjustment

        TIME: O(n) , SPACE: O(min(n,charset_size))

        KEY INSIGHT:when you hit a duplicate, shrink from left until the duplicate is removed,
            then continue expanding.

        
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