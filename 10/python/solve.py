import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'
lines = [line.strip() for line in open(infile)]

def x_gen():
  for line in lines:
    if not line:
        continue
    if line == "noop":
      yield 0
      continue
    _, v = line.split()
    yield 0
    yield int(v)

to_log = [20, 60, 100, 140, 180, 220]
log = []
cycle = 0
x = 1
out = ""
for to_add in x_gen():
  cycle += 1
  pos = (cycle - 1) % 40
  out += "*" if x - 1 <= pos <= x + 1 else " "
  if pos == 39:
    out += "\n"
  if cycle in to_log:
    log.append(cycle * x)
  x += to_add

ans_1 = sum(log)
assert(ans_1 == 11780)
print(ans_1)

ans_2 = out
print(ans_2)
