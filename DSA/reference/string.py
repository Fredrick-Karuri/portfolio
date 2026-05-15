##### String Operations #####

s = " Hello World"

#common operations
print("Lowercase:",s.lower())
print("Uppercase:",s.upper())
print("Split",s.split()) # split on white space by default
print("Split on 'o': ",s.split('o'))

#Joining strings
words = ["Hello","World"]
joined = ' '.join(words)
print("Joined:",joined)

# checking substring
print("'World' in s :", 'World' in s)

# String iteration
for i,char in enumerate(s):
    print(f"Index {i}: {char}")
    if i >=4:
        break
#  Reversing a string
reversed_s = s[::-1] # Slice with step -1
print("Reversed string: ", reversed_s)


# function that returns true if a string is a palindrome
def is_palindrome(s):
    """
    the plan:
    1.start with one pointer at the beginning
    2.start another pointer at the end
    3.compare the characters at both pointers
    4.if they dont match, not a palindrome, return false
    5.if they match, move the pointers closer together and keep checking
    6.if we make it through without finding mismatches, its a palindrome, return true
    """
    left = 0
    right = len(s)-1

    while left < right:
        if not s[left] == s[right]:
            return False
        left +=1
        right -=1
    return True

print("Is 'racecar' a palindrome:" ,is_palindrome("racecar"))