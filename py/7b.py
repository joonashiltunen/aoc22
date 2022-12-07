class Dir():
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0 # ONLY files on this exact level
        self.children = []
    
dirs = [] # yeah this is probably horribly unnecessary and ugly
current_dir = root = Dir("/", None)

for line in open("7.input").readlines()[1:]: # skip first line with [1:]
    if line.startswith("$ cd"):
        d_str = line.split()[-1]
        if d_str == "..":
            current_dir = current_dir.parent
        else:
            for c in current_dir.children:
                if c.name == d_str:
                    current_dir = c
    elif line[0].isdigit():
        current_dir.size += int(line.split()[0])
    elif line.startswith("dir"):
        new_dir = Dir(line.split()[-1], current_dir)
        current_dir.children.append(new_dir)
        dirs.append(new_dir)
                
def dir_size(d):
    return sum([dir_size(c) for c in d.children]) + d.size

result = root_size = dir_size(root)
free_space_needed = 30000000
free_space = 70000000-root_size
for d in dirs:
    d_size = dir_size(d)
    if d_size > free_space_needed - free_space and d_size < result:
        result = d_size
print(result)
