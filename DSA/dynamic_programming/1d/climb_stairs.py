class Solution:
    """"
    THE PROBLEM: Find the number of ways to climb n stairs taking 1 or 2 steps

    PATTERN: Dynamic Programming

    INSIGHT: To reach step `i` you must come from either step `i-1` or step `i-2`
    Therefore the ways to reach step `i` is the sum of the ways to reach those two previous steps
    This mirrors the fibonacci sequence

    THE PLAN: 
    1. Handle base cases: if n is 1, return 1; if n is 2 return 2
    2. Initialize two variables (one_step_behind = 2 and two_steps_behind = 1)
    3. Loop from step 3 up to n
    4. Calculate current_ways = one_step_behind + two_steps_behind
    5. Shift pointers forward : two_steps_behind becomes one_step_behind, one_step_behind becomes current_ways
    6. Return one_step_behind after the loop ends

    Example: n = 4
    - step 3: current = 2 + 1 = 3 -> two_behind=2, one_behind=3
    - step 4: current = 3 + 2 = 5 -> two_behind=3, one_behind=5
    Result: 5

    TIME: O(n) - Single pass iteration upto n
    SPACE: O(1) - Only tracking 2 variables instead of a full DP array

    """
    def climbStairs(self, n: int)-> int:

        if n < 2:
            return n
        
        two_steps_behind = 1
        one_step_behind = 2

        for _ in range(3, n+1):
            current_ways = one_step_behind + two_steps_behind
            two_steps_behind = one_step_behind
            one_step_behind = current_ways

        return one_step_behind
