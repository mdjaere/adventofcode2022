from __future__ import annotations
from dataclasses import dataclass
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'
lines = [line.strip() for line in open(infile)]


@dataclass
class File:
    name: str
    size: int


@dataclass
class Folder:
    name: str
    files: list[File]
    folders: list[Folder]
    parent: Folder | None = None
    size: int | None = None

    def get_size(self):
        if self.size == None:
            self.size = sum([f.size for f in self.files] +
                            [folder.get_size() for folder in self.folders])
        return self.size


current_folder = None
folders = []
for line in lines:
    cmd = line.split()
    if cmd[0:2] == ["$", "cd"]:
        # It is a cd command
        if cmd[2] == "..":
            current_folder = current_folder.parent
        else:
            # Entering new folder
            new_folder = Folder(name=cmd[2], files=[], folders=[
            ], parent=current_folder if current_folder else None)
            folders.append(new_folder)
            if current_folder:
                current_folder.folders.append(new_folder)
            current_folder = new_folder
    if not cmd[0] in ["$", "dir"]:
        # It is a file
        new_file = File(size=int(cmd[0]), name=cmd[1])
        current_folder.files.append(new_file)

sum_sub_limit = sum(folder.get_size()
                    for folder in folders if folder.get_size() <= 100000)
ans_1 = sum_sub_limit
assert(ans_1 == 1783610)
print(ans_1)


total_space = 70000000
space_needed = 30000000
current_space = folders[0].get_size()
current_free = total_space - current_space
additional_needed = space_needed - current_free

filtered_folder_sizes = [
    folder.size for folder in folders if folder.get_size() >= additional_needed]
s_f = sorted(filtered_folder_sizes)
ans_2 = s_f[0]
assert(ans_2 == 4370655)
print(ans_2)
