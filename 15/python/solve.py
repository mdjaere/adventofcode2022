import sys
import re
import math

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'

lines = [line.strip() for line in open(infile)]


data = [[int(x) for x in re.findall('-?\d+', line)] for line in lines]
sensors, beacons = zip(*[[(sx, sy), (bx, by)] for sx, sy, bx, by in data])
distances = [abs(sx-bx) + abs(sy-by) for sx, sy, bx, by in data]


def x_ranges_at_y(y_line):
    x_ranges = []
    for i in range(len(sensors)):
        sx, sy = sensors[i]
        bx, by = beacons[i]
        distance = abs(sx-bx) + abs(sy-by)
        adjusted_x_distance = distance - abs(sy - y_line)
        this_range = range(sx - adjusted_x_distance,
                           sx + adjusted_x_distance + 1)
        x_ranges.append(this_range)
    return x_ranges


if infile == "example":
    sample_at_y = 10
if infile == "input":
    sample_at_y = 2000000
x_ranges = x_ranges_at_y(sample_at_y)
s_and_b_x_coords = set([x for x, y in beacons + sensors if y == sample_at_y])
x_coords = set.union(*[set(item) for item in x_ranges]
                     ).difference(s_and_b_x_coords)

ans_1 = len(x_coords)
if infile == "input":
    assert(4961647 == ans_1)
print(ans_1)


# Entering rhomboid universe

eight = math.pi/4
sq_two = math.sqrt(2)

def transform(p):
    x, y = p
    return (
        round((x * math.cos(eight) - y * math.sin(eight)) * sq_two),
        round((x * math.sin(eight) + y * math.cos(eight)) * sq_two)
    )


def reverse_transform(p):
    x, y = p
    return (
        round((x * math.cos(-eight) - y * math.sin(-eight)) / sq_two),
        round((x * math.sin(-eight) + y * math.cos(-eight)) / sq_two)
    )


sensors_ = [transform(sensor) for sensor in sensors]
beacons_ = [transform(beacon) for beacon in beacons]

xy_domains_ = [[range(s_[0] - d, s_[0] + d + 1), range(s_[1] - d, s_[1] + d + 1)]
            for d, s_ in zip(distances, sensors_)]

x_values = set()
for x_d, y_d in xy_domains_:
    x_values.add(x_d.start)
    x_values.add(x_d.stop-1)

x_cands = set()
for x in x_values:
    if x + 2 in x_values:
        x_cands.add(x+1)
    if x - 2 in x_values:
        x_cands.add(x-1)

##############

y_values = set()
for x_d, y_d in xy_domains_:
    y_values.add(y_d.start)
    y_values.add(y_d.stop-1)

y_cands = set()
for y in y_values:
    if y + 2 in y_values:
        y_cands.add(y+1)
    if y - 2 in y_values:
        y_cands.add(y-1)

########

for x in x_cands:
    for y in y_cands:
        if any(x in x_range and y in y_range for x_range, y_range in xy_domains_):
            continue
        else:
            xy = reverse_transform((x, y))
            if infile == "example" and all(0 <= x <= 20 for x in xy):
                ans_coord = xy
            if infile == "input" and all(0 <= x <= 4000000 for x in xy):
                ans_coord = xy

ans_2 = ans_coord[0] * 4000000 + ans_coord[1]
if infile == "input":
    assert(ans_2 == 12274327017867)
print(ans_2)
