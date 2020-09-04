# Time complexity: O(n)
# Space complexity: O(n)

def merge_packages(items, limit):
    solution = []
    items_set = set(items)
    match = None
    
    i = len(items) - 1
    
    while i >= 0:
        print(items[i])
        if match is None and limit - items[i] in items_set:
            match = limit - items[i]
            solution.append(i)
        elif match == items[i]:
            solution.append(i)
            
        i -= 1
        
    print(solution)
    
    if len(solution) > 1 and solution[0] < solution[1]:
        solution.reverse()

    return solution

print(merge_packages([4, 6, 10, 15, 16], 21))