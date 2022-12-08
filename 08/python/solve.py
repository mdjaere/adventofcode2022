from functools import reduce
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'
grid = [[int(x) for x in line.strip()] for line in open(infile)]

r_len = len(grid[0])
c_len = len(grid)


def get_dirs(loc):
    return [
        # Left
        ((loc[0], ci) for ci in range(loc[1] - 1, -1, -1)),
        # Right
        ((loc[0], ci) for ci in range(loc[1]+1, c_len)),
        # Up
        ((ri, loc[1]) for ri in range(loc[0] - 1, -1, -1)),
        # Down
        ((ri, loc[1]) for ri in range(loc[0]+1, r_len))
    ]


visible = []

for ri in range(r_len):
    for ci in range(c_len):
        if 0 < ri < r_len and 0 < ci < c_len:
            dirs = get_dirs([ri, ci])
            is_visible = any(all(grid[ri][ci] > grid[d_ri][d_ci]
                                 for d_ri, d_ci in dir) for dir in dirs)
            if is_visible:
                visible.append((ri, ci))
        else:
            visible.append((ri, ci))
ans_1 = len(visible)
assert(ans_1 == 1820)
print(ans_1)


scores = []

for ri in range(r_len):
    for ci in range(c_len):
        dirs = get_dirs([ri, ci])
        dir_score_list = []
        for dir in dirs:
            dir_score = 0
            for d_ri, d_ci in dir:
                if grid[ri][ci] > grid[d_ri][d_ci]:
                    dir_score += 1
                else:
                    dir_score += 1
                    break
            dir_score_list.append(dir_score)
        scores.append(reduce(lambda a, b: a*b, dir_score_list, 1))

ans_2 = max(scores)
assert(ans_2 == 385112)
print(ans_2)
