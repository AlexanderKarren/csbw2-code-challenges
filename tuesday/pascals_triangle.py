# Time complexity O(n)
# Space complexity O(n)

def generate(numRows):
    if numRows <= 0:
        return []
    solution = [[1]]
    
    for i in range(1, numRows):
        prevRow = solution[i - 1]
        row = [1]
        if len(solution[i - 1]) < 2:
            row = [1, 1]
        else:
            for j in range(len(prevRow) - 1):
                sum = prevRow[j] + prevRow[j + 1]
                row.append(sum)
            row.append(1)
        
        solution.append(row)
        
    return solution

print(generate(20))
            