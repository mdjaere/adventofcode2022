import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'
lines = [line.strip().split() for line in open(infile)]

DIR = {"R": (0, +1),
       "L": (0, -1),
       "U": (+1, 0),
       "D": (-1, 0)}


def solve(n):
    knots = [(0, 0)] * n
    seen = set([knots[-1]])
    for line in lines:
        c, v = line
        for _ in range(int(v)):
            dir = DIR[c]
            knots[0] = (knots[0][0] + dir[0], knots[0][1] + dir[1])
            for i in range(len(knots) - 1):
                diff = (knots[i][0] - knots[i + 1][0],
                        knots[i][1] - knots[i + 1][1])
                if 2 in diff or -2 in diff:
                    to_move = [int(x/2) if abs(x) == 2 else x for x in diff]
                    knots[i + 1] = (knots[i + 1][0] + to_move[0],
                                         knots[i + 1][1] + to_move[1])
            seen.add(knots[-1])
    return len(seen)


ans_1 = solve(2)
assert(ans_1 == 5513)
print(ans_1)

ans_2 = solve(10)
assert(ans_2 == 2427)
print(ans_2)