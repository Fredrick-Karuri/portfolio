class Solution:
    """
    THE PROBLEM: Determine if string t is an anagram of string s

    PATTERN: Hash map / Frequency counter

    INSIGHT: An anagram means both strings have the exact same characters 
    with the exact same frequencies. If their lengths differ they cannot 
    be anagrams. We can count occurences of each character using a hashmap

    THE PLAN:
    1. If lengths of string s and string t are not equal return False
    2. Create a frequency map to track character balances
    3. Loop through both strings simultaneously
    4. Increment the balance for characters in s decrement for characters in t
    5. Check if all balances in the map are zero; If any are not, return False
    6. Return True if all character counts balance out perfectly

    Example: s = "rat", t = "car"
    - Lengths match (3 == 3)
    - Process index 0: count['r'] += 1, count['c'] -= 1
    - Process index 1: count['a'] += 1, count['a'] -= 1 (net 0)
    - Process index 2: count['t'] += 1, count['r'] -= 1 (net 'r' is 0)
    - Final map has count['c'] = -1 and count['t'] = 1. Not all zero.
    Result: False

    TIME: O(n) -  single pass through both strings of length n
    SPACE: O(1) - The hashmap holds a maximum of 26 keys for lowercase English letters

    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        character_counts = {}

        # Track frequencies by adding for s and subtracting for t
        for index in range(len(s)):
            char_from_s = s[index]
            char_from_t = t[index]

            character_counts[char_from_s] = character_counts.get(char_from_s,0) + 1
            character_counts[char_from_t] = character_counts.get(char_from_t,0) - 1

        # if it is a true anagram, every single count must resolve back to 0
        for count in character_counts.values():
            if count != 0:
                return False
        
        return True


        