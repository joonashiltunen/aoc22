line = open("6.input").readline() 

all_different = lambda a,b,c,d: a!=b and a!=c and a!=d and b!=c and b!=d and c!=d

i = 3
while i<len(line):
    if all_different(line[i-3], line[i-2], line[i-1], line[i]):
        print(i+1)
        break
    i += 1
