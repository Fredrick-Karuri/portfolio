class Solution:
    """
    THE PROBLEM: Calculate an array where each index contains the product of all numbers except itself without using division

    PATTERN: Prefix and Suffix (Left/Right) Product Accumulation

    INSIGHT: The product of all numbers except nums[i] is equal to the product of all numbers before i 
    multiplied by the product of all numbers after i. 
    We can accumulate the left products in a forward pass and then multiply by the right products 
    in a backward pass using a single running variable.

    THE PLAN:
    1. Intilialize an answer array of the same length filled with 1s
    2. Create a running variable left accumulator set to 1
    3. Iterate forward through the array: set answer[i] to left accumulator then update left accumulator 
    by multiplying it by nums[i]
    4. Create a running variable right accumulator set to 1
    5. Iterate backward through the array: set answer[i] to right accumulator then update right accumulator 
    by multiplying it by nums[i]
    6. Return completed answer array

    Example: nums = [1, 2, 3, 4]
    - Forward Pass (Left Products):  answer = [1, 1, 2, 6]
    - Backward Pass (Right Products Applied):
    - i = 3: right = 1 -> answer[3] = 6 * 1 = 6  -> right updates to 1 * 4 = 4
    - i = 2: right = 4 -> answer[2] = 2 * 4 = 8  -> right updates to 4 * 3 = 12
    - i = 1: right = 12 -> answer[1] = 1 * 12 = 12 -> right updates to 12 * 2 = 24
    - i = 0: right = 24 -> answer[0] = 1 * 24 = 24
    Result: [24, 12, 8, 6]

    TIME: O(n) - Two independent passes through the array of length n
    SPACE: O(1) - Excluding the output array, we only use two tracking integer variables

    """
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        array_length = len(nums)
        answer = [1] * array_length

        # Forward pass: Calculate prefix products
        left_accumulator = 1
        for index in range(array_length):
            answer[index] = left_accumulator
            left_accumulator *= nums[index]
        
        # Backward pass: Multiply by suffix products
        right_accumulator = 1
        for index in range(array_length - 1, -1, -1):
            answer[index] *= right_accumulator
            right_accumulator *= nums[index]
        
        return answer
        