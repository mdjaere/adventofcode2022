import sys
import re
import copy
from collections import defaultdict

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'
lines = [line for line in open(infile)]

# Parsing start positions
stacks = defaultdict(list)

for line in lines:
    if "[" in line:
        for m in re.finditer(r"[A-Z]", line):
            pos = int((((m.start()) - 1)/4)+1)
            stacks[pos] = [m[0]] + stacks[pos]

stacks_2 = copy.deepcopy(stacks)

# Solve

for line in lines:
    if "move" in line:
        amount, from_stack, to_stack = [
            int(x) for x in re.findall(r"\d+", line)]
        # Part 1
        to_move = stacks[from_stack][-(amount):]
        del stacks[from_stack][-(amount):]
        stacks[to_stack] = stacks[to_stack] + list(reversed(to_move))
        # Part 2
        to_move_2 = stacks_2[from_stack][-(amount):]
        del stacks_2[from_stack][-(amount):]
        stacks_2[to_stack] = stacks_2[to_stack] + to_move_2

ans = ""
for k in sorted(stacks.keys()):
    ans += stacks[k][-1]
assert(ans == "VGBBJCRMN")
print(ans)

ans_2 = ""
for k in sorted(stacks_2.keys()):
    ans_2 += stacks_2[k][-1]
assert(ans_2 == "LBBVJBRMH")
print(ans_2)
