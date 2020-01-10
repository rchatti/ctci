def isunique(in_string):
    string_dict = [[] for _ in range(27)]

    for letter in list(in_string):
        hkey = hash(letter) % 26
        
        if len(string_dict[hkey]) == 0:
            string_dict[hkey].append(letter)
        else:
            return False

    return True

print(isunique('abcd'))
print(isunique('abcda'))
