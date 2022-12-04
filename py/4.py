with open("4.input") as f:
    lines = [line.strip() for line in f.readlines()]

result = 0
for line in lines:
    p1,p2=line.split(",")
    p1=list(map(int, p1.split("-")))
    p2=list(map(int, p2.split("-")))
    result += int(((p1[0]<=p2[0])&(p1[1]>=p2[1])) | ((p2[0]<=p1[0])&(p2[1]>=p1[1])))
print(result)
