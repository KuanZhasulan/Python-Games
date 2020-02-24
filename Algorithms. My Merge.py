"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result = []
    count = 0
    newline  = []
    result2 = []
    count2 = 0
    for a in range(len(line)):
        result.append(0)
    for a in range(len(line)):
        result2.append(0)    
    for num in line:
        if num != 0:
            result[count] = num
            count += 1
    for num in range(len(result)):
        if num != len(result)-1 and result[num] == result[num+1]:
            newline.append(result[num]+result[num+1])
            result[num+1] = 0
        else:
            newline.append(result[num])
    for num in newline:
        if num != 0:
            result2[count2] = num
            count2 += 1 
    return result2
print merge([2, 0, 2, 2])
print merge([2, 0, 2, 4])
print merge([0, 0, 2, 2])
print merge([2, 2, 0, 0])
print merge([2, 2, 2, 2, 2])
print merge([8, 16, 16, 8])