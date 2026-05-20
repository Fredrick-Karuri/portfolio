

def removeDuplicates(self, nums: list[int]) -> int:
    '''
    Slow/fast pointer approach:
    since array is sorted, duplicates are adjacent
    use two pointers:
    slow: tracks position where next unique element should go
    fast: scan through array looking for new unique elements

    '''
    if len(nums) == 0:
        return 0
    
    # slow pointer: position for next unique element
    slow = 0

    # fast pointer: scan through the array
    for fast in range(1,len(nums)):
        #found a new unique number?
        if nums[fast] != nums[slow]:
            slow +=1 # move slow forward
            nums[slow]=nums[fast] # place unique number at slow position
    #slow is index of last unique element
    #so number of unique element is slow +1
    return slow +1
