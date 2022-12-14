import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'
lines = [line.strip() for line in open(infile)]

rocks = set()
floor = 0
for line in lines:
    coords = [[int(x) for x in f.split(",")] for f in line.split(" -> ")]
    for i in range(len(coords) - 1):
        s = coords[i]
        e = coords[i + 1]
        xs = sorted([s[0], e[0]])
        ys = sorted([s[1], e[1]])
        for x in range(xs[0], xs[1] + 1):
            for y in range(ys[0], ys[1] + 1):
                floor = max(floor, y+2)
                rocks.add((x, y))


def settle_grain(grain, solids, include_floor=False):
    gr_x, gr_y = grain
    if include_floor and gr_y == floor - 1:
        return False, grain
    candidates = [
        (gr_x, gr_y + 1),
        (gr_x - 1, gr_y + 1),
        (gr_x + 1, gr_y + 1)
    ]
    for c in candidates:
        if c[1] > floor:
            return True, None
        if c not in solids:
            return settle_grain(c, solids, include_floor)
    if grain == (500, 0):
        return True, grain
    return False, grain


# Part 1
solids_1 = set(rocks)
solved = False
while not solved:
    solved, grain = settle_grain((500, 0), solids_1, include_floor=False)
    if grain:
        solids_1.add(grain)

ans_1 = len(solids_1.difference(rocks))
assert(ans_1 == 901)
print(ans_1)


# Part 2
solids_2 = set(rocks)
solved = False
while not solved:
    solved, grain = settle_grain((500, 0), solids_2, include_floor=True)
    if grain:
        solids_2.add(grain)

ans_2 = len(solids_2.difference(rocks))
assert(ans_2 == 24589)
print(ans_2)