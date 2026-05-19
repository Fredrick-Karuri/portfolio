"""
THE PROBLEM: Given a binary string s return the number of steps to reduce its value V to 0
Dividing an even number by 2 shifts bits right. Subtracting 1 from an odd number changes
the last bit from 1 to 0.

PATTERN: Bit manipulation

INSIGHT: Leading 0s do not contribute to the value. Once we strip them we process from 
right to left.
A '0' bit requires 1 operation (division)
A '1' bit requires 2 operations (subtract 1 to make it zero then divide by 2 to shift it out)
The final leftmost '1' only requires 1 operation to turn it into a 0

THE PLAN:
1. Remove any leading 0s from the binary string S
2. If the the string is empty or becomes "0" return 0 operations
3. Initialize an operation_count variable to 0
4. Track the index of the first meaningful "1" bit. (leftmost_one_index)
5. Iterate backward from the end of the string down to (but excluding) the leftmost_one_index
6. For every '0' increment count by 1. For every '1' increment count by 2
7. Add 1 final operation to clear out the remaining single '1' bit at the front.

Example: S = "011100" -> strip leading zeros -> "11100" (leftmost_one_index = 0)
- bit at index 4 ('0'): count + 1 = 1
- bit at index 3 ('0'): count + 1 = 2
- bit at index 2 ('1'): count + 2 = 4
- bit at index 1 ('1'): count + 2 = 6
- loop ends. Add 1 for the final '1' at index 0 -> 6 + 1 = 7
Result: 7

TIME: O(n) - Where n is the number of characters in the string, due to a single backward scan
SPACE: O(1) - Only using a few integer counters and pointers
"""
def numSteps(S:str):
    # strip leading 0s
    cleaned_string = S.lstrip("0")

    if not cleaned_string:
        return 0
    
    operation_count = 0
    string_length = len(cleaned_string)

    # Process every bit from right to left except the leftmost (index 0)
    for current_index in range(string_length - 1, 0,-1):
        if cleaned_string[current_index] == "0":
            operation_count += 1 # Even number - one operation
        else:
            operation_count +=2 # Odd number - two operations
    
    # Add one last operation to convert the remaining "1" at index 0 to 0
    operation_count +=1

    return operation_count

