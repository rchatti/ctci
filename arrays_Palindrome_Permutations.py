"""
Input: Word
Idea: Loop letters and Add Count to dict. If count is Even, then Palindrome, else no
"""

def palindrome_permutation(in_word):
    letter_dict = {}

    # Loop letters and Add Count to dict.
    for letter in list(in_word.lower()):
        if letter in letter_dict.keys():
            letter_dict[letter] += 1 
        else:
            letter_dict[letter] = 1 
    

    ## If count is Even, then Palindrome, else no
    for (k,v) in letter_dict.items():
        if v % 2 != 0:
            return False
        
    return True

print(palindrome_permutation('tata')) ## True 
print(palindrome_permutation('ravi')) ## False 


print(palindrome_permutation('tact coa')) ## False 
