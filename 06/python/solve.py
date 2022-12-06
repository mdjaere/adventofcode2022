infile = "input"

with open(infile) as file:
  line = file.read()

def getMarker(count):
  for i in range(len(line)):
      if len(set(line[i:i+count])) == count:
          return i+count

# Part 1
ans_1 = getMarker(4)
assert(ans_1 == 1848)
print(ans_1)
# Part 2
ans_2 = getMarker(14)
assert(ans_2 == 2308)
print(ans_2)