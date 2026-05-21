

def threeSum(self, nums: list[int]) -> list[list[int]]:
    """
    THE PROBLEM: find all unique triplets that add to 0

    PATTERN: sort + two pointer 

    INSIGHT: fix one number, then use two pointers to find pairs that sum to its negative

    THE PLAN: 
    1.sort the array
    2.loop through each number as the "first" number
    3.for each first number, use two pointers(left and right) to find pairs
    4.skip duplicates to avoid duplicate triplets
    5.if sum == 0 , add triplet and move both pointers
    6.if sum < 0 ,move left pointer right (need larger sum)
    7.if sum > 0, move right pointer left (need smaller sum)

    Example: [-1,0,1,2,-1,-4] → sorted: [-4,-1,-1,0,1,2]
    - Fix -1: find two numbers that sum to 1 → found: [-1,0,1]

    """
    nums.sort() #sort first
    result = []
    n = len(nums)

    for i in range(n-2):
        #skip duplicate first numbers
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        #Two pointers for remaining array
        left =i+1
        right= n-1
        target = -nums[i] # we need two numbers that sum to this

        while left < right:
            current_sum = nums[left] +nums[right]

            if current_sum == target:
                result.append([nums[i],nums[left],nums[right]])

                #skip duplicates for left pointer
                while left < right and nums[left] == nums[left +1]:
                    left+=1
                # skip duplicates for right pointer
                while left < right and nums[right] == nums[right-1]:
                    right-=1
                
                left +=1
                right -=1
            elif current_sum <target:
                left +=1 #need larger sum
            else:
                right -=1 # need smaller sum
    return result    
