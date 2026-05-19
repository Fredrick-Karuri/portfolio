import re
class Solution:
    """
    THE PROBLEM: Given a string S return the maximum number of words found withing a single sentence.
    Sentences are separated by '.', '?' or '!'. A word must contain atleast one letter.

    PATTERN: Regular Expressions

    INSIGHT: Sentences can be extracted by splitting the string on any punctuation mark.('.', '?','!')
    Once separated a sentence can contain extra white space or empty elements so we must count only 
    the tokens that contain atleast one valid alphabetical letter.

    THE PLAN:
    1. Initialize max_word_count to 0
    2. Use regex to split the input string S into individual sentences using delimeters '.', '?', '!'
    3. Loop through each extracted sentence string 
    4. Split the sentence by whitespace characters to extract potential word tokens
    5. Filter the tokens to count only those that contain atleast one alphabetic letter (a-z)(A-Z)
    6. Update max_word_count if the valid word count of the current sentence is higher than the global max.
    7. Return the max_word_count

    Example: S = "We test coders. Give us a try? "
    - Sentence 1: "We test coders" -> words: ["We", "test", "coders"] -> count = 3
    - Sentence 2: " Give us a try" -> words: ["Give", "us", "a", "try"] -> count = 4
    - Sentence 3: " " -> words: [] -> count = 0
    Result: 4

    TIME: O(n) - Where n is the number of characters in string S (We can scan and split a sentence a constant number of times)
    SPACE: O(n) - To store the temporary lists of sentences and word tokens generated during splitting

    DESIGN DECISION: Use re as it handles all three delimeters in one expression without chaining .replace() or writing a loop over delimeter characters. If requirements change - say, add ; s a delimeter, I change one character inside [] not multiple places in custom logic. 
    """
    def maxWordsInSentence(self,S:str):
        max_word_count = 0

        # Split string into individual sentences using punctuation marks as delimeters
        sentences = re.split(r'[.?!]',S)

        for sentence in sentences:
            # Split the sentence by any white space to get raw word tokens
            raw_tokens = sentence.split() # No argument - split on any white space
            current_valid_words = 0

            for token in raw_tokens:
                # Check if token contains any alphaetical character
                if any(char.isalpha() for char in token):
                    current_valid_words += 1
        
            #  Track the maximum count found so far
            max_word_count = max(max_word_count,current_valid_words)
        
        return max_word_count

