import sys
infile = sys.argv[1] if len(sys.argv) > 1 else 'input'

area_pairs = [ [ [int(x) for x in p.split("-")] for p in line.strip().split(",")] for line in open(infile)]

score_1 = 0
score_2 = 0
for a, b in area_pairs:
    score_1 += all(a[0] <= x <= a[1] for x in b) or all(b[0] <= x <= b[1] for x in a)
    score_2 += any(a[0] <= x <= a[1] for x in b) or any(b[0] <= x <= b[1] for x in a)
assert(score_1 == 507)
print(score_1)
assert(score_2 == 897)
print(score_2)