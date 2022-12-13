
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'
lines = [line.strip() for line in open(infile)]
grid = [[ord(c) for c in line.strip()] for line in open(infile)]

# Exhange letter with ints
for ri in range(len(grid)):
    for ci in range(len(grid[0])):
        coor = (ri, ci)
        v = lines[ri][ci]
        if v == "S":
            S = coor
            grid[ri][ci] = ord("a")
        elif v == "E":
            E = coor
            grid[ri][ci] = ord("z")

directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]


def find_path(grid, start, end, is_legal):
    que = [start]
    paths = {start: []}

    while que:
        current = que.pop(0)
        for d in directions:
            r = current[0] + d[0]
            c = current[1] + d[1]
            if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]):
                continue
            new_h = grid[r][c]
            old_h = grid[current[0]][current[1]]
            if not is_legal(new_h, old_h):
                continue
            new_coord = (r, c)
            new_path = paths[current] + [new_coord]

            if new_h == grid[end[0]][end[1]]:
                return new_path

            if not new_coord in paths:
                paths[new_coord] = new_path
                que.append(new_coord)

    return False


shortest_path = find_path(grid, S, E, lambda new, old: new <= old + 1)
if shortest_path:
    ans_1 = len(shortest_path)
    assert(ans_1 == 481)
    print(ans_1)

shortest_path = find_path(grid, E, S, lambda new, old: new >= old - 1)
if shortest_path:
    ans_2 = len(shortest_path)
    assert(ans_2 == 480)
    print(ans_2)
