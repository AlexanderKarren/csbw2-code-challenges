# Time complexity: O(n)
# Space complexity: O(n)

def first_not_repeating_character(s):
    dup_table = {}
    list_length = len(s)
    i = len(s) - 1
    
    while i >= 0:
        # if letter is already in our table,
        if dup_table.get(s[i]) is not None:
            # increment the count
            count = dup_table.get(s[i])[0] + 1
            dup_table.update({s[i]: (count, i, s[i])})
        else:
            # otherwise, set the count to one
            dup_table.update({s[i]: (1, i, s[i])})
        i -= 1
    
    first_instance_index = list_length - 1
    no_dups = True
    print(dup_table)
    for count in dup_table.values():
        # if count in tuple is 1,
        if count[0] == 1:
            no_dups = False
            if count[1] < list_length:
                first_instance_index = count[1]
            
    if no_dups:
        return "_"
            
    return s[first_instance_index]
            
print(first_not_repeating_character("abacabad"))