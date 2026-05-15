class Solution:
    """
    THE PROBLEM: Find days until next warmer temperature

    PATTERN: Monotonic stack

    INSIGHT: Use stack to track indices of decreasing temperatures.
    When we find warmer temp, pop stack and calculate days

    THE PLAN:
    1. Use stack to store indices of temperature
    2. For each temperature, pop all cooler temps from the stack
    3. Calculate days difference for each popped index
    4. Push current index to stack

    Example: temperatures = [73,74,75,71,69,72,76,73]
    - Day 0 (73): wait 1 day for 74
    - Day 3 (71): wait 2 days for 72
    Result: [1,1,4,2,1,1,0,0]

    Time: O(n)
    Space: O(n)
    """
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        num_days = len(temperatures)
        days_to_wait = [0] * num_days
        stack_of_waiting_days = []

        for current_day in range(num_days):
            current_temp = temperatures[current_day]

            while stack_of_waiting_days and temperatures[stack_of_waiting_days[-1]] < current_temp:
                previous_cooler_day = stack_of_waiting_days.pop()
                days_to_wait[previous_cooler_day] = current_day - previous_cooler_day
            
            stack_of_waiting_days.append(current_day)
        
        return days_to_wait

        