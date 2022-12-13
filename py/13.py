lines = [line.strip() for line in open("13.input").readlines()]

def compare(left, right, indent=""): # -> True/False/None
    print(indent, left, "vs.", right)
    # if left == []:
        # return True
    # if right == []:
        # return False
    if isinstance(left, int) and isinstance(right, int):
        if left == right: return None
        print(indent, "comp", left, right)
        return left < right
    if isinstance(left, int): left = [left]
    if isinstance(right, int): right = [right]
    for i in range(len(left)):
        if len(right) == i: # Right side ran out of items, so inputs are not in the right order
            return False
        c = compare(left[i], right[i], indent+"  ") 
        if c is not None:
            return c
        #if i == len(left)-1: # Left side ran out of items
            #return True
    if len(left) == len(right):
        return None
    print("Left side ran out of items")
    return True # Left side ran out of items
        
result = 0
for i in range(0, len(lines), 3):
    print(lines[i], " vs. ", lines[i+1], "index=", i//3+1)
    p1 = eval(lines[i])
    p2 = eval(lines[i+1])
    print(p1, p2)
    c = compare(p1, p2)
    print(c)
    if c is None:
        print("ERROR", p1, p2, c)
        raise Exception("uh oh")
    elif c:
        result += (i//3+1)

print(result)
