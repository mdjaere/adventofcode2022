import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'

bags = [[]]

for line in open(infile):
  line = line.strip()
  if not line:
    bags.append([])
    continue
  bags[-1].append(int(line))
  
s_bags = sorted(sum(bag) for bag in bags)

ans_1 = s_bags[-1]
assert(70613 == ans_1)
print(ans_1)

ans_2 = sum(s_bags[-3:])
assert(ans_2 == 205805)
print(ans_2)
