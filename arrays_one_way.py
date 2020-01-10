"""
Input: Str1 and Str2 

Idea: if Lengths of Str1 and Str2 are off by more than 1, then return false 
        Add Str1 strings and Count to Dict
        Remove Str2 letters from Dict. 

        If Len of Dict > 1: then False, else True 

"""

def one_way(str1, str2):
    
    # if Lengths of Str1 and Str2 are off by more than 1, then return false 
    if abs(len(str1) - len(str2)) > 1:
        return False

    str_dict = {}
    letter_count = 0

    # Add Str1 strings and Count to Dict
    for letter in list(str1):
        if letter in str_dict:
            str_dict[letter] += 1
        else:
            str_dict[letter] = 1

    # Remove Str2 letters from Dict. 
    for letter in list(str2):
        if letter in str_dict.keys():
            str_dict[letter] -= 1
        else:
            str_dict[letter] = -1

    # If Len of Dict > 1: then False, else True 
    for (k,v) in str_dict.items():
        if v > 1 or v < -1:
            return False
        elif v == 1 or v == -1:
            letter_count += 1
    
    if letter_count > 1: 
        return False

    return True


print(one_way('ravi','ivar'))
print(one_way('ravi','ivari'))
print(one_way('ravi','ivariv'))

print(one_way('pale','bake'))