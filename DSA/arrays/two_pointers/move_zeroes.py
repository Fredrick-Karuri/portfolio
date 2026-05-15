
def moveZeroes(self, nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.

    problem: move all zeros to the end while maintaining relative order of non-zeros
    example:[0,1,0,3,12] -> [1,3,12,0,0]
    pattern: slow/fast two pointers

    the plan:
    1.initialize slow pointer at index 0(tracks position for next non-zero)
    2.use fast pointer to scan through the entire array
    3.for each element at fastpointer:
        -if nums[fast] is NON-ZERO:
            .swap nums[slow] with nums[fast]
            .move slow pointer forward (slow+=1)
        -if nums[fast] is ZERO:
            .do nothing just continue scanning with fast
    4.after loop completes, all non-zeros will be at the front and all zeros will 
        naturally be at the end

    why it works:
    -slow pointer marks where the next nonzero should go
    -we swap nonzeros to the front pushing zeros backwards
    -by swapping, (not overwriting) we preserve all elements
        
    """
    slow = 0
    array_length= range(len(nums))
    for fast in array_length:
        if nums[fast] != 0:
            nums[slow],nums[fast]=nums[fast],nums[slow]
            slow+=1

