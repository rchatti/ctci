def check_permutation(str1, str2):
    """
    nipeapple
    pineapple

    add str1 counts to hash table 'a':5, 'b':1, 'z':9
    remove str2 counts from hash table 
    check to see if hash table has count > 1 
    """

    hash_tab = {}
    #     add str1 counts to hash table 'a':5, 'b':1, 'z':9
    for letter in list(str1):
        if letter in hash_tab.keys():
            hash_tab[letter] += 1
        else: 
            hash_tab[letter] = 1

    # remove str2 counts from hash table 
    for letter in list(str2):
        if letter in hash_tab.keys():
            hash_tab[letter] -= 1
        else:
            return False 

    # check to see if hash table has count > 1 
    for (k,v) in hash_tab.items():
        if v > 0: 
            return False
    
    return True


print(check_permutation('nipeapple', 'pineapple'))
print(check_permutation('nipeapple', 'pineapple1'))