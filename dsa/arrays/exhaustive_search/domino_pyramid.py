from itertools import permutations

class Solution:
    """
    THE PROBLEM: Given 6 integers representing 6 dominoes, return "YES" if they can be arranged and rotated into a valid 3-level pyramid , "NO" otherwise. 
    A valid pyramid requires each upper domino's halves to match the inner edges of the 
    two dominoes it rests on.

    THE PATTERN: Exhaustive Search (Permutation + bitmask)

    INSIGHT: With only 6 dominoes, the total search space is 6! * 2^6 = 46,080
    combinations  - small enough that bruteforce is optimal. We flatten orientation - trying
    into a bitmask loop: bit i of the mask decides whether domino i is flipped. This keeps
    arrangement(permutation) an orientation(bitmask) as two clean, separate concerns in one
    flat double loop.

    THE PLAN:
    1. Parse 12 integers into 6 domino tuples.
    2. For every permutation of the dominoes(6! = 720):
        For every flip bitmask 0 ... 63 (2^6 = 64 orientations):
        a. Apply flips to produce orientation dominoes: bottom_left, bottom_mid, 
           bottom_right, middle_left, middle_right, top.
        b. Check 6 edge constraints:
            middle_left[0]  == bottom_left[1]   ← middle-left rests on bottom_leftc
            middle_left[1]  == bottom_mid[0]    ← middle-left rests on bottom_mid
            middle_right[0] == bottom_mid[1]    ← middle-right rests on bottom_mid
            middle_right[1] == bottom_right[0]  ← middle-right rests on bottom_right
            top[0]          == middle_left[1]   ← top rests on middle_left
            top[1]          == middle_right[0]  ← top rests on middle_right
    3. Return "YES" on first success, "NO" if all exhausted.

    Example: A = [4,3, 3,4, 1,2, 2,3, 6,5, 4,5]
        Dominoes: (4,3),(3,4),(1,2),(2,3),(6,5),(4,5)
        Valid arrangement after flips:
          Bottom: (1,2),(3,4),(5,6)
          Middle: (2,3),(4,5)
          Top:    (3,4)
        Checks: 2==2, 3==3, 4==4, 5==5, 3==3, 4==4 → "YES"

    TIME: O(1) - Fixed upper bound of 46,080(720*64) iterations regardless of input
    SPACE: O(1) - Only 6 oriented dominoes stored per check

    DESIGN DECISION: Permutations + bitmask over recursive backtracking
    Arrangement (which domino goes where) and orientation( which face points left vs right)
    are independent axes. 
    1. A bitmask encodes all 2^6 (64) flip combos in one integer with
    a cheap bit-shift test(mask >> i & 1) - so if 1&1 we flip
    2. itertools.permutation handles 6!(720) in one line - it is implemented in C
    The result is two clean, flat loops over separated concerns - simpler than backtracking,
    which mixes both decisions into a single recursive state.
    """
    def canBuildPyramid(self, A: list[int]) -> str:
        # Stride through the array in steps of 2 - pairs become tuples
        dominoes = [(A[index],A[index+1]) for index in range(0,12,2)]

        # Permutations: for every ordering of 6 dominoes (720)
        for arrangement in permutations(dominoes):
            # for every flip combination (64)
            # flip_mask - A 6 bit integer. Each bit controls one domino
            for flip_mask in range(64):
                oriented = [
                    (right,left) if (flip_mask >> index) & 1 # flip
                    else (left,right) # normal
                    for index, (left,right) in enumerate(arrangement)
                ]
                # Unpacking
                bottom_left, bottom_mid, bottom_right, middle_left, middle_right, top = oriented

                # Check if the pyramid contacts match
                pyramid_is_valid  = (
                    middle_left[0] == bottom_left[1] and
                    middle_left[1] == bottom_mid[0] and
                    middle_right[0] == bottom_mid[1] and 
                    middle_right[1] == bottom_right[0] and 
                    top[0] == middle_left[1] and 
                    top[1] == middle_right[0]
                )

                if pyramid_is_valid:
                    return "YES"
        return "NO"

if __name__ == "__main__":
    solution = Solution()

    # Given example
    input = [4, 3, 3, 4, 1, 2, 2, 3, 6, 5, 4, 5]
    result = solution.canBuildPyramid(input)
    assert result == "YES", f"Expected YES, got {result}"
    print(f"Example: {input} -> {result}")

    print("\n All tests passed!")

# if __name__ == "__main__":
#     solution = Solution()

#     # Example from the problem — expected: YES
#     example_input = [4, 3, 3, 4, 1, 2, 2, 3, 6, 5, 4, 5]
#     result = solution.canBuildPyramid(example_input)
#     assert result == "YES", f"Expected YES, got {result}"
#     print(f"Example:  {example_input} → {result} ✓")

#     # All identical dominoes — expected: YES (trivially matches)
#     all_same_input = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#     result = solution.canBuildPyramid(all_same_input)
#     assert result == "YES", f"Expected YES, got {result}"
#     print(f"All same: {all_same_input} → {result} ✓")

#     print("\nAll tests passed.")