import sys
import json
import functools

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'
lines = [line.strip() for line in open(infile)]

def is_right_order(a, b, level=0):
    assert(any(isinstance(x, list) for x in [a, b]))
    a, b = [[x] if isinstance(x, int) else x for x in [a, b]]
    i = 0
    while i < len(a) and i < len(b):
        a_item = a[i]
        b_item = b[i]
        if isinstance(a_item, list) or isinstance(b_item, list):
            solve = is_right_order(a_item, b_item, level=level + 1)
            if solve == 0:
                i += 1
                continue
            else:
                return solve
        if a_item == b_item:
            i += 1
            continue
        return a_item - b_item
    if len(a) != len(b):
        return len(a) - len(b)
    return 0

# Part 1

pair_id = 1
result = 0
left = None
right = None
for line in lines:
    if not line:
        pair_id += 1
        left = None
        right = None
        continue
    if left == None:
        left = json.loads(line)
        continue
    right = json.loads(line)
    if is_right_order(left, right) <= 0:
        result += pair_id

ans_1 = result

print(ans_1)

# Part 2

dividers = [[[2]], [[6]]]

packets = [json.loads(line.strip())
           for line in lines if line] + dividers

packets = sorted(packets, key=functools.cmp_to_key(is_right_order))

ans_2 = 1
for divider in dividers:
    ans_2 *= (packets.index(divider) + 1)
print(ans_2)

########

if infile == "example":
    assert(ans_1 == 13)
    assert(ans_2 == 140)
if infile == "input":
    assert(ans_1 == 5292)
    assert(ans_2 == 23868)