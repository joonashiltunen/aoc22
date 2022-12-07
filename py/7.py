class Dir():
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.total_size = 0
        self.children = []
    
dirs = []
current_dir = Dir("/", None)

for line in open("7.input").readlines()[1:]:
    if line.startswith("$ cd"):
        cd_target = line.split()[-1]
        if cd_target == "..":
            current_dir = current_dir.parent
        else:
            current_dir = next(c for c in current_dir.children if c.name == cd_target)
    elif line[0].isdigit():
        dir_size_to_increase = current_dir
        while dir_size_to_increase:
            dir_size_to_increase.total_size += int(line.split()[0])
            dir_size_to_increase = dir_size_to_increase.parent
    elif line.startswith("dir"):
        new_dir = Dir(line.split()[-1], current_dir)
        current_dir.children.append(new_dir)
        dirs.append(new_dir)

print(sum([d.total_size for d in dirs if d.total_size < 100000]))
