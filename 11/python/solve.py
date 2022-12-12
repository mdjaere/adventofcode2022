import sys
import re
from functools import reduce
from math import floor

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'

with open(infile) as f:
  raw_monkeys = f.read().split("\n\n")


class Monkey():

  def __init__(self, raw):
    self.handling_count = 0
    for line in raw.split("\n"):
      words = line.strip().split()
      if "items" in line:
        self.items = [int(x) for x in re.findall("[0-9]+", line)]
        # print(self.items)
      if "Operation" in line:
        opr = words[-2]
        scalar = words[-1]
        if scalar == "old":
          opr = "**"
          scalar = 2
        operation_string = f"lambda x: x {opr} {scalar}"
        self.operation = eval(operation_string)
      if "Test" in line:
        self.divisor = int(words[-1])
      if "true" in line:
        self.if_true = int(words[-1])
      if "false" in line:
        self.if_false = int(words[-1])


# Part 1

monkeys = [Monkey(m) for m in raw_monkeys]
for _ in range(20):
  for m in monkeys:
    for x in m.items:
      w = m.operation(x)
      w = floor(w / 3)
      next_m = m.if_true if w % m.divisor == 0 else m.if_false
      monkeys[next_m].items.append(w)
      m.handling_count += 1
    m.items = []

s = sorted([m.handling_count for m in monkeys])
ans_1 = s[-1] * s[-2]
print(ans_1)

# Part 2

monkeys_2 = [Monkey(m) for m in raw_monkeys]

common_divisor = reduce(lambda a, b: a * b, [m.divisor for m in monkeys_2], 1)

for i in range(10000):
  for m in monkeys_2:
    for x in m.items:
      w = m.operation(x)
      w = w % common_divisor
      next_m = m.if_true if w % m.divisor == 0 else m.if_false
      monkeys_2[next_m].items.append(w)
      m.handling_count += 1
    m.items = []

s_2 = sorted([m.handling_count for m in monkeys_2])
ans_2 = s_2[-1] * s_2[-2]
print(ans_2)
