class Dir():
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0 # ONLY files on this exact level
        self.children = []
    def __repr__(self):
        return f"name={self.name}, parent={self.parent and self.parent.name}, size={self.size}, children={self.children}"
    def __str__(self):
        return self.__repr__()
    
dirs = [] # yeah this is probably horribly unnecessary and ugly
current_dir = Dir("/", None)

I = iter(open("7.input").readlines())
next(I) # skip first line with cd /
try:
    while line := next(I):
        print(line)
        if line[0] == "$":
            if line[2:4] == "cd":
                d_str = line.split()[-1]
                if d_str == "..":
                    current_dir = current_dir.parent
                else:
                    for c in current_dir.children:
                        if c.name == d_str:
                            current_dir = c
        elif line[0] != "d": # not dir -> size
            current_dir.size += int(line.split()[0])
        elif line[0] == "d": # dir
            new_dir = Dir(line.split()[-1], current_dir)
            current_dir.children.append(new_dir)
            dirs.append(new_dir)
                
except StopIteration:
    print(dirs)
    def dir_size(d):
        return sum([dir_size(c) for c in d.children]) + d.size
      
    result = 0
    for d in dirs:
        d_size = dir_size(d)
        if d_size < 100000:
            result += d_size
    print(result)