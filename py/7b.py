class Dir():
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0
        self.children = []
    
dirs = []
current_dir = root = Dir("/", None)

for line in open("7.input").readlines()[1:]:
    if line.startswith("$ cd"):
        d_str = line.split()[-1]
        if d_str == "..":
            current_dir = current_dir.parent
        else:
            current_dir = next(c for c in current_dir.children if c.name == d_str)
    elif line[0].isdigit():
        dir_size_to_increase = current_dir
        while dir_size_to_increase:
            dir_size_to_increase.size += int(line.split()[0])
            dir_size_to_increase = dir_size_to_increase.parent
    elif line.startswith("dir"):
        new_dir = Dir(line.split()[-1], current_dir)
        current_dir.children.append(new_dir)
        dirs.append(new_dir)

result = root.size
extra_space_needed = root.size + 30000000 - 70000000
for d in dirs:
    d_size = d.size
    if d_size > extra_space_needed and d_size < result:
        result = d_size
print(result)
