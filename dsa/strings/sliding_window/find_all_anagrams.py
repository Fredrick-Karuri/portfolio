

class Solution:
    """
    THE PROBLEM: Find all start indices where p's anagram appears in s [Question 438]

    PATTERN: Sliding window + hashmap

    INSIGHT: Anagrams have same character frequencies. Use fixed size sliding window 
    of length p, compare frequency maps.

    THE PLAN: 
    1. Count character frequencies in p
    2. Use sliding window of size len(p) on s
    3. Track character frequencies in current window
    4. When window matches p's frequency, record start index
    5. Slide window: remove left character, add right character

    Example: s="cbaebabacd", p="abc"
    Windows: "cba"✓, "bae"✗, "aeb"✗, "eba"✗, ..."bac"✓, ...
    Result: [0, 6]
    """
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return[]
        
        result = []
        p_count = {}
        window_count = {}

        # Count frequencies in p
        for char in p:
            p_count[char] =p_count.get(char,0) + 1
        # Initial window
        for i in range(len(p)):
            char = s[i]
            window_count[char] = window_count.get(char,0) +1
        # Check first window
        if window_count == p_count:
            result.append(0)
        # Slide window
        for i in range(len(p), len(s)):
            # Add new character
            new_char = s[i]
            window_count[new_char] = window_count.get(new_char,0)+1

            # Remove old character
            old_char = s[i - len(p)]
            window_count[old_char] -=1

            if window_count[old_char] == 0:
                del window_count[old_char]
            # check if anagram
            if window_count == p_count:
                result.append(i- len(p) +1)
        return result
        