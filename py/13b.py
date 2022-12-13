lines = [line.strip() for line in open("13.input").readlines() if line.strip()]

def compare(left, right, indent=""): # -> -1/1/0
    if isinstance(left, int) and isinstance(right, int):
        if left == right: return 0
        return left < right and -1 or 1
    if isinstance(left, int): left = [left]
    if isinstance(right, int): right = [right]
    for i in range(len(left)):
        if len(right) == i: # Right side ran out of items, so inputs are not in the right order
            return 1
        c = compare(left[i], right[i], indent+"  ") 
        if c != 0:
            return c
    if len(left) == len(right):
        return 0
    return -1 # Left side ran out of items
        
lines = list(map(eval, lines))
lines.append([[2]])
lines.append([[6]])

import functools
print(lines[0], lines[-1])
lines.sort(key=functools.cmp_to_key(compare))
print(lines[0], lines[-1])

print((lines.index([[2]])+1)*(lines.index([[6]])+1))
