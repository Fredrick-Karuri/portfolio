
# function that finds the two numbers in an array that add up to a target
def two_sum(numbers_array,target):
    """
    the plan:
    1.create empty hashmap to store numbers we have seen and their indices
    2.loop through the array with index and value
    3.calculate the  complement: target - current number
    4.check if complement exists in hashmap
        .if yes , we found the pair, return their indices
        .if no store the current number and its index in hashmap, keep going
    5.if we finish the loop without finding the pair, return None
    
    """

    seen_numbers={}
    for current_index, num in enumerate(numbers_array):
        complement = target - num
        if complement in seen_numbers:
            return [seen_numbers[complement],current_index ] #return both indices
        seen_numbers[num] = current_index # store number with its index
    return None
    

print ("Two sum:",two_sum([2,7,11,15],9))