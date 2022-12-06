line = open("6.input").readline() 

def all_different(L):
    for i,p in enumerate(L):
        for j,q in enumerate(L):
            if p==q and i!=j:
                return False
    return True

i = 14
while i<len(line):
    if all_different(line[i-14:i]):
        print(i)
        break
    i += 1
